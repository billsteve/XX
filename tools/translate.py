# -*- coding: utf-8 -*-
import requests

from XX.HTML.UrlHelper import UrlHelper as Uh


def google_translate(txt):
    q = Uh.url_encode(txt)
    url = f"https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&ssel=0&tsel=3&kc=0&tk=550486.961169&q={q}"
    r = requests.get(url)
    return r.json()[0][0][0]
