from flask import Flask, jsonify
from flask_cors import CORS

from fake_db import bd

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/datos')
def datos():
    return jsonify(bd), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)
