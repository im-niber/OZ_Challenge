import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

req = requests.get(url)

html = req.text
# print(html)

soup = BeautifulSoup(html, "html.parser")

query = soup.select_one("#query")
print(query)


