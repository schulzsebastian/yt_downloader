#!/usr/bin/env python
# -*- coding: utf-8 -*-

from script import youtube_connector
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxx'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = request.form.get('url')
        session['metadata'] = youtube_connector(url)
        return ('', 302)


@app.route('/link')
def link():
    print session['metadata']
    return render_template('link.html',
                           path=session['metadata']['path'],
                           filename=session['metadata']['filename'],
                           title=session['metadata']['title'])


if __name__ == '__main__':
    app.run(debug=True)
