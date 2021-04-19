# Bid parser (esamarathon.com)

Python script for fetching and parsing information about bidwars of a marathon.

## Requirements

Python 3 + some packages (see `requirements.txt`)

Recommended to setup a virtualenv and install using pip:

```
pip install -r requirements.txt
```

## Usage example

Fetch all bidwars from Hekathon 21 and print them:

```
from bidwar_parser import get_bidwars

bids = get_bids("hekathon", "hek21")
for bid in bids:
    print(bid)
```

Should output:

```
{'name': 'Catgirl Skin', 'run': 'Dustforce DX', 'description': '', 'amount': '$0.00', 'goal': '$12.00', 'categories': []}
{'name': 'Blindfolded Water Escape', 'run': 'Ori and the Will Of The Wisps', 'description': 'Run the Water Escape level Blindfolded.', 'amount': '$0.00', 'goal': '$17.00', 'categories': []}   
{'name': 'Any% Showcase', 'run': 'Brigand: Oaxaca', 'description': '', 'amount': '$0.00', 'goal': '$25.00', 'categories': []}
{'name': 'Costume Selection', 'run': 'Spider-Man (2000)', 'description': '', 'amount': '$0.00', 
'goal': '(None)', 'categories': [{'name': 'Ben Reilly', 'run': 'Spider-Man (2000)', 'amount': '$0.00', 'goal': '(None)', 'scale': 0.0}, {'name': 'Scarlet Spidey', 'run': 'Spider-Man (2000)', 'amount': '$0.00', 'goal': '(None)', 'scale': 0.0}, {'name': 'Spider-Man', 'run': 'Spider-Man (2000)', 'amount': '$0.00', 'goal': '(None)', 'scale': 0.0}]}
{'name': 'catJAM at the End', 'run': 'Magicka 2', 'description': '', 'amount': '$0.00', 'goal': 
'$27.00', 'categories': []}
{'name': 'Commentary Bias', 'run': 'Star Wars: Jedi Knight - Jedi Academy', 'description': 'Commentators are biased towards whichever team has more donations.', 'amount': '$0.00', 'goal': '(None)', 'categories': [{'name': 'Team Carla', 'run': 'Star Wars: Jedi Knight - Jedi Academy', 'amount': '$0.00', 'goal': '(None)', 'scale': 0.0}, {'name': 'Team Juanita', 'run': 'Star Wars: Jedi Knight - Jedi Academy', 'amount': '$0.00', 'goal': '(None)', 'scale': 0.0}]}
...
```
