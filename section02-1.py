# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common?type=a&size=120x150&quality=95&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2Fportrait%2F201906%2F20190627094434434.jpg'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = "d:/test1.jpg"
save_path2 = "d:/index.html"

# 예외처리

try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download Failed")
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print("Filename {}".format(file1))
    print("Filename {}".format(file2))

    # 성공
    print("Download Succeed")