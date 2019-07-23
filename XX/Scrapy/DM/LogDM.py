#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/17 10:53
# @Email     : billsteve@126.com
# @Des       : 
# @File        : LogDM
# @Software: PyCharm
# 记录开始抓了哪些url
import base64
import os
import pickle
import random
import time
import traceback

import XX.Date.DatetimeHelper as ctime
import XX.Encrypt.EncryptHelper as enc
import XX.HTTP.RequestsHelper as creq
import XX.Tools.Proxy as cpxy
import XX.configs as cc
import scrapy
from XX.DB.RedisHelper import *
from XX.Log.LogHelper import *
from logzero import logger
from scrapy.http import TextResponse
from thrift.transport import TSocket


class ToCrawlUrl(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_request(self, request, spider):
        save_path = ToCrawlUrl.settings.get("ROOT_PATH_LOG") + ctime.GetToday() + "_to_crawl.txt"
        logFile(save_path, str(ctime.GetNowTime()) + "\t" + spider.name + "\t" + request.url + "\n", method="a")


# 记录成功抓了哪些url
class CrawledUrl(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_response(self, request, response, spider):
        save_path = CrawledUrl.settings.get("ROOT_PATH_LOG") + ctime.GetToday() + "_carwled.txt"
        logFile(save_path, str(ctime.GetNowTime()) + "\t" + spider.name + "\t" + str(response.status) + "\t" + request.url + "\n",
                method="a")
        return response


