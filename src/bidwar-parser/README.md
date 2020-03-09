# Bidwar parser

Python script for fetching and parsing information about bidwars of a marathon.

## Requirements

Python 3 + packages `bs4` and `requests`.

Recommended to install with pip:

```
pip install bs4 requests
```

## Usage example

Fetch all bidwars from Hekathon 19 and print them:

```
import get_bidwars from bidwar-parser

bidwars = get_bidwars("hek19")
for bidwar in bidwars:
    print(bidwar)
```

Should output:

```
('Death Cubed', [('Kill the Robots', '10'), ('Save the Robots', '30')])
('Resident Evil 2 (2019)', [('Arklay Sheriff', '3'), ('Casual', '0'), ('Classic (1998)', '0'), ('Noir', '0'), ('Normal', '0')])
("Mirror's Edge Live Commentary Bias", [('Carlos', '122'), ('Juan', '117')])
('Elder Scrolls Oblivion Character Name', [('Goodigo', '5'), ('I AM SPEED', '5'), ('I AM SPEED', '5'), ('Steamed Hams', '10')])
('Fallout 3 Good vs. Bad Ending', [('Bad Ending', '35'), ('Good Ending', '34')])
('Nintendogs Dog Name', [('Bombay', '16'), ('Borscht', '9'), ('Cat', '10')])
('Uncharted 2 Skin choice', [('Chloe', '0'), ('Jeff', '0'), ('Wetsuit Elena', '2')])
('Jedi Academy Live Commentary Bias', [('Carla', '186'), ('Juanita', '206')])
```