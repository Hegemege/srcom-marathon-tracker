# Marathon tracker

Python script for fetching the marathon donation total.

## Requirements

Python 3 + some packages (see `requirements.txt`)

Recommended to setup a virtualenv and install using pip:

```
pip install -r requirements.txt
```

## Usage example

```
from marathon_tracker import get_marathon_total

print("Hekathon 2021 donations total:")
total = get_esamarathon_marathon_total("hekathon", "hek21")
print(total)
```

Should output

```
Hekathon 2021 donations total:
<integer>
```
