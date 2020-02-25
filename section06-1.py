# Section 06-1
# Selenium
# Selenium 사용 실습(1) - 설치 및 기본 테스트

# selenium 임포트
from selenium import webdriver

# webdriver 설정(크롬, 파이어폭스 등)
browswer = webdriver.Chrome('./webdriver/chromedriver.exe')
