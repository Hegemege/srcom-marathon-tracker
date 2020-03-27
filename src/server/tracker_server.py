from flask import Flask, jsonify, request
from flask_cors import CORS
from ..donation_parser.donation_parser import get_donations
from ..bidwar_parser.bidwar_parser import get_bidwars
from ..marathon_tracker.marathon_tracker import get_marathon_total
from ..incentive_parser.incentive_parser import get_incentives

app = Flask(__name__)
CORS(app)


@app.route("/donations")
def donations():
    marathon = request.args.get("marathon")
    date = request.args.get("date")
    donations = get_donations(marathon, date)
    return jsonify(donations=donations)


@app.route("/bidwars")
def bidwars():
    marathon = request.args.get("marathon")
    bidwars = get_bidwars(marathon)
    return jsonify(bidwars=bidwars)


@app.route("/marathon-total")
def marathon_total():
    marathon = request.args.get("marathon")
    total = get_marathon_total(marathon)
    return jsonify(total=total)


@app.route("/incentives")
def incentives():
    marathon = request.args.get("marathon")
    incentives = get_incentives(marathon)
    return jsonify(incentives=incentives)


if __name__ == "__main__":
    app.run(port=8090)
