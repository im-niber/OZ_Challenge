from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

url = "http://section.cafe.naver.com/ca-fe/home"
driver.get(url)
html = driver.page_source
print(html)

soup = BeautifulSoup(html, "html.parser")
query = soup.select_one("#query")
print(query)

