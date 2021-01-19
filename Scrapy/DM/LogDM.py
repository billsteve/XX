# -*- coding: utf-8 -*-
import logging

import XX.Date.DatetimeHelper as Dt


# 记录开始抓取的URL
class ToCrawlUrl(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_request(self, request, spider):
        save_path = self.settings.get("ROOT_PATH_LOG") + Dt.get_today() + "_to_crawl.log"
        # TODO:
        logging.info(save_path, str(Dt.get_now_time()) + "\t" + spider.name + "\t" + request.url + "\n", method="a")


# 记录成功抓了的URL
class CrawledUrl(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_response(self, request, response, spider):
        save_path = self.settings.get("ROOT_PATH_LOG") + Dt.get_today() + "_carwled.log"
        # TODO:
        logging.info(save_path, str(Dt.get_now_time()) + "\t" + spider.name + "\t" + str(
            response.status) + "\t" + request.url + "\n",
                 method="a")
        return response
