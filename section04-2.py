# Section04-2
# Requests
# requests 사용 스크랩핑(2) - JSON

import json
import requests

s = requests.Session()

# 100개 JSON 데이터 요청
url = "http://httpbin.org/stream/10"
r = s.get(url, stream=True)

# 수신 확인 
print(r.text)

# Encoding 확인 
print("Encoding : {}".format(r.encoding))

if r.encoding is None:
    r.encoding = "UTF-8"

print("Encoding : {}".format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))

    # JSON(Dict) 변환 후 타입 확인
    b = json.loads(line) # str => dict
    # print(b)
    # print(type(b))

    # 정보내용 출력
    for k, v in b.items():
        print(" Key : {}, Value : {}".format(k,v))

    print()
    print()

s.close()

r = s.get('https://jsonplaceholder.typicode.com/todos/1')

# Header 정보
print(r.headers)

# 본문 정보
print(r.text)

# JSON 변환
print(r.json())

# Key 반환
print(r.json().keys())
print(r.json().values())

# 인코딩 반환
print(r.encoding)

# 바이너리 정보
print(r.content)

s.close()