import requests
from bs4 import BeautifulSoup
from termcolor import colored


url = requests.get("https://www.gumtree.co.za/s-all-the-ads/v1b0p1?q=python")
if url.ok:
    soup = BeautifulSoup(url.content, "html.parser")
    job_url = soup.find_all("a", class_="related-ad-title")

    for url in job_url:
        job_title = url.text
        job_href = soup.find("a", class_="related-ad-title").get("href")

        new_url = requests.get("https://www.gumtree.co.za{}".format(job_href))
        job_description = BeautifulSoup(new_url.content, "html.parser")

        job_description_text = job_description.find_all(
            "div", class_="description")

        for description in job_description_text:
            print(colored(job_title, "green"))
            print(description.text)
