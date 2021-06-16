from wordcloud import WordCloud
import numpy as np
from PIL import Image
from random import randint

font = "/System/Library/Fonts/Avenir.ttc"
with open("data3.txt") as f:
    words = f.read()
twitter_mask = np.array(Image.open('twitter.png'))
stop_words = ["of", "for", "in", "the", "and", "by", "A"]


def myColor(word, font_size, position, orientation, random_state, font_path):
    a = randint(-52, 19)
    return (53 + a, 184 + a, 236 + a)


wordcloud = WordCloud(
    font_path=font,
    background_color="#ffffff",
    stopwords=set(stop_words),
    mask=twitter_mask,
    color_func=myColor)
wordcloud.generate(words)
wordcloud.to_file("tlNow.png")
print("Finished!")
