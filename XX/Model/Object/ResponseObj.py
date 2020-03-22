# -*- coding:utf-8 -*-
from scrapy.http import Response as ScrapyResponse


# 请求服务端，返回的response
class ResponseObj(ScrapyResponse):
    url = None
    status = None
    status_code = None
    # 默认是返回header
    headers = {}
    ResponseHeaders = {}
    RequestHeaders = {}
    content = None
    text = ""
    method = None
    msg = ""
    cache = 0
    cache_file = None
    data = {}
    cookies = {}
    encoding = "UTF-8"
    errback = None
    callback = None

    def __init__(self, *arg, **kw):
        for k, v in kw.items():
            setattr(self, k, v)
        self.url = kw.get("url")
        self.status = kw.get("status")
        self.status_code = kw.get("status_code")
        self.headers = kw.get("headers")
        self.ResponseHeaders = kw.get("ResponseHeaders")
        self.RequestHeaders = kw.get("RequestHeaders")
        self.content = kw.get("content")
        self.text = kw.get("text")
        self.method = kw.get("method")
        self.msg = kw.get("msg")
        self.cache = kw.get("cache")
        self.cache_file = kw.get("cache_file")
        self.data = kw.get("data")
        self.cookies = kw.get("cookies")
        self.encoding = kw.get("encoding")
        self.errback = kw.get("errback")
        self.callback = kw.get("callback")


if __name__ == "__main__":
    a = ResponseObj(a=1)
    print(a.a)
