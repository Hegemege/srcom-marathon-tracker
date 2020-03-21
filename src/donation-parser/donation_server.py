from flask import Flask, jsonify, request
from flask_cors import CORS
from donation_parser import get_donations

app = Flask(__name__)
CORS(app)


@app.route("/")
def donations():
    date = request.args.get("date")
    donations = get_donations("hek19", date)
    return jsonify(donations=donations)


if __name__ == "__main__":
    app.run(port=8090)
