# -*- coding: utf-8 -*-
import MeCab
with open("data2.txt",'r') as f:
    fi=f.read()

m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
keyword = m.parse(fi)

words = []
for row in keyword.split("\n"):
    word = row.split("\t")[0]
    if word == "EOS":
        break
    else:
        pos = row.split("\t")[1].split(",")[0]
        if pos == "名詞":
                words.append(word)
        '''elif pos == "感嘆詞":
                words.append(word)'''


w =','. join(words)
keywords = w.replace(',',' ')
with open("data3.txt","w") as f:
    f.write(keywords)
print("morphologicalAnalysisSucceeded!")
