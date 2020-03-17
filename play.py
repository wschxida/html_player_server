# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request
import os


app = Flask(__name__)

legal_suffix = ('WEBM', 'MP4')


@app.route('/')
def index():
    files = os.listdir('static/video')
    for video_file in files:
        for suffix in legal_suffix:
            if suffix in video_file.split('.')[-1].upper():  # Check file in list have a suffix of webm, mp4 or ogg.
                return render_template('index.html', files=files)
    return render_template('404.html', error="Video directory is empty!"), 404


@app.route('/<video_file>')
def play(video_file):
    user_agent = request.headers.get('User-Agent')
    if os.path.exists('static/video/' + video_file):
        for suffix in legal_suffix:
            if suffix in video_file.split('.')[-1].upper():
                return render_template('player.html', user_agent=user_agent, video_file=video_file)
    return render_template('404.html', error="Video file %s doesn't exist!" % video_file), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8508)
