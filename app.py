import os
from flask import Flask, jsonify, render_template, send_from_directory, redirect, url_for
from flask_cors import CORS

from pylib.org_parser import parse_dir, pathify, levelify


app = Flask(__name__)
CORS(app)

rootdir = 'notes'


@app.route('/current')
def notes():
    return jsonify(levelify(pathify(parse_dir('notes'))))
    

@app.route('/')
def home():
    return redirect(url_for('root'))

@app.route('/' + rootdir + '/')
def root():
    return send_from_directory('client/build', filename='index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)