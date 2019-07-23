#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/13 16:06
# @Email     : billsteve@126.com
# @Des       : 创建Spider
# @File        : __CREATE_SPIDER.
# @Software: PyCharm


def createSpiderCode(config):
    code = """
import json
import os
import sys

import XX.Tools.Debug as d
from XX.DB.RedisHelper import *
from scrapy import cmdline
from scrapy_redis.spiders import RedisSpider

sys.path.append("{project_path}")
import Config.db as db


class {class_name}(RedisSpider):
    handle_httpstatus_list = [429, 402, 200]
    name = '{spider}'

    def __init__(self, *args, **kwargs):
        RedisSpider.__init__(self, *args, **kwargs)
        self.parameter = json.loads(kwargs.pop('parameter', '{{}}'))
        self.conn_redis = RedisHelper.getRedisConnect(host=db.REDIS_HOST, pwd=db.REDIS_PWD)
        self.ar = self.parameter['ar'] if 'ar' in self.parameter else ""

        self.ar = kwargs.pop("ar", 0)
        if self.ar:
            for i in range(0, 1):
                url = "{test_url}"
                res = self.conn_redis.lpush(self.name + ":start_urls", url)
                print(" === Add url ===\t" + str(res) + "\t====================\t" + url, flush=True)

    def parse(self, response):
        if 400 <= response.status < 600:
            if response.status == 429 or response.status == 407 or response.status == 402:
                add_res = self.conn_redis.lpush(self.name + ":start_urls", response.url)
                print("==Proxy error=== Status_code is " + str(response.status) + " Readd 2 redis res\t" + str(add_res), flush=True)
            else:
                print("==Not allowed status code==" + str(response.status), flush=True)
        else:
            yield getattr(ParseUtils, self.name)(response.html, response.url)
            # json API
            try:
                json_data = json.loads(response.text)
                if json_data:
                    json_data["url"] = response.url
                    yield json_data
                else:
                    d.d(response.text, line1="---")
            except Exception as e:
                d.d(e, line1="===")
                self.conn_redis.lpush(self.name + ":start_urls", response.url)
                


if __name__ == '__main__':
    spider = [spider for spider in dir() if spider.endswith("Spider") and spider != "RedisSpider" and spider != "Spider"][0]
    cmd = 'scrapy crawl  ' + getattr(globals()[spider], "name") + " -a ar=1"
    cmdline.execute(cmd.split())
"""
    print(str(code).format(**config))


if __name__ == '__main__':
    config = {
        "class_name": "TestSpider",
        "spider": "test",
        "test_url": "https://www.baidu.com",
        "project_path": "D:\\code\\python\\Qcc",
    }
    createSpiderCode(config)
