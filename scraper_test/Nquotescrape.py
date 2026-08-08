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

        # 🔴 FIXED PART STARTS HERE
        tags = quote.find("div", class_="tags")  # (kept your variable)

        tag = tags.find_all("a", class_="tag")   # (this was unused before)

        tags_list = []  # ✅ ADDED: clean storage for tag text

        for t in tag:   # ✅ FIXED: proper loop over tag elements
            tags_list.append(t.text)  # ✅ extract clean text

        # 🔴 FIXED PART ENDS HERE

        quotes_data.append([quote_text, author, tags_list])  # 🔴 FIXED

    next_button = soup.find("li", class_="next")

    if next_button:
        next_page = next_button.a["href"]

        url = urljoin(url, next_page)

    else:
        break

with open("N_all_quotes_data_full.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(quotes_data)

print("Quotes scraped successfully!")