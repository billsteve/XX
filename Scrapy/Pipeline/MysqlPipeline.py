#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 放到MySQL数据库


class MysqlPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        cls.cacheFilePath = cls.settings.get("FUN_CACHE_FILE_PATH")
        return cls()

    def process_item(self, item, spider):
        import importlib
        module = importlib.import_module("Helper.Json2Mysql", MysqlPipeline.settings.get("PROJECT_PATH"))
        getattr(module, spider.name)(item, MysqlPipeline.settings.get("MCFG"))
        return item
