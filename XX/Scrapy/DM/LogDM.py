#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/17 10:53
# @Email     : billsteve@126.com
# @Des       : 
# @File        : LogDM
# @Software: PyCharm
# 记录开始抓了哪些url

import XX.Date.DatetimeHelper as ctime


class ToCrawlUrl(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_request(self, request, spider):
        save_path = ToCrawlUrl.settings.get("ROOT_PATH_LOG") + ctime.get_today() + "_to_crawl.txt"
        log_file(save_path, str(ctime.get_now_time()) + "\t" + spider.name + "\t" + request.url + "\n", method="a")


# 记录成功抓了哪些url
class CrawledUrl(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_response(self, request, response, spider):
        save_path = CrawledUrl.settings.get("ROOT_PATH_LOG") + ctime.get_today() + "_carwled.txt"
        log_file(save_path, str(ctime.get_now_time()) + "\t" + spider.name + "\t" + str(response.status) + "\t" + request.url + "\n",
                method="a")
        return response


