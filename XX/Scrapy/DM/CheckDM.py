#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/1/21 20:54
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : CheckDM.py
# @Des         : 
# @Software : PyCharm
import time
from XX.DB.RedisHelper import *
from logzero import logger
import XX.BuiltinFunctions as BF

HBASE_HTML_EXPIRE_TS = 86400 * 30


class Not200(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def __init__(self):
        self.conn_redis = RedisHelper.get_redis_connect(host=self.settings.get("REDIS_HOST"), pwd=self.settings.get("REDIS_PWD"), port=self.settings.get("REDIS_PORT"))

    def process_response(self, request, response, spider):
        if response.status != self.settings.get("STATUS_CODE", 200):
            logger.info("=== Add not 200 set res is \t" + str(self.conn_redis.sadd(spider.name + ":start_urls:not200", response.url)))

        # 延时
        err_count = self.conn_redis.scard(spider.name + ":start_urls:not200")
        for i in range(int(err_count)):
            BF.print_from_head("Has " + str(err_count) + " error url Please wait" + "." * i)
            time.sleep(1)
        return response
