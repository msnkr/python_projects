from bs4 import BeautifulSoup
import requests
from termcolor import colored


def comb_hn(url):
    res = requests.get(url)

    if res.ok:
        url_response = res.text

        soup = BeautifulSoup(url_response, "html.parser")

        text = soup.find_all(class_="titleline")
        score = soup.find_all(class_="score")

        count = 0

        for x in range(len(score)):
            current_text = text[count].a.text
            str_current_score = score[count].text
            int_current_score = int(str_current_score.split(" ")[0])

            links = text[count].a["href"]

            if int_current_score > 200:
                print("{} {} points: {}".format(
                    current_text, colored(int_current_score, "green"), links))

            count += 1


page = 1

while page < 10:
    url = "https://news.ycombinator.com/?p={}".format(page)
    comb_hn(url)
    page += 1
