# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["D:/crawl-test/test2.jpg", "D:/crawl-test/index2.html"]

# 다운로드 리소스 url
target_url = ["https://search.pstatic.net/common?type=a&size=120x150&quality=95&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2Fportrait%2F201906%2F20190627094559503.jpg",
"http://google.com"]

for i, url in enumerate(target_url):
    # 예외처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)
        # 수신 내용
        contents = response.read()
        print("-------------------------------")

        # 상태 정보 중간 출력
        print("Header Info-{} : {}".format(i, response.info()))
        print("HTTP Status Code : {}".format(response.getcode()))
        print("-------------------------------")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download Failed.")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download Failed.")
        print("URL Error Reason : ", e.reason)
    # 성공
    else:
        print()
        print("Download Succeed.")
