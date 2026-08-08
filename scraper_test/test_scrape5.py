import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://quotes.toscrape.com"


number_count = 0

while True:
    try:
        response = requests.get(url, timeout=10)
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as e:
        print("Request failed", e)
        break
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text")
        author = quote.find("small", class_="author")
        number_count += 1
        print(number_count,".", text.text, "-", author.text)

    pagination = soup.find("li", class_="next")

    if pagination is None:
        break

    next_page = pagination.find("a")["href"]
    url = urljoin(url, next_page)