import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# 링크 정보
link_list = []
for i in range(1,4):
    url = f"https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24"
    browser.get(url)

    datalist = browser.find_elements(By.CLASS_NAME, 'gd_name')

    for item in datalist:
        link = item.get_attribute('href')
        link_list.append(link)

    time.sleep(3)

browser.get(link_list[0])

title = browser.find_element(By.CLASS_NAME, 'gd_name').text
author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
rating = browser.find_element(By.CLASS_NAME, 'yes_b').text
reviews = browser.find_element(By.CLASS_NAME, 'txC_blue').text
sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]

ranking_str = browser.find_element(By.CLASS_NAME, "gd_best").text.split(" | ")

ranking = ranking_str[0] 
ranking_weeks = ranking_str[1] 

