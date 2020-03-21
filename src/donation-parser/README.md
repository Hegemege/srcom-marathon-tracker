# Donation parser

Python script for fetching and parsing information about donations of a marathon.

## Requirements

Python 3 + packages `bs4` and `requests`.

Recommended to install with pip:

```
pip install bs4 requests
```

## Usage example

Fetch all donations since 1556490705 (April 28th 2019 10:31:45 PM GMT) from Hekathon 19 and print them:

```
from donation_parser import get_donations

timestamp = "1556490705"
print("Hekathon 2019 donations since " + timestamp + ":")
donations = get_donations("hek19", timestamp)
for donation in donations:
    print(donation)
```

Should output:

```
Hekathon 2019 donations since 1556490705:
('Mokoan', '$2', 'To the runner, what is your favorite thing/moment when running this game?')
('UltraStars3000', '$2', 'Just because Oddworld is life !')
('Sajiki', '$5', 'yo muffin, really glad you can showcase a rando at a marathon, thanks to you and the entire community :)')
```
