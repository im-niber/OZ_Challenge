
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요 : ")
url = base_url + keyword
driver.get(url)

# 스크롤 
# driver.execute_script("window.scrollTo(0,8000)")

# 스크롤 2
for i in range(4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
query = soup.select(".title_link")

for item in query:
    print(item.text)

time.sleep(5)

