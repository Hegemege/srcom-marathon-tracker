# srcom-marathon-tracker

Various scripts and tools useful for tracking marathons on speedrun.com and esamarathon.com


## [OBS Browser sources](src/obs/)

Browser source files for OBS to display trackers

## `speedrun.com` trackers

### [Bidwar parser](src/speedruncom/bidwar_parser/)

Tools for parsing bidwars.

### [Donation parser](src/speedruncom/donation_parser/)

Tools for parsing donations.

### [Incentive parser](src/speedruncom/incentive_parser/)

Tools for parsing donation incentives.

### [Marathon tracker](src/speedruncom/marathon_tracker/)

Tools for tracking the total donation amount.

## `esamarathon.com` trackers

### [Marathon tracker](src/esamarathon/marathon_tracker/)

Tools for tracking the total donation amount.

### [Bids parser](src/esamarathon/bids_parser/)

Tools for parsing bids/bidwars.

## [Tracker server](src/server/)

Flask server for serving the various trackers via an HTTP API.