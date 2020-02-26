# Section 06-1
# Selenium
# Selenium 사용 실습(1) - 설치 및 기본 테스트

# selenium 임포트
from selenium import webdriver

# webdriver 설정(크롬, 파이어폭스 등)
browser = webdriver.Chrome('./webdriver/chromedriver.exe')

# 크롬 브라우저 내부 대기
# 넉넉히 5초정도 대기
browser.implicitly_wait(5)

# 속성확인
# print(dir(browser))

# 브라우저 사이즈
browser.set_window_size(1920,1080) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용
# browser.page_source에 beautifulsoup를 활용하면 파싱 가능
# print("Page Contents : {}".format(browser.page_source))
print()

# 세션 값 출력
print('Session ID : {}'.format(browser.session_id))

# 타이틀 출력
print('Title : {}'.format(browser.title))

# 현재 URL 출력
print('URL : {}'.format(browser.current_url))

# 현재 쿠키 출력
print('Cookies : {}'.format(browser.get_cookies))