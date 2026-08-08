import requests
from bs4 import BeautifulSoup

number_counter = 0

url = "https://webscraper.io/test-sites/e-commerce/static?utm_source=chatgpt.com"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

carts = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")

for cart in carts:
    product_name = cart.find("a", class_="title")
    price = cart.find("span", itemprop="price")
    product_description = cart.find("p", class_="description card-text")
    number_counter += 1
    print(number_counter, ".", product_name["title"].strip(), "-", price.text.strip(), "-", product_description.text.strip())

