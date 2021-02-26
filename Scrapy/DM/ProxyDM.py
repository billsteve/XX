#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import random

from logzero import logger
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from w3lib.http import basic_auth_header

import XX.DB.RedisHelper as Rh


# redisIP池代理
class IPPollingProxy:
    # ping from all province, then get cdn ip
    proxy_cdn = []

    # crawl everyday, then check them
    proxy_public = []

    # You must be allowed within the range of IP
    proxy_private = [
        'proxy.scrapy.com:23088',
    ]

    # all proxy pool
    proxy = proxy_public + proxy_private

    def process_request(self, request, spider):
        proxy_ip = random.choice(self.proxy)
        if proxy_ip:
            request.meta['proxy'] = "http://" + proxy_ip
        return


# 阿布云代理
class AbuyunProxy:

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_request(self, request, spider):
        # 代理服务器
        proxy_url = "http://http-dyn.abuyun.com:9020"
        code = bytes((self.settings.get("PROXY_UN") + ":" + self.settings.get("PROXY_PWD")), "ascii")
        proxyAuth = "Basic " + base64.urlsafe_b64encode(code).decode("utf8")
        request.meta["proxy"] = proxy_url
        request.headers["Proxy-Authorization"] = proxyAuth


# 固定IP代理
class IpProxy:

    def __init__(self):
        # 获取Redis连接
        pass

    def process_request(self, request, spider):
        #  这是ip用例，如果想要实时更新，就可以从DB中获取
        ips = ["49.85.6.229:39896", "49.85.6.229:39896", "49.85.6.229:39896"]
        ip = random.choice(ips)
        request.meta["proxy"] = ip


# Goubanjia代理
class GoubanjiaProxy:

    def __init__(self):
        # 获取Redis连接
        pass

    def process_request(self, request, spider):
        #  这是ip用例，如果想要实时更新，就可以从DB中获取
        ips = ["49.85.6.229:39896"]
        ip = random.choice(ips)
        request.meta["proxy"] = ip


class MimvpProxy:

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def __init__(self):
        self.conn_redis = Rh.RedisHelper.get_redis_connect(self.settings.get("REDIS_HOST"),
                                                           password=self.settings.get("REDIS_PWD"), db=9)

    def process_request(self, request, spider):
        ips = self.conn_redis.keys()
        if ips:
            request.meta["proxy"] = "http://c1259e45c76b:b7b9bd6b48@" + random.choice(ips)
            logger.info("Proxy is " + str(request.meta["proxy"]))
        else:
            logger.info("No Proxy ip")


# 快代理
class KuaiProxy:

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        return cls()

    def process_request(self, request, spider):
        request.meta['proxy'] = "http://%(proxy)s" % {'proxy': self.settings.get("PROXY_URL")}
        # 用户名密码认证 # 白名单认证可注释下一行
        request.headers['Proxy-Authorization'] = basic_auth_header(self.settings.get("PROXY_UN"), self.settings.get("PROXY_PWD"))
        # 这里是为了强制切换IP，因为隧道模式的IP有可能还能用
        request.headers["Connection"] = "close"
        return None


class Data5U(HttpProxyMiddleware):

    # 初始化
    def __init__(self, ip=''):
        super().__init__()
        self.ip = ip

    # 请求处理
    def process_request(self, request, spider):
        # 先随机选择一个IP
        IPPOOL = []
        thisip = random.choice(IPPOOL)
        print("当前使用IP是：" + thisip)
        request.meta["proxy"] = "http://" + thisip


class ProxyMiddleware:
    # scrapy暂不推荐使用，暂不提供技术支持

    # 代理服务器

    # appkey为你订单的key

    def process_request(self, request, spider):
        proxyServer = "transfer.moguproxy.com:9001"
        proxyAuth = "Basic " + ""
        request.meta["proxy"] = proxyServer

        request.headers["Authorization"] = proxyAuth
