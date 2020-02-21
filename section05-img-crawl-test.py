import os # 폴더 만들 때
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 구글 이미지 크롤링

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-Agent', UserAgent().chrome)]
# Header 정보 삽입
req.install_opener(opener)

base_url = 'https://www.google.co.kr/search?q='
url_img = '&sxsrf=ACYBGNR-MrjwYYOPlwGpCG4JEn_rIUArtw:1582128158380&source=lnms&tbm=isch&sa=X&ved=2ahUKEwih6_nW_t3nAhWTP3AKHZAmD-gQ_AUoAXoECBIQAw&biw=1707&bih=781'

quote = rep.quote_plus('태연')

URL = base_url + quote + url_img

savePath = 'D:/crawl-test/'

# 폴더 생성 예외 처리
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    print("Creation Failed")
    print("folder name : {}".format(e.filename))
else:
    print("Complete Folder Check!")

    
# Request
res = req.urlopen(URL)

# bs4 초기화
soup = BeautifulSoup(res, "html.parser")

# Select

img_list = soup.select('div.bRMDJf.islir > img')

for i, img in enumerate(img_list, 1):
    # print(img['data-iurl'], i)
    fullFileName = os.path.join(savePath, savePath + 'image-' + str(i) + '.png')
    req.urlretrieve(img['data-iurl'], fullFileName)

print("Complete Download!")