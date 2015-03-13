#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

"""
A small utility to download streams from SVT-Play
"""

import requests
import pydoc
import json
import time
import sys
import re

def stripComments(inp):
    inp = str(inp)
    return re.sub(r'(?m)^ *#.*\n?', '', inp)


def progressbar(it, prefix = "", size = 60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()

class streamlist:
    url = ''
    playlists = []
    outFile = ''

    def __init__(self, url):
        streamlist.url = url

    def getPlaylists(self):
        """
        This function gets the url and returns a list of stream URLs
        """
        r = requests.get(streamlist.url + '?output=json')
        jsonData = json.loads(r.text)
        playlistUrl = jsonData['video']['videoReferences'][1]['url']
        f = requests.get(playlistUrl)
        playlist = stripComments(f.text)
        playlist = playlist.splitlines()
        streamlist.playlists = playlist

    def fetchSegments(self, outFile):
        r = requests.get(streamlist.playlists[3])
        urls = stripComments(r.text)
        urls = urls.splitlines()
        with open(outFile, "ab") as output:
            for i in progressbar(range(len(urls)), "Fetching segments: "):
                s = requests.get(urls[i])
                output.write(s.content)
                s.close()
        output.close()

if __name__ == '__main__':
    streamt = streamlist(sys.argv[1])
    streamt.getPlaylists()
    streamt.fetchSegments(sys.argv[2])

