import os
from flask import Flask, jsonify, render_template, send_from_directory, redirect, url_for
from flask_cors import CORS

from pylib import org_parser


app = Flask(__name__)
CORS(app)


@app.route('/current')
def notes():
    return jsonify(org_parser.parse_dir('notes'))
    

@app.route('/')
def home():
    return send_from_directory('client/build', filename='index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)