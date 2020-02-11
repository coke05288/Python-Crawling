# Section03-2
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(2) - RSS

import urllib.request
import urllib.parse

# 중소벤처기업부 : https://www.mss.go.kr
# 중소벤처기업부 RSS : http://116.67.85.22/rss/smba/board/95.do
API = "https://www.mss.go.kr"

params = []

# 81 : 공지사항
# 86 : 보도자료
# 95 : 뉴스레터
# 125 : 고시
# 126 : 사업공고

for num in [81, 86, 95, 125, 126] :
    params.append(num)

# 요청
for c in params:
    # URL 인코딩
    # param = urllib.parse.urlencode(c)
    # print(param)
    # URL 완성
    url = API + "/rss/smba/board/" + str(c) +".do"
    # URL 출력
    print(url)
    # 요청
    res_data = urllib.request.urlopen(url).read()
    # 수신 후 디코딩
    text = res_data.decode('utf-8')
    # 출력
    print("="*50)
    print(text)

