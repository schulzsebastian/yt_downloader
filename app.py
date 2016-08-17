#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
from werkzeug.utils import secure_filename
import os 
from script import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxx'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = request.form.get('url')
        session['metadata'] = youtube_connector(url, False)
        return redirect(url_for('link'))

@app.route('/link')
def link():
    return render_template('download.html', metadata=session['metadata'])

@app.route('/download')
def download():
    file = youtube_connector(session['metadata']['url'], True)
    filename = file['title'] + '.mp3'
    return send_from_directory(app.static_folder, filename, as_attachment=True, attachment_filename="%s.mp3" % filename.encode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
