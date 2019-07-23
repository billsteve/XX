#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 10:19
# @Author   : Peter
# @Des       : 
# @File        : BBSItem
# @Software: PyCharm

import XX.Date.DatetimeHelper as ctime
from scrapy import Item, Field


# 帖子模型
class BBSItem(Item):
    # BBS平台 (车质网论坛', 汽车之家论坛,百度贴吧，易车网论坛，易车网)
    platform = Field()
    # 关键字
    keyword = Field()
    # 插入时间
    insert_time = Field()
    # 帖子的url
    bbs_url = Field()
    # 来源的url
    bbs_source_url = Field()
    # 帖子编号 就是论坛的 web_id
    bbs_id = Field()
    # 帖子名字
    bbs_name = Field()
    # 帖子时间
    bbs_time = Field()
    # 帖子楼层  :  实际上是：content
    bbs_floor = Field()
    # 帖子信息(浏览量, 评论量等)
    bbs_info = Field()
    # 爬虫名字
    spider = Field()
    # parameter keywords
    pkeyword = Field()
    # 搜索关键词
    searchword = Field()
    # Job_id
    job_id = Field()
    # car_id
    car_id = Field()
    # cache_info
    cache_info = Field()

    def __init__(self, *args, **kwargs):
        super(BBSItem, self).__init__(self, *args, **kwargs)
        self['platform'] = ''
        self['keyword'] = ''
        self['insert_time'] = ctime.GetNowTime()
        self['bbs_url'] = ''
        self['bbs_name'] = ''
        self['bbs_time'] = ''
        self['bbs_floor'] = ""
        self['bbs_info'] = {}
        self['bbs_source_url'] = ''
        self["bbs_id"] = ""
        self['spider'] = ''
        self['searchword'] = ''
        self["pkeyword"] = ""
        self["job_id"] = ""
        self["car_id"] = ""
        self["cache_info"] = {
            "ts": 86400 * 3,
            "file": True
        }
