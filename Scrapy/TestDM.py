#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/2/15 21:04
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : TestDM.py
# @Des         : 
# @Software : PyCharm


class TestDM(object):
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.settings = settings
        return cls()

    # 读缓存，生成response
    def process_request(self, request, spider):
        print("===" * 44)
        print(self.settings.get("PROJECT_NAME", "crawl"))
        print(self.settings.get("HBASE_ROW_KEY_FUN"))
        self.settings.get("HBASE_ROW_KEY_FUN")()
        print("===" * 44)
