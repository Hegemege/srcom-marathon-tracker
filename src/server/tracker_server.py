from flask import Flask, jsonify, request
from flask_cors import CORS
from ..speedruncom.donation_parser.donation_parser import get_donations
from ..speedruncom.bidwar_parser.bidwar_parser import get_bidwars
from ..speedruncom.marathon_tracker.marathon_tracker import get_marathon_total
from ..speedruncom.incentive_parser.incentive_parser import get_incentives
from ..esamarathon.bids_parser.bids_parser import get_esamarathon_bids
from ..esamarathon.marathon_tracker.marathon_tracker import (
    get_esamarathon_marathon_total,
)
from ..esamarathon.donation_parser.donation_parser import (
    get_esamarathon_donations,
)

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


@app.route("/esamarathon/bids")
def esamarathon_bids():
    try:
        marathon = request.args.get("marathon")
        marathon_prefix = request.args.get("marathon_prefix")
        title_filter = request.args.get("filter")
        bids = get_esamarathon_bids(marathon_prefix, marathon)
        if title_filter is not None:
            bids = list(filter(lambda x: title_filter in x["run"], bids))
        return jsonify(bids=bids)
    except:
        return handle_error()


@app.route("/esamarathon/marathon-total")
def esamarathon_marathon_total():
    try:
        marathon_prefix = request.args.get("marathon_prefix")
        format_filter = request.args.get("format")
        total = get_esamarathon_marathon_total(marathon_prefix, format_filter == "int")
        return jsonify(total=total)
    except:
        return handle_error()


@app.route("/esamarathon/donations")
def esamarathon_donations():
    try:
        marathon_prefix = request.args.get("marathon_prefix")
        marathon = request.args.get("marathon")
        donations = get_esamarathon_donations(marathon_prefix, marathon)
        return jsonify(donations=donations)
    except:
        return handle_error()


def handle_error():
    print("Parsing failed in", request.url_rule, "with params", dict(request.args))
    traceback.print_exc()
    return "", 500


if __name__ == "__main__":
    app.run(port=8090)
