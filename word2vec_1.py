from gensim.models import word2vec

import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

fp = codecs.open("./data/2BEXXX09.txt", "r", encoding="utf-16")

bf = BeautifulSoup(fp, "html.parser")
body = bf.select_one("text body")
text = body.get_text()
lines = text.split("\r\n")

okt = Okt()
results = []
for line in lines:
    words = okt.pos(line, norm=True, stem=True)
    r = []
    for w, s in words:
        if not s in ["Josa", "Eomi", "Punctuation"]:
            r.append(w)
    results.append((" ".join(r)).strip())

output = (" ".join(results)).strip()

with open("./data/toji.wk","w", encoding="utf-8") as fp:
    fp.write(output)

data = word2vec.LineSentence("./data/toji.wk")
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("toji.model")



