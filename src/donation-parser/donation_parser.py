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


def get_donations(marathon_url, since_epoch_timestamp):
    try:
        url = (
            "https://www.speedrun.com/ajax_donations.php?marathon="
            + marathon_url
            + "&date="
            + since_epoch_timestamp
        )
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        return parse_donations(soup)
    except BaseException as e:
        print("Parsing donations failed")
        print(e)
        sys.exit(1)


def parse_donations(soup):
    printable = set(string.printable)

    donations = []

    # Merge all read lines into one group
    # Parsingt the lines with bs4 will remove broken HTML and other nastiness
    lines = []

    for donation_item in list(soup.children):
        lines = []
        for entry in donation_item:
            if entry is None:
                continue

            raw_lines = str(entry).strip().split("\n")

            for raw_line in raw_lines:
                raw_line_printable = "".join(filter(lambda x: x in printable, raw_line))
                lines.append(raw_line_printable)

        # BeautifulSoup creates some empty-ish DOM elements every now
        # and then, skip them
        if len(lines) < 10:
            continue

        # Skip the donation total
        if len(list(donation_item.children)) < 5:
            continue

        # Parse the donation author
        raw_donation_author = lines[2]
        raw_donation_author = raw_donation_author.strip()

        if len(raw_donation_author) > 100:
            soup = BeautifulSoup(raw_donation_author, "html.parser")
            raw_donation_author = str(soup.a["href"]).replace("/user/", "")

        raw_donation_amount = lines[5]
        soup = BeautifulSoup(raw_donation_amount, "html.parser")
        raw_donation_amount = soup.string

        raw_donation_message = (
            list(donation_item.children)[7]
            .string.replace("\r", " ")
            .replace("\n", " ")
            .strip()
        )

        raw_donation_message = "".join(
            filter(lambda x: x in printable, raw_donation_message)
        )

        # Example structure
        # ("author", "amount", "comment")
        donation = (raw_donation_author, raw_donation_amount, raw_donation_message)
        donations.append(donation)

    return donations


if __name__ == "__main__":
    main()
