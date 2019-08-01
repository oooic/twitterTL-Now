# -*- coding:utf-8 -*-
import json, twitter
import config as config

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
api = twitter.Api(CK, CS, AT, ATS)
with open("tweeetText.txt","r") as f:
    txt=f.read()
api.PostUpdates(status=txt+u"\n#美味しいNLP",media="new.png")
