import requests
from bs4 import BeautifulSoup
import csv

from urllib.parse import urljoin

url = "http://books.toscrape.com"

books_data = []

while True:

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        books_data.append([title, price])

    next_button = soup.find("li", class_="next")

    if next_button:
        next_page = next_button.a["href"]

        url = urljoin(url, next_page)

    else:
        break

with open("all_books_full.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    writer.writerows(books_data)

print("All pages scraped successfully!")
