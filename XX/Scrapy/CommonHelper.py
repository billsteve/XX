#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/10/12 16:04
import os

import XX.File.FileHelper as uf


class CommonHelper():
    @classmethod
    def get_spider_by_forum_id(cls, **kw):
        pass

    # 获取唯一URL
    @staticmethod
    def uniqueUrl(url):
        return url

    # 删除缓存文件
    @staticmethod
    def remove_cache_file(url, spider, root_path_cache, sc):
        url = CommonHelper.uniqueUrl(url)
        uf.FileHelper.remove_file(root_path_cache + spider + sc + uf.FileHelper.get_md_5_name(url) + ".cache")

    # 获取所有的spider名字
    @staticmethod
    def get_spiders(path, rp):
        spiders = []
        fns = uf.FileHelper.get_file_list(path)
        for fp, fn in fns:
            if fn.endswith("Spider.py"):
                for line in open(fp + os.sep + fn, encoding="utf-8"):
                    if line.strip().startswith("name ="):
                        spider = line.strip().split("=")[1].strip()
                        if spider.find("+") >= 0:
                            spider = eval(spider)
                        spiders.append(spider.strip("'").strip('"'))
        return spiders


class ResponseHelper:
    @staticmethod
    def check_response(response):
        if 400 <= response.status < 600:
            if response.status == 429 or response.status == 407 or response.status == 402:
                print("==Proxy error=== Status_code is " + str(response.status), flush=True)
            return False
        else:
            return True
