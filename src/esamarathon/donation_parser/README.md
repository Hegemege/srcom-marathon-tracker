# Donation parser

Python script for fetching and parsing information about donations of a marathon.

## Requirements

Python 3 + some packages (see `requirements.txt`)

Recommended to setup a virtualenv and install using pip:

```
pip install -r requirements.txt
```

## Usage example

Fetch all donations since 1620137623 (Tuesday, 4 May 2021 14:07:03 UTC) from Hekathon 21 and print them:

```
from donation_parser import get_donations

print("Hekathon 2021 donations")
donations = get_esamarathon_donations("hekathon", "hek21")
for donation in donations:
    print(donation)
```

Should output (example data):

```
Hekathon 2021 donations:
{'author': 'hegemege', 'timestamp': 1620139016, 'amount': '$2.00'}
{'author': 'hegemege', 'timestamp': 1620137623, 'amount': '$3.00'}   
```

Passing None or a stirng not formatted as an epoch time will likely return all donations for the given marathon.
