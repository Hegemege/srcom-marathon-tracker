# srcom-marathon-tracker

Various scripts and tools useful for tracking marathons on speedrun.com and esamarathon.com


## [OBS Browser sources](src/obs/)

Browser source files for OBS to display trackers

## `speedrun.com` trackers

### [Bidwar parser](src/bidwar_parser/)

Tools for parsing bidwars.

### [Donation parser](src/donation_parser/)

Tools for parsing donations.

### [Incentive parser](src/incentive_parser/)

Tools for parsing donation incentives.

### [Marathon tracker](src/marathon_tracker/)

Tools for tracking the total donation amount.

## `esamarathon.com` trackers

### [Bids parser](src/bids_parser/)

Tools for parsing bids/bidwars.


## Setup development environment
Install dependencies for the trackers and the flask server

```
pip install bs4 requests
pip install -r src/server/requirements.txt
```

Run local environment on port 8090
```
export FLASK_APP=src/server/wsgi.py
flask run -p 8090
```

Trackers in `/obs` should now show some data from localhost:8090
