from bs4 import BeautifulSoup
import time
import requests

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7", 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
word = input("검색할 단어")

url = "https://www.coupang.com/np/search?component=&q="
url += word

req = requests.get(url, timeout=5, headers= headers)
print(url)
print(req.status_code)

html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")

for item in items:
    name = item.select_one(".name")
    price = item.select_one(".price-value")
    link = item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")

    print(f"제품명: {name.text}")
    print(f"{price.text}원")
    rocket = item.select_one(".badge.rocket")

    if rocket:
        print("로켓 배송 가능")
    else:
        print("")

    print(f"링크: https://www.coupang.com{link}")

    if img_src.get("data-img-src"):
        img_url = f"http:{img_src.get('data-img-src')}"
    else:
        img_url = f"http:{img_src.get('src')}"

    print(f"이미지 URl: {img_url}")