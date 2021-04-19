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

## [Tracker server](src/server/)

Flask server for serving the various trackers via an HTTP API.