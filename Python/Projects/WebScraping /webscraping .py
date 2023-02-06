import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


rows = soup.select('ol h3')

row = rows[0]

name = row.select_one('.source-title').text.strip()

print(name)
