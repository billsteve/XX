#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import random

from logzero import logger

import XX.DB.RedisHelper as Rh


class IPPollingProxy(object):
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
        # 验证代理用户名和密码
        # proxy_user_pass = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        # 根据国内国外ip确定启动哪一组代理池
        # ip发送到ping.chinaz.com查询地址
        # 根据地址来判断启动代理池
        # if u'国内' in area:
        #     request.meta['proxy'] = '这里设置国内http代理'
        # elif u'国外' in area:
        #     request.meta['proxy'] = '这里设置国外http代理'
        # else:
        #     pass
        return


class AbuyunProxy(object):

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


class IpProxy(object):

    def __init__(self):
        # 获取Redis连接
        pass

    def process_request(self, request, spider):
        #  这是ip用例，如果想要实时更新，就可以从DB中获取
        ips = ["49.85.6.229:39896", "49.85.6.229:39896", "49.85.6.229:39896"]
        ip = random.choice(ips)
        request.meta["proxy"] = ip


# Goubanjia代理
class Goubanjia(object):

    def __init__(self):
        # 获取Redis连接
        pass

    def process_request(self, request, spider):
        #  这是ip用例，如果想要实时更新，就可以从DB中获取
        ips = ["49.85.6.229:39896"]
        ip = random.choice(ips)
        request.meta["proxy"] = ip


class MimvpProxy(object):

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
