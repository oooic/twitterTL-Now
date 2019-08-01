# -*- coding:utf-8 -*-
import json,re
import emoji

with open("data.txt","r") as f:
    txt=f.read()

txt= re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,txt)
txt= re.sub(r"&.*?;", "" ,txt)
txt= re.sub(r"@.*?(:|\s)", "" ,txt)
txt= re.sub(r"\n", "" ,txt)
def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)
txt=remove_emoji(txt)

with open ("data2.txt","w") as f:
    f.write(txt)
print("textMoldSucceeded!")
