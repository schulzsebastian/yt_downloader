#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    'outtmpl': 'static/%(title)s.%(ext)s'
}

default_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

def youtube_connector(url, download):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            metadata = ydl.extract_info(url, download=download)
        except:
            metadata = ydl.extract_info(default_url, download=download)
            url = default_url
        return {'title': metadata['title'], 'url': url}