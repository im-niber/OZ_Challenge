from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

url = "http://naver.com"
driver.get(url)

title = driver.title
print(title)

html = driver.page_source
print(html)