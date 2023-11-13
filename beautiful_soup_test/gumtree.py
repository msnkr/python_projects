import requests
from bs4 import BeautifulSoup


url = requests.get("https://www.gumtree.co.za/s-all-the-ads/v1b0p1?q=python")
if url.ok:
    soup = BeautifulSoup(url.content, "html.parser")
    job_title = soup.find_all("div", class_="title")
    job_url = soup.find_all("a", class_="related-ad-title")

    for url in job_url:
        print(url)
