#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/7/8 22:44
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : data.py
# @Software : PyCharm
import time

import XX.Encrypt.EncryptHelper as cenc


# 服务端生成的response json结构封装
class CrawlerUrl(object):
    url = None
    url_md5 = None
    spider = None
    post_data = None
    url_type = None
    source_url_id = None
    cookie = None
    data_type = None
    resp_status = None
    retry_num = None
    has_next_page = None
    except_type = None
    except_msg = None
    crawled_item = None
    other = None
    id_del = None
    update_ts = None
    create_ts = None

    def __init__(self, *arg, **kw):
        self.url = kw.get("url")
        self.url_md5 = cenc.Encrypt.md5(self.url)
        self.spider = kw.get("spider")
        self.post_data = kw.get("post_data")
        self.url_type = kw.get("url_type")
        self.source_url_id = kw.get("source_url_id")
        self.cookie = kw.get("cookie")
        self.data_type = kw.get("data_type")
        self.resp_status = kw.get("resp_status")
        self.retry_num = kw.get("retry_num")
        self.has_next_page = kw.get("has_next_page")
        self.except_type = kw.get("except_type")
        self.except_msg = kw.get("except_msg")
        self.crawled_item = kw.get("crawled_item")
        self.other = kw.get("other")
        self.id_del = kw.get("id_del")
        self.update_ts = kw.get("update_ts")
        self.create_ts = kw.get("create_ts")

    @staticmethod
    def save_2_mysql(self, data):
        ts = int(time.time())
        val = data.get("url"), data.get("url_md5"), data.get("post_data"), data.get("url_type"), data.get(
            "source_url_id"), data.get("cookie"), data.get("data_type"), data.get("resp_status"), data.get(
            "retry_num"), data.get("has_next_page"), data.get("id_del"), data.get("except_type"), data.get(
            "except_msg"), 0, data.get("update_ts", ), data.get("create_ts"), ts, ts
        sql = "INSERT INTO data values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return sql, val


if __name__ == "__main__":
    res = CrawlerUrl(url_type=0, url="baidu.com")
    import json

    print(json.dumps(res.__dict__))
    pass
