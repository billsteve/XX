#!/usr/bin/env python
# encoding: utf-8
import os
import unittest

from scrapy.http.request import Request
from scrapy.http.response.text import TextResponse
from scrapy.spiders import Spider

import XX.File.FileHelper as Fh
from XX.Scrapy.DM.CacheDM import CacheFileRequest


def get_cache_file(url, spider=None, root_path_cache_=""):
    return root_path_cache_ + spider + os.sep + Fh.FileHelper.getMd5Name(url) + ".cache"


class TestCacheDM(unittest.TestCase):
    url = ""

    def setUp(self) -> None:
        self.url = "https://www.li2st1.com"
        self.cache_file_exclude = "list"
        self.cache_file_exclude_ts = 86400

        self.cfr = CacheFileRequest()
        self.cfr.cache_file_exclude = self.cache_file_exclude
        self.cfr.cache_file_exclude_ts = self.cache_file_exclude_ts
        self.cfr.cacheFilePath = get_cache_file

        self.request = Request(url=self.url, body="111")
        self.spider = Spider("name")

    # 在response里写缓存
    def test_write(self):
        self.response = TextResponse(url=self.url, body="OK".encode("utf-8"))
        resp = self.cfr.process_response(self.request, self.response, self.spider)
        self.assertIsInstance(resp, TextResponse)

    # 在request里读缓存
    def test_read(self):
        resp = self.cfr.process_request(self.request, self.spider)
        self.assertIn(type(resp), [None, TextResponse])


if __name__ == '__main__':
    unittest.main()
