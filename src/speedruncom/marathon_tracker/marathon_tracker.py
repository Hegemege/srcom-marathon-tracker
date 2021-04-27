import requests
import sys
import string


def main():
    print("Hekathon 2019 donations total:")
    total = get_marathon_total("hek19")
    print(total)


def get_marathon_total(marathon_uri):
    url = (
        "https://www.speedrun.com/ajax_donations.php?marathon="
        + marathon_uri
        + "&action=total"
    )
    response = requests.get(url, timeout=5)
    content = response.content.decode("utf-8")
    if len(content) > 10:
        raise Exception("Marathon not found")
    return content


if __name__ == "__main__":
    main()
