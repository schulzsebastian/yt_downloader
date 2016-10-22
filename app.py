#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, send_file
import uuid
import youtube_dl

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    unique_filename = str(uuid.uuid4())
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'static/files/' + unique_filename + '.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        title = ydl.extract_info(url)['title']
        path = 'static/files/' + unique_filename + '.mp3'
    return send_file(path,
                     as_attachment=True,
                     attachment_filename=title.encode('utf-8') + '.mp3')

if __name__ == '__main__':
    app.run(debug=True)
