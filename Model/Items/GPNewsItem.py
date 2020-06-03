#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/5 14:53
# @Email     : billsteve@126.com
# @Des       : 
# @File        : GPNewsItem
# @Software: PyCharm
from scrapy import Field, Item


class GPNewsItem(Item):
    spider = Field()
    title = Field()
    publish_time = Field()
    news_source = Field()
    read_num = Field()
    content = Field()
    url = Field()
    source_url = Field()

    def __init__(self, *arg, **kw):
        super(GPNewsItem, self).__init__(*arg, **kw)
        self["spider"] = None
        self["title"] = None
        self["publish_time"] = None
        self["news_source"] = None
        self["read_num"] = None
        self["content"] = None
        self["source_url"] = None
