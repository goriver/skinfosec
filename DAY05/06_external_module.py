from bs4 import BeautifulSoup
from urllib import request

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <h1>Hello External Module </h1>
# <h1>it's my page </h1>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# # print(soup.find('a'))   
# # print(soup.prettify())
# # print(soup.h1.text) # Hello External Module tnvm
# # print(soup.h1) # <h1>Hello External Module tnvm </h1>
# for i in soup.find_all("h1"):
#     print(i)

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target,"html.parser")
for location in soup.select("location"):
    print("도시 : ", location.select_one("city").string)
    print("날씨 : ", location.select_one("wf").string)
    print("최저기온 : ", location.select_one("tmn").string)
    print("최고기온 : ", location.select_one("tmx").string)


"""
news = request.urlopen("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001")
soup = BeautifulSoup(news,"html.parser")
for news_title in soup.select("div ul dt"):
    print(news_title.text.strip())
    # nclicks(fls.list)

"""