from flask import Flask, jsonify, request
from flask_cors import CORS
from ..donation_parser.donation_parser import get_donations
from ..bidwar_parser.bidwar_parser import get_bidwars
from ..marathon_tracker.marathon_tracker import get_marathon_total
from ..incentive_parser.incentive_parser import get_incentives

import traceback

app = Flask(__name__)
CORS(app)


@app.route("/donations")
def donations():
    try:
        marathon = request.args.get("marathon")
        date = request.args.get("date")
        donations = get_donations(marathon, date)
        return jsonify(donations=donations)
    except:
        return handle_error()


@app.route("/bidwars")
def bidwars():
    try:
        marathon = request.args.get("marathon")
        title_filter = request.args.get("filter")
        bidwars = get_bidwars(marathon)
        if title_filter is not None:
            bidwars = list(filter(lambda x: title_filter in x["title"], bidwars))
        return jsonify(bidwars=bidwars)
    except:
        return handle_error()


@app.route("/marathon-total")
def marathon_total():
    try:
        marathon = request.args.get("marathon")
        total = get_marathon_total(marathon)
        return jsonify(total=int(total))
    except:
        return handle_error()


@app.route("/incentives")
def incentives():
    try:
        marathon = request.args.get("marathon")
        incentives = get_incentives(marathon)
        return jsonify(incentives=incentives)
    except:
        return handle_error()


def handle_error():
    print("Parsing failed in", request.url_rule, "with params", dict(request.args))
    traceback.print_exc()
    return "", 500


if __name__ == "__main__":
    app.run(port=8090)
