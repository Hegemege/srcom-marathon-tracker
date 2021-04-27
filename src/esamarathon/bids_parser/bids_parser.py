from bs4 import BeautifulSoup
import requests
import sys
import string


def main():
    print("Hekathon 2021 bids:")
    bids = get_bids("hekathon", "hek21")
    for bid in bids:
        print(bid)


def get_esamarathon_bids(marathon_prefix, marathon_uri):
    url = "https://{0}.esamarathon.com/bids/{1}".format(marathon_prefix, marathon_uri)
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    return parse_bids(soup)


def parse_bids(soup):
    bids = []

    for hidden in soup.body.find_all(style="display:none;"):
        hidden.decompose()

    bids_raw = list(
        soup.body.findChildren("div", {"class": "container-fluid"}, recursive=False)[
            0
        ].table.children
    )[2:]

    previous_bid = {}

    for row in bids_raw:
        if row.name != "tr":
            continue

        cells = list(row.children)
        if len(cells) == 0:
            continue

        # Length 13 is the run itself, length 3 is the bidwar
        if len(cells) == 13:
            bid_name = cells[1].a.text.strip()
            run_name = cells[3].text.strip()
            bid_description = cells[7].text.strip()
            amount = cells[9].text.strip()
            goal = cells[11].text.strip()

            bid = {}
            bid["name"] = bid_name
            bid["run"] = run_name
            bid["description"] = bid_description
            bid["amount"] = amount
            bid["goal"] = goal
            bid["categories"] = []

            previous_bid = bid

            bids.append(bid)
        else:
            categories = cells[1].tbody
            for category_row in list(categories.children):
                if len(category_row) <= 1:
                    continue
                category_cells = list(category_row.children)

                category_name = category_cells[1].a.text.strip()
                category_run = category_cells[3].text.strip()
                if len(category_run) == 0:
                    category_run = category_cells[5].text.strip()

                category_amount = category_cells[9].text.strip()
                category_goal = category_cells[11].text.strip()

                category = {}
                category["name"] = category_name
                category["run"] = category_run
                category["amount"] = category_amount
                category["goal"] = category_goal

                previous_bid["categories"].append(category)

    # Add relative sizing to each category. [0..1] where 1 is the maximum donation category
    for bid in bids:
        max_donated = 1.0

        if len(bid["categories"]) > 0:
            max_donated_category = max(
                bid["categories"], key=lambda x: float(x["amount"][1:])
            )
            max_donated = max(1.0, float(max_donated_category["amount"][1:]))

        for category in bid["categories"]:
            scale = float(max_donated_category["amount"][1:]) / max_donated
            category["scale"] = scale

    # Sort categories in each bidwar by donated amount descending
    for bid in bids:
        bid["categories"].sort(key=lambda x: x["scale"], reverse=True)

    return bids


if __name__ == "__main__":
    main()
