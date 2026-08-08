import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

counter = 0

while True:
    try:
        response = requests.get(url, timeout=10)
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        break

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="product_pod")
    for article in articles:
        book_titles = article.find("h3").find("a")["title"]
        price = article.find("p", class_="price_color").text
        availability = article.find("p", class_="instock availability").text.strip()
        rating = article.find("p", class_="star-rating")["class"][1]

        price_value = float(price.replace("£", ""))

        if price_value <= 25 and rating in ["Four", "Five"]:
            counter += 1
            print(counter, ".", book_titles, "-", price, "-", availability, "-", rating)

    pagination = soup.find("li", class_="next")
    if pagination is None:
        break

    next_page = pagination.find("a")["href"]

    url = urljoin(url, next_page)

