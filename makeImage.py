from wordcloud import WordCloud
import numpy as np
from PIL import Image
from random import randint

font="/Users/oishikota/Library/Fonts/Ronde-B_square.otf"
with open("data3.txt") as f:
    words=f.read()
twitter_mask = np.array(Image.open('twitter.png'))
stop_words = [u'ある', u'こと', u'これ',u'peing',u'質問箱',u'RT',u'よう',u'そう',u'いる',u'もの',u'それ',u'今日',u'みたい']

def myColor(word, font_size, position, orientation, random_state, font_path):
    a=randint(-52,19)
    return (53+a,184+a,236+a)
wordcloud = WordCloud(font_path=font,background_color="#ffffff",stopwords=set(stop_words),mask=twitter_mask,color_func=myColor)
wordcloud.generate(words)
wordcloud.to_file("tlNow.png")
print("Finished!")
