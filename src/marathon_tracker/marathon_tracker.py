import requests
import sys
import string


def main():
    print("Hekathon 2019 donations total:")
    total = get_marathon_total("hek19")
    print(total)


def get_marathon_total(marathon_uri):
    try:
        url = (
            "https://www.speedrun.com/ajax_donations.php?marathon="
            + marathon_uri
            + "&action=total"
        )
        response = requests.get(url, timeout=5)
        return response.content.decode("utf-8")
    except BaseException as e:
        print("Parsing marathon total failed")
        raise e


if __name__ == "__main__":
    main()
