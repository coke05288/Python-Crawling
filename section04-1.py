# Section04-1
# Requests
# requests 사용 스크랩핑(1) - Session

import requests

# 세션 활성화
# s = requests.Session()
# r = s.get("http://www.naver.com")

# 수신 데이터
# print(r.text)

# 수신 상태 코드
# print('Status Code : {}'.format(r.status_code))

# 확인
# ok 구문은 if문에서 많이 사용
# print('OK? : {}'.format(r.ok))

# 세션 비활성화
# s.close()

s = requests.Session()

# 쿠키 Return
r1 = s.get("https://httpbin.org/cookies",cookies={"name":"Kim"})
print(r1.text)

# 쿠키 Set
r2 = s.get("https://httpbin.org/cookies/set", cookies={"name":"Kim2"})
print(r2.text)

# User-A
url = 'https://httpbin.org'
headers = {"user-agent" : 'nice-man_1.0.0_win10_ram16_home_chrome'}

# Header 정보 전송
r3 = s.get(url, headers=headers)
print(r3.text)

# 세션 비활성화
s.close()

# width문 사용(권장) -> 파일, DB, HTTP
with requests.Session() as s:
    r = s.get("http://daum.net")
    # print(r.text)
    print(r.ok)
