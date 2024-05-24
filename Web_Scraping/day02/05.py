from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
url = "https://kream.co.kr"
# url = "https://kream.co.kr/search?keyword=%EC%8A%88%ED%94%84%EB%A6%BC&tab=products"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".nav-search.icon.sprite-icons").click()
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    sleep(0.5)
# 후드 들고오는 코드

# for i in range(2):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     sleep(2)

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# query = soup.select(".product")

# for item in query:
#     if "hooded" in item.text or "후드" in item.text:
#         name = item.select_one(".name")
#         translated_name = item.select_one(".translated_name")
#         price = item.select_one(".amount")
        
#         print(name.text)
#         print(translated_name.text)
#         print(price.text)
#         print()

# driver.quit()