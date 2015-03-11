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

def getUrl(url):
    r = requests.get(url + '?output=json')
    jsonData = json.loads(r.text)
    playlistUrl = jsonData['video']['videoReferences'][1]['url']
    print(playlistUrl)
    f = requests.get(playlistUrl)
    print(f.text)
    playlist = stripComments(f.text)
    playlist = playlist.splitlines()
    print(playlist)

if __name__ == '__main__':
    getUrl(sys.argv[1])
