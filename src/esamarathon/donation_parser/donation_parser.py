from bs4 import BeautifulSoup
import requests
import sys
import string
import datetime
import time


def main():
    print("Hekathon 2021 donations")
    donations = get_esamarathon_donations("hekathon", "hek21")
    for donation in donations:
        print(donation)


def get_esamarathon_donations(marathon_prefix, marathon_uri):
    url = "https://{0}.esamarathon.com/donations/{1}".format(
        marathon_prefix, marathon_uri
    )

    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    return parse_donations(soup)


def parse_donations(soup):
    donations = []

    #        donation = {
    #            "amount": raw_donation_amount,
    #            "author": raw_donation_author,
    #            "message": raw_donation_message,
    #            "timestamp": raw_donation_timestamp,
    #        }
    #        donations.append(donation)

    donations_raw = list(
        soup.body.findChildren("div", {"class": "container-fluid"}, recursive=False)[
            0
        ].table.children
    )[3::2]

    for row in donations_raw:
        fields = list(row.children)[1::2]

        timestamp = fields[1].text.strip()
        pattern = "%m/%d/%Y %H:%M:%S %z"
        parsed_time = datetime.datetime.strptime(timestamp, pattern)
        epoch = int(parsed_time.timestamp())

        donation = {
            "author": fields[0].text.strip(),
            "timestamp": epoch,
            "amount": fields[2].text.strip(),
            # last field has Yes if there is a comment, and not the actual comment text??
        }

        donations.append(donation)

    return donations


if __name__ == "__main__":
    main()
