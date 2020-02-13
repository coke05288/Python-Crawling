# Section04-3
# Requests
# requests 사용 스크랩핑(3) - REST API

import requests

# Rest API : GET, POST, DELETE, PUT : UPDATE, REPLACE(FETCH : UPDATE, MODIFY)
# URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET) ex : www.movies.com/movies/ - 영화를 전부 조회
# POST) ex : www.moviescom/movies/ - 영화를 생성
# PUT ) 수정
# 요청 방식이 달라도 주소는 유지

# 세션 활성화
s = requests.Session()

# # 예제 1) GET 요청
# r = s.get('https://api.github.com/events')
# # 수신상태 체크
# r.raise_for_status()
# # 출력
# for line in r.json():
#     for k, v in line.items():
#         print('Key : {}\nValue : {}'.format(k, v))
#     print()


# # 예제 2) 쿠키 설정
# jar = requests.cookies.RequestsCookieJar()
# # 쿠키 삽입
# jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')
# # 요청
# r = s.get('http://httpbin.org/cookies', cookies=jar)
# # 출력
# print(r.text)


# # 예제 3) timeout
# r = s.get('https://github.com', timeout=5)
# # 출력
# print(r.text)


# # 예제 4) POST
# jar = requests.cookies.RequestsCookieJar()
# r = s.post('http://httpbin.org/post', data={'id':'test77', 'pw':'111'}, cookies=jar)
# # 출력
# print(r.text)
# print(r.headers)


# # 예제 5) 
# # 요청
payload1 = {
    'id':'test77',
    'pw':'111'
}
# payload2 = (
#     ('id', 'test99'),
#     ('pw', '197')
# )
# r = s.post('http://httpbin.org/post', data=payload2)
# # 출력
# print(r.text)


# # 예제 6) PUT
# r = s.put('http://httpbin.org/put', data=payload1)
# print(r.text)


# # 예제 7) DELETE
# r = s.delete('http://httpbin.org/delete',data={'id': 1})
# print(r.text)


# # 예제 8) DELETE
# r = s.delete('https://jsonplaceholder.typicode.com/posts/1',data={'id': 1})
# print(r.ok)
# print(r.text)


# 세션 닫기
s.close()
