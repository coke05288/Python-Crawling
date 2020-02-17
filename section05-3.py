# Section05-3
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(3) - 로그인 처리

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Login 정보(개발자 도구)
login_info = {
    'redirectUrl': 'http://event.danawa.com/experience/',
    'loginMemberType': 'general',
    'id': '',
    'password': ''
}

# Header 정보
headers = {
    "User-Agent" : UserAgent().chrome,
    "referer" : 'https://auth.danawa.com/login?url=http%3A%2F%2Fevent.danawa.com%2Fexperience%2F'
}

with req.session() as s:
    # Request(로그인 시도)
    res = s.post('https://auth.danawa.com/login', login_info, headers=headers)
    
    # 로그인 시도 실패 시 예외
    if res.status_code != 200:
        raise Exception("Login Failed!")

    # 본문 수신 데이터 확인
    # print(res.content.decode('UTF-8'))

    # 로그인 성공 후 세션 정보를 가지고 페이지를 이동
    res = s.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)

    # Euc-Kr(한글이 깨질 경우)
    # res.encoding = 'euc-kr'

    # 페이지 이동 후 수신 데이터 확인
    # print(res.text)

    # bs4 초기화
    soup = BeautifulSoup(res.text, 'html.parser')

    # 로그인 성공 체크
    check_name = soup.find('p', class_='user')
    print(check_name)

    if check_name is None:
        raise Exception('Login Failed, Wrong Password!!')

    # 선택자 사용
    info_list = soup.select("div.my_info > div.sub_info > ul.info_list > li")
    
    # 이 부분에서 재요청, 파일 다운로드, DB저장, 파일쓰기 등의 작업

    # 제목 
    print()
    print("***** My Info *****")
    print()

    for v in info_list:
        # 속성 메소드 확인
        # print(dir(v))

        # 필요한 텍스트 추출
        proc, val = v.find('span').string.strip(), v.find('strong').string.strip()
        print('{} : {}'.format(proc, val))