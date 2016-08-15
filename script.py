#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import youtube_dl

def download_from_url(url):
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        metadata = ydl.extract_info(url, download=True)
        filename = metadata['title'] + '-' + metadata['display_id'] + '.mp3'
    #del
    os.remove(filename)


download_from_url('https://www.youtube.com/watch?v=dQw4w9WgXcQ')