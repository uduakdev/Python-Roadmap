import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

url = "https://quotes.toscrape.com"

quotes_data = []

while True:

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        quote_text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = quote.find("div", class_="tags")
        tag = tags.find_all("a", class_="tag")
        quotes_data.append([quote_text, author, tags])

    next_button = soup.find("li", class_="next")

    if next_button:
        next_page = next_button.a["href"]

        url = urljoin(url, next_page)

    else:
        break

with open("all_quotes_data_full.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(quotes_data)

print("Quotes scraped successfully!")
