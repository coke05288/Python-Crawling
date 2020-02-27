# Section 06-2
# Selenium
# Selenium 사용 실습(2) - 실습 프로젝트(1)

# selenium 임포트
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from io import BytesIO
import urllib.request as req
import time
import xlsxwriter



chrome_options = Options()
chrome_options.add_argument("--headless")

# 엑셀 처리 선언
workbook = xlsxwriter.Workbook('D:/crawl-test/crawling_results.xlsx')

# 워크 시트
worksheet = workbook.add_worksheet()

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chromedriver.exe', options = chrome_options)
# webdriver 설정(Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome('./webdriver/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(3)

# 브라우저 사이즈
browser.set_window_size(1920, 1080) # maximize_window() minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# 제조사별 더 보기 클릭 1
# Explicitly wait
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더 보기 클릭 2
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label'))).click()

# 2차 페이지 내용
# print('After Page Contents : {}'.format(browserlget_source))

time.sleep(3)

# 현재 페이지 
cur_page = 1

# 크롤링 페이지
target_crawl_num = 3

# 엑셀 행 수
insert_cnt = 1

while cur_page <= target_crawl_num:

    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 소스 코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')   


    # 현재 페이지 확인
    print("현재 페이지 : {}".format(cur_page))
    print()

    # 필요 정보 추출
    for v in pro_list:
        if not v.find('div', class_ = "ad_header"):

            prod_name = v.select('p.prod_name > a')[0].text.strip()
            prod_price = v.select('p.price_sect > a')[0].text.strip()

            # 이미지
            img_data = BytesIO(req.urlopen(v.select('a.thumb_link > img')[0]['data-original']).read())

            # print(v.select('p.prod_name > a')[0].text.strip())
            # print(v.select('a.thumb_link > img')[0]['src'])
            # print(v.select('p.price_sect > a')[0].text.strip())

            # 엑셀 저장(텍스트)
            worksheet.write('A%s'% insert_cnt, prod_name)
            worksheet.write('B%s'% insert_cnt, prod_price)
            # 엑셀 저장(이미지)
            worksheet.insert_image('C%s'% insert_cnt, prod_name, {'image_data' : img_data})

            insert_cnt += 1

        print()
    print()

    # 페이지 별 스크린 샷 저장
    browser.save_screenshot('D:/crawl-test/target-page{}.png'.format(cur_page))

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('종료')
        break

    # 페이지 이동
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    # BeautifulSoup 인스턴스 삭제
    del soup

    # 3초 대기
    time.sleep(3)

    

# 브라우저 종료
browser.quit()

# 엑셀 파일 닫기
workbook.close()