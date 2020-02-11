# Section03-3
# 기본 스크랩핑 실습
# 다음 주식 정보 가져오기

import json
import urllib.request as req
from fake_useragent import UserAgent


# UserAgent Test (Fake Header 정보 - 가상으로 생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)


# 헤더 정보
headers ={
    "User-agent" : ua.chrome,
    "referer" : 'https://m.finance.daum.net'
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# 응답 데이터 확인(Json Data)
# print('res', res)

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data']

# 중간 확인
# print("중간확인 : ", rank_json, '\n')

for elm in rank_json:
    print("({}) 종목명 : {} | 현재가 : {:g}원 | 등락 : {:g} | 등락률 : {:.2f} %\n"\
    .format(elm['rank'], elm['name'], elm['tradePrice'], elm['changePrice'], elm['changeRate']*100))

# 추가과제
# with open("D:/crawl-test/stock_rank_10.xmlx", "wb") as c:
#     c.write()