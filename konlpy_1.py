import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

fp = codecs.open("./data/2BEXXX09.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text body")
text = body.get_text()


twitter = Okt()
word_dic = {}
lines = text.split("\r\n")

for line in lines:
    mallist = twitter.pos(line)
    for w, p in mallist:
        if p == "Noun":
            if not (w in word_dic):
                word_dic[w] = 0
            word_dic[w] += 1

keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for w, c in keys[:50]:
    print(f"{w}({c})", end="")

