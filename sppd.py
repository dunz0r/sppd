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
import sys
import re

def stripComments(inp):
    inp = str(inp)
    return re.sub(r'(?m)^ *#.*\n?', '', inp)


class streamlist:
    url = ''
    playlists = []

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

    def fetchStreams(self):
        r = requests.get(streamlist.playlists[6])
        urls = stripComments(r.text)
        urls = urls.splitlines()
        for y,x in enumerate(urls):
            sys.stdout.write("Fetching segment {0:3d} of {1:3d}\n\r".format(y+1, len(urls)))
            sys.stdout.flush()

if __name__ == '__main__':
    streamt = streamlist(sys.argv[1])
    streamt.getPlaylists()
    streamt.fetchStreams()

