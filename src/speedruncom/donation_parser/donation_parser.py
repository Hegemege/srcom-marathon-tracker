from bs4 import BeautifulSoup
import requests
import sys
import string


def main():
    timestamp = "1556490705"
    print("Hekathon 2019 donations since " + timestamp + ":")
    donations = get_donations("hek19", timestamp)
    for donation in donations:
        print(donation)


def get_donations(marathon_uri, since_epoch_timestamp=None):
    url = "https://www.speedrun.com/ajax_donations.php?marathon=" + marathon_uri
    if since_epoch_timestamp is not None and since_epoch_timestamp.isdigit():
        url += "&date=" + since_epoch_timestamp

    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    return parse_donations(soup)


def parse_raw_lines(donation_item):
    printable = set(string.printable)

    lines = []
    for entry in donation_item:
        if entry is None:
            continue

        raw_lines = str(entry).strip().split("\n")

        for raw_line in raw_lines:
            raw_line_printable = "".join(filter(lambda x: x in printable, raw_line))
            lines.append(raw_line_printable)

    return lines


def parse_donations(soup):
    printable = set(string.printable)

    donations = []

    for donation_item in list(soup.children):
        lines = parse_raw_lines(donation_item)

        # BeautifulSoup creates some empty-ish DOM elements every now
        # and then, skip them
        if len(lines) < 10:
            continue

        # When fetching all donations, there is an extra element at the start
        if len(list(donation_item.children)) < 5:
            donation_item = list(donation_item.children)[1]
            lines = parse_raw_lines(donation_item)

        # Parse the donation author
        raw_donation_author = lines[2]
        raw_donation_author = raw_donation_author.strip()

        if len(raw_donation_author) > 100:
            soup = BeautifulSoup(raw_donation_author, "html.parser")
            raw_donation_author = str(soup.a["href"]).replace("/user/", "")

        raw_donation_amount = lines[5]
        soup = BeautifulSoup(raw_donation_amount, "html.parser")
        raw_donation_amount = soup.string

        raw_donation_timestamp = lines[7]
        soup = BeautifulSoup(raw_donation_timestamp, "html.parser")
        raw_donation_timestamp = soup.td.time["datetime"]

        raw_donation_message = (
            list(donation_item.children)[7]
            .string.replace("\r", " ")
            .replace("\n", " ")
            .strip()
        )

        raw_donation_message = "".join(
            filter(lambda x: x in printable, raw_donation_message)
        )

        donation = {
            "amount": raw_donation_amount,
            "author": raw_donation_author,
            "message": raw_donation_message,
            "timestamp": raw_donation_timestamp,
        }
        donations.append(donation)

    return donations


if __name__ == "__main__":
    main()
