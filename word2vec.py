import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

fp = codecs.open("./data/2BEXXX09.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text body")
text = body.get_text()


twitter = Twitter()
word_dic = {}
lines = text.split("\r\n")

for line in lines:
    