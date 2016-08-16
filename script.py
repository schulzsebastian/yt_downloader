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

def download_from_url(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            metadata = ydl.extract_info(url, download=True)
        except:
            metadata = ydl.extract_info(default_url, download=True)
        return metadata['title'] + '.mp3'

def get_url_metadata(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            data = ydl.extract_info(url, download=False)
        except:
            data = ydl.extract_info(default_url, download=False)
        return {'title': data['title'], 'url': data['url']}