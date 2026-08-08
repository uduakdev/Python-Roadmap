import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://news.ycombinator.com"

number_count = 0

while True:
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    post_titles = soup.find_all("span", class_="titleline")

    for post_title in post_titles:
        title = post_title.find("a")
        number_count += 1
        print(number_count, ".", title.text, "-", title["href"])

    pagination = soup.find("a", class_="morelink")

    if pagination is None:
        break

    url = urljoin(url, pagination["href"])