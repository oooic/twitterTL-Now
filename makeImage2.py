from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image
from random import randint
#単語データを読み込む
font="/Users/oishikota/Library/Fonts/Ronde-B_square.otf"
with open("data3.txt") as f:
    words=f.read()

stop_words = [u'ある', u'こと', u'これ',u'peing',u'質問箱',u'RT',u'よう',u'そう',u'いる',u'もの',u'それ',u'ちゃん',u'さん',u'みたい',u'SleepMeister']

def get_wordcrowd_color_mask( text, imgpath ):
    img_color = np.array(Image.open( imgpath ))
    wc = WordCloud(width=800,
                   height=600,
                   font_path=font,
                   mask=img_color,
                   collocations=False,
                   stopwords=set(stop_words),
                   background_color="#000000" #単語の重複しないように
                  ).generate( text )

    image_colors = ImageColorGenerator(img_color)
    wc.recolor(color_func=image_colors)
    wc.to_file("tlNow.png")

get_wordcrowd_color_mask(words, './hoge.png')
