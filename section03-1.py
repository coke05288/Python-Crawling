# Section03-1
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청 1 (Encar)
url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)

# 여러 정보
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('read : {}'.format(mem.read(100).decode('utf-8')))
print('parse : {}'.format(urlparse('http://www.encar.co.kr?id=test&pw=1234').query))

# 기본 요청 2 (ipify)
API = "https://api.ipify.org/"

# Get 방식 Parameter
values={
    'format' : 'text' # json, jsonp, txt
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

# 요청 URL 생성
URL = API + "?" + params

print("요청 URL : {}".format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신 데이터 디코딩
text = data.decode('utf-8')
print("response : {}".format(text))