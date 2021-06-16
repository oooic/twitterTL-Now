from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image
from random import randint
from datetime import datetime as dtdt
# 単語データを読み込む
font = "/System/Library/Fonts/Avenir.ttc"
with open("data3.txt", "r", encoding="utf-8-sig") as f:
    words = f.read()

stop_words = ["of", "for", "in", "the", "and", "by", "A", "on", "to"]


def get_wordcrowd_color_mask(text, imgpath):
    freq = dict()
    for w in words.split():
        if w in stop_words:
            continue
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    img_color = np.array(Image.open(imgpath))
    wc = WordCloud(width=300,
                   height=300,
                   font_path=font,
                   mask=img_color,
                   collocations=False,
                   stopwords=set(stop_words),
                   background_color="#ffffff"  # 単語の重複しないように
                   ).fit_words(freq)

    image_colors = ImageColorGenerator(img_color)
    wc.recolor(color_func=image_colors)
    wc.to_file("data/" + str(dtdt.now().timestamp()) + ".png")


get_wordcrowd_color_mask(words, './img/hoge.png')
