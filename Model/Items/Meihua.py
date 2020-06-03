#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time        : 2018/7/24 14:03
# @Email       : billsteve@126.com
# @File          : Meihua.py
# @Software  : PyCharm


class MediaChannel(object):
    name = ""
    web_id = ""
    count = ""

    def __init__(self, *arg, **kw):
        self.name = kw.get("name", "")
        self.web_id = kw.get("web_id", "")
        self.count = kw.get("count", 0)


class MediaType(object):
    name = ""
    web_id = ""
    count = ""

    def __init__(self, *arg, **kw):
        self.name = kw.get("name", "")
        self.web_id = kw.get("web_id", "")
        self.count = kw.get("count", "")


class MediaInfo(object):
    name = ""
    web_id = ""
    price = ""
    circulation = ""

    def __init__(self, *arg, **kw):
        self.name = kw.get("name", "")
        self.web_id = kw.get("web_id", "")
        self.price = kw.get("price", "")
        self.circulation = kw.get("circulation", "")
