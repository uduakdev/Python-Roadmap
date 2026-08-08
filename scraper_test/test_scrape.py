import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url = "https://books.toscrape.com/"

number_count = 0

while True:
    try:
        response = requests.get(url, timeout=10)
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        break
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.find("h3").find("a")
        price = book.find("p", class_="price_color")
        availability = book.find("p", class_="instock availability")

        price_value = float(price.text.replace("£", ""))

        if price_value <= 30:
            number_count += 1
            print(number_count, ".", title["title"], "-", price.text.strip(), "-", availability.text.strip())

    pagination = soup.find("li", class_="next")
    if pagination is None:
        break

    next_page = pagination.find("a")["href"]
    url = urljoin(url, next_page)