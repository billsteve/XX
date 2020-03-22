#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/17 10:51
# @Email     : billsteve@126.com
# @Des       : 
# @File        : HeadersDM
# @Software: PyCharm
import random


class Header(object):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.2.2457.400",
    }

    def process_request(self, request, spider):
        request.headers.setdefault('Accept', self.headers["Accept"])
        request.headers.setdefault('Accept-Encoding', self.headers["Accept-Encoding"])
        request.headers.setdefault('Accept-Language', self.headers["Accept-Language"])
        request.headers.setdefault('Upgrade-Insecure-Requests', self.headers["Upgrade-Insecure-Requests"])
        request.headers.setdefault('User-Agent', self.headers["User-Agent"])


class RandomUserAgentPc(object):

    def process_request(self, request, spider):
        import user_agent
        ua = user_agent.generate_user_agent(os="win", device_type=["desktop"])
        request.headers.setdefault('User-Agent', ua)


class RandomUserAgent_mobile(object):

    def process_request(self, request, spider):
        import user_agent
        ua = user_agent.generate_user_agent(os="win", device_type=["smartphone"])
        request.headers.setdefault('User-Agent', ua)


class RandomUserAgent_weixin(object):
    userAgents = {
        'weixin': [
            # weixin pc for windows
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat'
        ]
    }

    def process_request(self, request, spider):
        user_agent = random.choice(self.userAgents['weixin'])
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
        return


class HeaderAcceptAll(object):
    def process_request(self, request, spider):
        request.headers.setdefault('Accept', "*/*")


class HeaderAcceptJson(object):

    def process_request(self, request, spider):
        request.headers.setdefault('Accept', "application/json, text/javascript, */*; q=0.01")
        request.headers.setdefault("X-Requested-With", "XMLHttpRequest")


class HeaderAcceptImg(object):

    def process_request(self, request, spider):
        request.headers.setdefault('Accept', "image/webp,image/apng,image/*,*/*;q=0.8")


class HeaderAcceptHtml(object):

    def process_request(self, request, spider):
        request.headers.setdefault('Accept', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")


class AutoHomeHeader(object):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400",
        "x-requested-with": "XMLHttpRequest"
    }

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.headers["User-Agent"])
