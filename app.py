#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = request.form.get('url')
        if not url:
            url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        return redirect(url_for('download', url=url))


@app.route('/download')
def download():
    url = request.args.get('url')
    return render_template('download.html', url=url)


if __name__ == '__main__':
    app.run(debug=True)
