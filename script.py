#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import youtube_dl


def youtube_connector(url):
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
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            metadata = ydl.extract_info(url)
        except:
            metadata = ydl.extract_info(default_url)
            url = default_url
        return {
            'title': metadata['title'],
            'filename': metadata['title'] + '.mp3',
            'path': '/static/' + metadata['title'] + '.mp3'
        }
