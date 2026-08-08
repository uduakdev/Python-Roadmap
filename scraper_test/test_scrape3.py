import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.scrapethissite.com/pages/forms/"

number_count = 0

while True:
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("tr", class_="team")
    for table in tables:
        team_name = table.find("td", class_="name")
        year = table.find("td", class_="year")
        wins = table.find("td", class_="wins")
        number_count += 1
        print(number_count, ".", team_name.text.strip(), "-", year.text.strip(), "-", wins.text.strip())

    pagination = soup.find("a", attrs={"aria-label": "Next"})
    if pagination is None:
        break

    next_page = pagination["href"]
    url = urljoin(url, next_page)