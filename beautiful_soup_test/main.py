from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"
res = requests.get(url)

hacker_dict = {}

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

        if int_current_score > 50:
            print("{} with {} points".format(current_text, int_current_score))

        count += 1
