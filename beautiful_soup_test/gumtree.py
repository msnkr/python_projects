import requests
from bs4 import BeautifulSoup
from termcolor import colored


description = input("What job you looking for?: ")

url = requests.get(
    "https://www.gumtree.co.za/s-jobs/full+time/v1c8a1jtp1?q={}".format(description.replace(" ", "+")))

if url.ok:
    soup = BeautifulSoup(url.content, "html.parser")
    job_urls = soup.find_all("a", class_="related-ad-title")

    for job_url in job_urls:
        job_title = job_url.text
        job_href = job_url.get("href")

        new_url = requests.get("https://www.gumtree.co.za{}".format(job_href))
        job_description_soup = BeautifulSoup(new_url.content, "html.parser")
        job_description = job_description_soup.find(
            "div", class_="description")

        try:
            print(colored(job_title, "green"))
            print(colored("https://www.gumtree.co.za{}".format(job_href), "light_cyan"))
            print(job_description.text)
            print("="*50)
        except AttributeError as err:
            print(colored("No description available", "red"))
            print("="*50)
