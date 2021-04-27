from bs4 import BeautifulSoup
import requests
import sys
import string


def main():
    print("Hekathon 2019 incentives:")
    incentives = get_incentives("hek19")
    for incentive in incentives:
        print(incentive)


def get_incentives(marathon_uri):
    url = "https://www.speedrun.com/" + marathon_uri + "/donate/goals"
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    return parse_incentives(soup)


def get_printable(input_string):
    printable = set(string.printable)
    return "".join(
        filter(lambda x: x in printable, input_string.encode("utf-8").decode("utf-8"))
    )


def print_soup(soup):
    for i in range(len(list(soup.children))):
        print(i, get_printable(list(soup.children)[i]))
        print("-" * 100)


def parse_incentives(soup):
    incentives = []

    content = soup.findAll("div", {"class": "maincontent"})[0]
    content = list(content.children)[3]
    # content is now a long list of mumbo-jumbo containing the incentive data

    # Remove last 3 (garbage)
    content = list(content.children)[:-3]

    # Divide result set into groups of 6 lines
    content = [content[i * 6 : (i * 6) + 6] for i in range(len(content) // 6)]

    for item in content:
        incentive_title = list(item[3].children)[0].strip()
        incentive_closed = False
        if len(list(item[3].children)) >= 4:
            incentive_closed = "Closed" in str(list(item[3].children)[3])
        progress_content = list(item[5].children)[1]
        progress_content = list(progress_content.children)[0].strip()

        progress_content = progress_content.replace("$", "")
        incentive_current, incentive_target = progress_content.split(" of ")

        incentives.append(
            {
                "title": incentive_title,
                "current": incentive_current,
                "target": incentive_target,
                "reached": int(incentive_current) >= int(incentive_target),
                "closed": incentive_closed,
            }
        )

    return incentives


if __name__ == "__main__":
    main()
