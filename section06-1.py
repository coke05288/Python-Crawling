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

# 검색창 input 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('잔나비 최정훈')

# 검색(Form Submit)
element.submit()

# 스크린 샷 저장 1
browser.save_screenshot("D:/crawl-test/website_ch1.png")

# 스크린 샷 저장 2
# browser.get_screenshot_as_file("D:/crawl-test/website_ch2.png")

# 브라우저 종료
browser.quit()