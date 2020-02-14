# Section05-1
# BeautifulSoup
# BeutifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

test_html = """
<html>
    <head>
        <title>The Dormouse's sotry</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is g2 area</h2>
        <p class="title"><b>The Dormouse's Story</b></p>
        <p class="story">Once upon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""

# 예제 1) BeautifulSoup 기초
# bs4 초기화
soup = BeautifulSoup(test_html, 'html.parser')

# 타입 확인
print('soup', type(soup))
# 내용 확인
print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print("h1", h1)

# p 태그 접근
p1 = soup.html.body.p
print("p1",p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling
print("p2", p2)

# 텍스트 출력1
print('h1 >>' , h1.string)

# 텍스트 출력2
print('p >>' , p1.string)

# 텍스트 출력3
print('p2 >>' , p2.string)

# 함수 확인
# print(dir(p2))

# 다음 엘리먼트 확인
# print(list(p2.next_element))

# 반복 출력 확인
# for v in p2.next_element:
#     print(v)

# 예제 2(Find, Find_all)
# bs4 초기화

soup2 = BeautifulSoup(test_html, 'html.parser')

# a 태그 모두 선택
link1 = soup2.find_all('a') # limit=2
# print(type(link1))
print('links', link1)

# 태그 이외에 태그 속성값으로 읽어올 수 있음.
link2 = soup.find_all("a", class_='sister') # id="link2", string="title", string=["Elsie"]
print(link2)

for t in link2:
    print(t)

# 처음 발견한 a 태그 선택
# find와 find_all 의 차이
# find는 하나만 있는 태그 혹은 처음 발견되는 태그만 필요할 때 유용
link3 = soup.find("a")
print()
print(link3)
print(link3.string)
print(link3.text)

print()

# 다중 조건
link4 = soup.find("a", {"class" : "sister", "data-io":"link3"})
print(link4)
print(link4.text)
print(link4.string)

print()

# css 선택자 활용 : select / select_one
# 태그로 접근 : find_all / find
# 예제3(select, select_one)
# 태그 + 클래스 + 자식선택자

link5 = soup.select_one('p.title > b')
print(link5)
print(link5.text)


link6 = soup.select_one('a#link1')
print(link6)
print(link6.text)


link7 = soup.select_one("a[data-io='link3']")
print("ex7 : ", link7)
print("ex7 string : ", link7.string) # . : 클래스 | # : ID

print()

link8 = soup.select("p.story > a")
print("ex8 : ", link8)
for l in link8:
    print(l.string)
    
print()

link9 = soup.select('p.story > a:nth-of-type(2)')
print(link9)

print("==================================================")

link10 = soup.select("p.story")
print(link10)
for t in link10:
    temp = t.find_all("a")
    if temp:
        for v in temp:
            print('>>>>>', v.string)
    else:
        print('-----',t.string)
    
# 데이터를 일단 가져오고 커스텀 하고 싶다. Select / find_all