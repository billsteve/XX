#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/14 16:18
# @Author   : Peter
# @Site       : 
# @File        : ForumReview_Count.py
# @Software: PyCharm
import scrapy


class PostReviewItem(scrapy.Item):
    id = scrapy.Field()
    forum_id = scrapy.Field()
    car_id = scrapy.Field()
    review_count = scrapy.Field()

    def __init__(self, *arg, **kw):
        super(PostReviewItem, self).__init__(self, *arg, **kw)
        self.id = None
        self.forum_id = ""
        self.car_id = ""
        self.review_count = ""
