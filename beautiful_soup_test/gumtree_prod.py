import requests
from bs4 import BeautifulSoup
from termcolor import colored


description = input("What are you looking for?: ")

url = requests.get(
    "https://www.gumtree.co.za/s-all-the-ads/v1b0p1?q={}".format(description.replace(" ", "+")))

if url.ok:
    soup = BeautifulSoup(url.content, "html.parser")
    prod_url = soup.find_all("a", class_="related-ad-title")

    for prod in prod_url:
        prod_name = prod.text
        prod_url = prod.get("href")

        prod_url_req = requests.get(
            "https://www.gumtree.co.za{}".format(prod_url))

        prod_soup = BeautifulSoup(
            prod_url_req.content, "html.parser")
        prod_price = prod_soup.find("span", class_="ad-price").text

        try:
            print("{}: {}".format(
                prod_name, colored(prod_price.strip(), "green")))
        except AttributeError as err:
            print(colored("Not Found", "red"))
