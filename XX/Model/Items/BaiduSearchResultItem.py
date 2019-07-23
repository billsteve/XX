#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/3/21 14:00
# @File           : BaiduSearchResult
# @Des           : 百度搜索结果Item
# @Email        : billsteve@126.com
import time

from scrapy import Item, Field


# 百度搜索结果
class BaiduSearchResultItem(Item):
    # 平台
    platform = Field()
    # 关键字
    keyword = Field()
    # 爬取时间
    crawl_time = Field()
    # 当前URL
    url = Field()
    # 帖子的真正url
    real_url = Field()
    # 来源的url
    source_url = Field()
    # 帖子名字
    title = Field()
    # 爬虫名字
    spider = Field()
    # 百度跳转URL
    skip_url = Field()
    # 快照URL
    snapshot_url = Field()
    # 快照URL
    show_url = Field()
    # is advertise 是否是广告
    is_ad = Field()
    # content
    content = Field()

    def __init__(self, *args, **kwargs):
        Item.__init__(self, *args, **kwargs)
        self['platform'] = kwargs.get("keyword")
        self['keyword'] = kwargs.get("keyword")
        self['crawl_time'] = int(time.time())
        self['url'] = kwargs.get("url")
        self['real_url'] = kwargs.get("real_url")
        self['title'] = kwargs.get("title")
        self['source_url'] = kwargs.get("title")
        self['spider'] = kwargs.get("spider")
        self['skip_url'] = kwargs.get("skip_url")
        self['snapshot_url'] = kwargs.get("snapshot_url")
        self['show_url'] = kwargs.get("show_url")
        self['is_ad'] = kwargs.get("is_ad")
        self['content'] = kwargs.get("content")
