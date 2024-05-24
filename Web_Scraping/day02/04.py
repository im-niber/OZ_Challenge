from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# 브라우저 자동 종료 x
options.add_experimental_option("detach", True)

# 화면 자동 설정s
options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")
# options.add_argument("window-size=500, 500")

# 화면 숨김
# options.add_argument("--headless")

# 음소거 옵션
options.add_argument("--mute-audio")

# 시크릿모드
options.add_argument("incognito")

# 브라우저 상단 메시지 삭제
options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
url = "https://google.com"
driver.get(url)

driver.quit()