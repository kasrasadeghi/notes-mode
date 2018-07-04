from flask import Flask, jsonify, render_template

from pylib import org_parser


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', node=org_parser.parse_file('current.org'))

@app.route('/current')
def notes():
    return jsonify(org_parser.parse_file('current.org'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)