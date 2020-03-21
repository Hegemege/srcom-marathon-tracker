from flask import Flask, jsonify
from flask_cors import CORS
from donation_parser import get_donations

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    donations = get_donations("hek19", "1556490705")
    return jsonify(donations=donations)


if __name__ == "__main__":
    app.run(port=8090)
