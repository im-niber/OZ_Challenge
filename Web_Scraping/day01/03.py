import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" } 

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword
req = requests.get(url, headers=header_user)
html = req.text

soup = BeautifulSoup(html, "html.parser")

results = soup.select(".title_link")
authors = soup.select(".name")

for (item, author) in zip(results, authors):
    print(item.text)
    print(author.text)