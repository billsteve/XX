#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/14 16:15
# @Author   : Peter
# @Site       : 
# @File        : PostItem.py
# @Software: PyCharm
import time

from scrapy import Field, Item


class PostItem(Item):
    # 帖子基本信息----------------------------------------------------------------
    # 爬虫名字
    spider = Field()
    # 平台
    bbs_forum = Field()
    # 论坛
    bbs_catalog = Field()
    # 插入时间
    bbs_crawl_ts = Field()
    # 帖子的url
    bbs_url = Field()
    # 来源的url
    bbs_source_url = Field()
    # 帖子编号
    bbs_web_id = Field()
    # 标题
    bbs_title = Field()
    # 帖子内容
    bbs_content = Field()
    # 帖子时间
    bbs_time = Field()
    # 帖子楼层
    bbs_floor = Field()
    # parameter keywords
    bbs_url_kw = Field()
    # car_id
    bbs_product_id = Field()
    # 论坛ID
    bbs_forum_id = Field()
    # info
    bbs_info = Field()
    # 头图信息
    bbs_pics = Field()
    # 帖子类型
    bbs_type = Field()
    # --------------------------------

    # 帖子附加信息----------------------------------------------------------------
    # 帖子信息(浏览量, 评论量等)
    bbs_read_num = Field()
    bbs_like_num = Field()
    bbs_comment_num = Field()
    bbs_forward_num = Field()

    # 回复ID
    bbs_reply_id = Field()

    # 发布者信息
    bbs_postor_web_id = Field()
    bbs_postor_name = Field()
    bbs_postor_head_pic = Field()
    bbs_postor_homepage = Field()
    bbs_postor_isvip = Field()
    bbs_postor_islocked = Field()
    bbs_postor_info = Field()

    def __init__(self, *arg, **kw):
        super(Item, self).__init__(*arg, **kw)
        # 设置默认值
        # 爬虫名字
        self["spider"] = None
        # 平台
        self["bbs_forum"] = None
        # 平台
        self["bbs_catalog"] = None
        # 插入时间
        self["bbs_crawl_ts"] = int(time.time())
        # 帖子的url
        self["bbs_url"] = None
        # 来源的url
        self["bbs_source_url"] = None
        # 帖子编号
        self["bbs_web_id"] = None
        # 标题
        self["bbs_title"] = None
        # 帖子内容
        self["bbs_content"] = None
        # 帖子时间
        self["bbs_time"] = None
        # 帖子楼层(1是主贴2是第一个回帖)
        self["bbs_floor"] = None
        # parameter keywords
        self["bbs_url_kw"] = None
        # car_id
        self["bbs_product_id"] = None
        # 论坛ID
        self["bbs_forum_id"] = None
        # info
        self["bbs_info"] = None
        # 图片信息
        self["bbs_pics"] = None
        # 帖子类型
        self["bbs_type"] = None
        # 帖子信息(浏览量, 评论量等)
        self["bbs_read_num"] = 0
        self["bbs_like_num"] = 0
        self["bbs_comment_num"] = 0
        self["bbs_forward_num"] = 0
        # 回复ID
        self["bbs_reply_id"] = None
        # 发布者信息
        self["bbs_postor_web_id"] = None
        self["bbs_postor_name"] = None
        self["bbs_postor_head_pic"] = None
        self["bbs_postor_homepage"] = None
        self["bbs_postor_isvip"] = None
        self["bbs_postor_islocked"] = None
        self["bbs_postor_info"] = None
