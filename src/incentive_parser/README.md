# Incentive parser

Python script for fetching and parsing information about donation incentives of a marathon.

## Requirements

Python 3 + some packages (see `requirements.txt`)

Recommended to setup a virtualenv and install using pip:

```
pip install -r requirements.txt
```

## Usage example

Fetch all incentives from Hekathon 19 and print them:

```
from incentive_parser import get_incentives

incentives = get_incentives("hek19")
for incentive in incentives:
    print(incentive)
```

Should output:

```
{'title': 'Ghost of a Tale Sing the Commanders Incredible Song', 'current': '30', 'target': '30'}
{'title': 'Ghost of a Tale Any% Run', 'current': '34', 'target': '30'}
{'title': 'Rot Gut: Try to get a time of 4:20', 'current': '85', 'target': '42'}
{'title': 'Super Hatty 64', 'current': '75', 'target': '64'}
{'title': 'Ori Wilhelm Frog', 'current': '69', 'target': '50'}
{'title': 'Run Refunct Any% during the final cutscene of HL2', 'current': '80', 'target': '50'}
{'title': 'Gnomes vs. Fairies Music Competition', 'current': '120', 'target': '50'}
{'title': 'Showcase Cornerstone Any%', 'current': '98', 'target': '50'}
{'title': 'Snake Pass Alternate Skin', 'current': '10', 'target': '15'}
```
