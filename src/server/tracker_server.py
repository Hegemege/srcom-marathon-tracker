from flask import Flask, jsonify, request
from flask_cors import CORS
from ..donation_parser.donation_parser import get_donations
from ..bidwar_parser.bidwar_parser import get_bidwars

app = Flask(__name__)
CORS(app)


@app.route("/donations")
def donations():
    date = request.args.get("date")
    donations = get_donations("hek19", date)
    return jsonify(donations=donations)


@app.route("/bidwars")
def bidwars():
    bidwars = get_bidwars("hek19", date)
    return jsonify(bidwars=bidwars)


if __name__ == "__main__":
    app.run(port=8090)
