import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql
import re
from datetime import datetime

browser = webdriver.Chrome()

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='****',
    db='yes24',
    charset='utf8mb4',
 
    cursorclass=pymysql.cursors.DictCursor
)
link_list = []

for i in range(1, 3):
    url = f"https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24"
    browser.get(url)

    datalist = browser.find_elements(By.CLASS_NAME, 'gd_name')

    for item in datalist:
        link = item.get_attribute('href')
        link_list.append(link)

    time.sleep(2)

with connection.cursor() as cur:
    for i in range(1, len(link_list)):
        browser.get(link_list[i])

        title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        print(i)
        print(title)
        author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text

        publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text

        match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)
        if match:
            year, month, day = match.groups()
            date_obj = datetime(int(year), int(month), int(day))
            publishing = date_obj.strftime("%Y-%m-%d")
        else:
            publishing = "2222-02-22"

        review = browser.find_element(By.CLASS_NAME, 'txC_blue').text

        rating = browser.find_element(By.CLASS_NAME, 'yes_b').text

        try:
            review = int(review.replace(",", ""))
        except:
            review = 0
            rating = 0

        sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
        sales = int(sales.replace(",", ""))

        price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
        price = int(price.replace(",", ""))
        
        full_text = browser.find_element(By.CLASS_NAME, "gd_best").text
        parts = full_text.split(" | ")

        if len(parts) == 1:
            ranking = 0
            ranking_weeks = 0
        else:

            try:
                ranking_part = parts[0]
                ranking = ''.join(filter(str.isdigit,ranking_part))
            except:
                ranking = 0

            try:
                ranking_weeks_part = parts[1]
                ranking_weeks = ''.join(filter(str.isdigit, ranking_weeks_part.split()[-1]))
            except:
                ranking_weeks = 0

        sql = """insert into Books(
            title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks
            )
            VALUES(
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """
        cur.execute(sql, (title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
        connection.commit()
        time.sleep(2)