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

print("Hekathon 2019 donations total:")
total = get_marathon_total("hek19")
print(total)
```

Should output

```
Hekathon 2019 donations total:
1634
```
