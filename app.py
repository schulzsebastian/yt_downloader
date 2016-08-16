#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for, session, send_file
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
        session['metadata'] = get_url_metadata(url)
        return redirect(url_for('download'))

@app.route('/download')
def download():
    filename = download_from_url(session['metadata']['url'])
    return send_file(app.static_folder + '/' + filename)

if __name__ == '__main__':
    app.run(debug=True)
