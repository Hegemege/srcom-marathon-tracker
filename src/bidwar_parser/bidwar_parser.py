from bs4 import BeautifulSoup
import requests
import sys
import string


def main():
    print("Hekathon 2019 bidwars:")
    bidwars = get_bidwars("hek19")
    for war in bidwars:
        print(war)


def get_bidwars(marathon_uri):
    url = "https://www.speedrun.com/" + marathon_uri + "/donate/bidwars"
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    return parse_bidwars(soup)


def parse_bidwars(soup):
    printable = set(string.printable)

    find_bidwars = False
    find_title = False
    next_line_value = False
    find_closed_line = 0

    # Example structure
    # ("bidwar_title", [("bidwar_category", "donation_amount"), ...])
    current_bidwar = None

    bidwars = []

    # Merge all read lines into one group
    # Parsing the lines with bs4 will remove broken HTML and other nastiness
    lines = []
    for item in list(soup.children):
        group_line = item.encode("utf-8").decode("utf-8")
        raw_lines = group_line.split("\n")

        for raw_line in raw_lines:
            raw_line_printable = "".join(filter(lambda x: x in printable, raw_line))
            lines.append(raw_line_printable)

    for line in lines:
        if '<div class="panel panel-tabbed">' in line:
            find_bidwars = True
            continue

        if find_bidwars == False:
            continue

        # Parse bidwars
        if '<div class="panel">' in line:
            find_title = True
            continue

        # Find the title of the bidwar
        if find_title:
            find_title = False
            find_closed_line = 3
            # Example line: <p>Resident Evil 2 (2019)</p></div>
            title = line.replace("<p>", "").split("<")[0]

            if current_bidwar is not None:
                bidwars.append(current_bidwar)

            current_bidwar = {"title": title, "categories": [], "closed": False}

        # See if the bidwar is closed or not
        if find_closed_line > 0:
            find_closed_line -= 1
            if find_closed_line == 0:
                current_bidwar["closed"] = "Closed" in line

        # Find the line that contains the values of the bidwar
        if '<div class="progress-text">' in line:
            next_line_value = True
            continue

        # Parse the progress of the bidwar
        if next_line_value:
            next_line_value = False
            # Example line: Kill the Robots ($10)
            # with a bunch of \t and other crap around

            # Find the numerical value between the last two parentheses on the line
            start_index = line.rfind("(")
            end_index = line.rfind(")")

            # start_index contains the opening parenthesis, thus +1
            # Another +1 to skip the currency symbol
            donated = line[start_index + 2 : end_index]

            line_cleaned = line.strip()
            end_index = line_cleaned.rfind("(")
            # -1 to take away the last space between the category name and the parenthesis
            category = line.strip()[: end_index - 1]

            current_bidwar["categories"].append(
                {"category": category, "donated": donated}
            )

    # Add last bidwar
    if current_bidwar is not None:
        bidwars.append(current_bidwar)

    return bidwars


if __name__ == "__main__":
    main()
