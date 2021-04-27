from bs4 import BeautifulSoup
import requests
import sys
import string


def main():
    print("Hekathon 2021 donations total:")
    total = get_esamarathon_marathon_total("hekathon")
    print(total)


def get_esamarathon_marathon_total(marathon_prefix, truncInt=True):
    url = "https://{0}.esamarathon.com/index".format(marathon_prefix)
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    return parse_total(soup, truncInt)


def parse_total(soup, truncInt):
    donation_summary = soup.body.findChildren("small")[0].text
    donation_total_raw = donation_summary.split("$")[1].split(" ")[0]
    donation_total = float(donation_total_raw)
    if truncInt:
        return int(donation_total)
    return donation_total


if __name__ == "__main__":
    main()
