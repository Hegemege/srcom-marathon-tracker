# Donation parser

Python script for fetching and parsing information about donations of a marathon. Also contains simple Flask + WSGI server scripts (e.g. to use with a nginx reverse proxy) and a OBS tracker to buffer and display donations with a simple popup animation.

## Requirements

Python 3 + some packages (see `requirements.txt`)

Recommended to setup a virtualenv and install using pip:

```
pip install -r requirements.txt
```

## `donation_parser` usage example

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
{'amount': '$2', 'author': 'Mokoan', 'message': 'To the runner, what is your favorite thing/moment when running this game?', 'timestamp': '2019-04-29T02:13:05Z'}
{'amount': '$2', 'author': 'UltraStars3000', 'message': 'Just because Oddworld is life !', 'timestamp': '2019-04-29T00:15:06Z'}
{'amount': '$5', 'author': 'Sajiki', 'message': 'yo muffin, really glad you can showcase a rando at a marathon, thanks to you and the entire community :)', 'timestamp': '2019-04-28T23:30:51Z'}
```

Passing None or a stirng not formatted as an epoch time will likely return all donations for the given marathon.
