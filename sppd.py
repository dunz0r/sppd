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

import subprocess
import requests
import pydoc
import json
import sys
import re

def stripComments(inp):
    inp = str(inp)
    return re.sub(r'(?m)^ *#.*\n?', '', inp)


class sppd:
    url = ''

    def __init__(self, url):
        print("hello")
        sppd.url = url

    def getUrls(self):
        """
        This function gets the url and returns a list of stream URLs
        """
        r = requests.get(sppd.url + '?output=json')
        jsonData = json.loads(r.text)
        playlistUrl = jsonData['video']['videoReferences'][1]['url']
        f = requests.get(playlistUrl)
        playlist = stripComments(f.text)
        playlist = playlist.splitlines()
        print playlist
        return playlist

    def fetchStreams(self,playlist):
        print(playlist)


if __name__ == '__main__':
    stream = sppd(sys.argv[1])
    stream.getUrls()

