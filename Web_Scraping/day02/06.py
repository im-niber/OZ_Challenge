from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(1)

# 다시 접속해서 광고 건너뜀
driver.get(url)
time.sleep(1)

# 버튼 순서로 차트 클릭 + 더보기 버튼도 순서로 나눔.
btns = driver.find_elements(By.CSS_SELECTOR, ".nav_item")
driver.find_elements(By.CSS_SELECTOR, ".nav_item")[2].click()
time.sleep(1)

# 모든 더보기 버튼을 다 누른다음에, 노래 순위만 들고오면 될 줄 알았는데
# 노래 차트의 더보기 버튼을 누르려면 차트 화면쪽이 active 되어야 가능해서
# 다 누르는 방식은 좀 더 작업이 들어가지 싶어서, 순서를 찾아서 노래 순위 더 보기 버튼만
# 클릭하였다.
moreBtns = driver.find_elements(By.ID, "moreBtn")
time.sleep(1)

moreBtns[1].click()
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

rank = soup.select(".ranking_num")
title = soup.select(".list_music > .list_item > .content > .inner > a > .title")
name = soup.select(".list_music > .list_item > .content > .inner > a > .name")

for rank, title, name in zip(rank, title, name):
    print(f"순위 : {rank.text}")
    print(f"노래 제목 : {title.text.replace("\n", "").replace("\t", "")}")
    print(f"가수 이름 : {name.text}")
    
driver.quit()