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
    playlist = []

    def __init__(self, url):
        print("hello")
        streamlist.url = url

    def getUrls(self):
        """
        This function gets the url and returns a list of stream URLs
        """
        r = requests.get(streamlist.url + '?output=json')
        jsonData = json.loads(r.text)
        playlistUrl = jsonData['video']['videoReferences'][1]['url']
        f = requests.get(playlistUrl)
        playlist = stripComments(f.text)
        playlist = playlist.splitlines()
        streamlist.playlist = playlist

    def fetchStreams(self):
        print(streamlist.playlist)


if __name__ == '__main__':
    streamt = streamlist(sys.argv[1])
    streamt.getUrls()
    streamt.fetchStreams()

