from flask import Flask, jsonify

import org_parser


app = Flask(__name__)

@app.route('/current')
def notes():
    return jsonify(org_parser.parse_file('current.org').json())

if __name__ == '__main__':
    app.run(debug=True, port=5000)