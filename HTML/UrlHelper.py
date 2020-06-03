#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse as parse
from urllib.parse import urlparse

import XX.Dict.DictHelper as h_dict
import XX.RegExp.RegExp as Re
from tld import parse_tld, get_tld


class UrlHelper():

    # 检验是否是一个合法URL
    @staticmethod
    def check_url(url):
        if Re.RegExpHelper.is_url(url):
            return 1

    @staticmethod
    def check_domain(url):
        if Re.RegExpHelper.is_domain(url):
            return 1

    # 是否有参数列表
    @staticmethod
    def has_params(url):
        return

    # 获取域名
    @staticmethod
    def get_domain(url):
        url = UrlHelper.add_schema(url)
        return urlparse(url).hostname

    # 获取协议
    @staticmethod
    def get_protocol(url):
        protocol = url.split(":")[0]
        if protocol.startswith("http"):
            return protocol

    # 删除参数:保留协议和基本网址
    @staticmethod
    def get_without_params(url):
        if not url:
            return ""
        url = url.split(UrlHelper.get_domain(url))[0] + UrlHelper.get_domain(url)
        return url if not url.endswith("/") else url[:-1]
        # return url.split("#")[0].split("?")[0]

    # 获取参数列表
    @staticmethod
    def get_params(url):
        res = {}
        try:
            values = url.split('?')[-1]
            for key_value in values.split('&'):
                try:
                    res[key_value.split('=')[0]] = key_value.split('=')[1]
                except:
                    pass
            return res
        except:
            print(" === URL: " + str(url))
            return {}

    # 添加参数
    @staticmethod
    def set_params(url, params):
        if not str(url).endswith("?"):
            url = url + "?"
        for k, v in dict(params).items():
            url = url + "&" + str(k) + "=" + str(v)
        url = str(url).replace("?&", "?")
        return url

    # 添加参数
    @staticmethod
    def add_params(url, d):
        params = UrlHelper.get_params(url.split("#")[0])
        main_url = UrlHelper.get_without_params(url)
        params = dict(params, **d)
        d = h_dict.DictHelper.sortedDictKey(params)
        params_str = ""
        for k, v in d.items():
            params_str += "&" + str(k) + "=" + str(v)
        return main_url + "?" + params_str.lstrip("&")

    # url解码
    @staticmethod
    def url_decode(k):
        return parse.unquote(str(k))

    # URL编码
    @staticmethod
    def url_encode(k):
        return parse.quote(str(k))

    # 解析dict
    @staticmethod
    def parse_dict(item):
        for k in item:
            if isinstance(item[k], str):
                item[k] = UrlHelper.url_decode(item[k])
            elif isinstance(item[k], dict):
                item[k] = UrlHelper.parse_dict(item[k])
        return item

    # 从url中获取参数列表
    @staticmethod
    def format_url_to_dict(url):
        res = {}
        try:
            values = url.split('?')[-1]
            for key_value in values.split('&'):
                try:
                    res[key_value.split('=')[0]] = key_value.split('=')[1]
                except:
                    pass
            return res
        except Exception as e:
            raise e

    # 获取域名属于几级域名
    @staticmethod
    def get_url_level(url):
        url = UrlHelper.add_schema(url)
        if parse_tld(url)[2] == "" or parse_tld(url)[2] == "www":
            return 1
        elif parse_tld(url)[2]:
            return 2
        else:
            return 0

    @staticmethod
    def get_top_level_url(url):
        lurl = parse_tld(UrlHelper.add_schema(url))
        return lurl[1] + "." + lurl[0]

    # 域名的所有部分
    @staticmethod
    def get_main_url(url):
        url = UrlHelper.get_absolute_url(url)
        if url:
            lurl = parse_tld(url)
            if lurl[2] and len(lurl[2]):
                if lurl[2] == "www":
                    return lurl[1] + "." + lurl[0]
                else:
                    return lurl[2] + "." + lurl[1] + "." + lurl[0]
            elif lurl[1] and len(lurl[1]):
                return lurl[1] + "." + lurl[0]
            else:
                return lurl[0]

    @staticmethod
    def get_scheme(url):
        return get_tld(url, as_object=True).parsed_url.scheme

    @staticmethod
    def get_absolute_url(url, main_url=""):
        if url.startswith("#") or url.find("javascript") >= 0 or url.startswith("mailto"):
            return ""
        if url.startswith("/"):
            url = main_url + url
        if not url.startswith("http") or url.startswith("//"):
            url = "https://" + str(url).lstrip("//")
        return url

    @staticmethod
    def get_relative_url(url_source, url_new):
        if UrlHelper.get_absolute_url(url_new, url_source):
            return parse.urljoin(url_source, url_new)

    @staticmethod
    def add_schema(url, schema="http://"):
        return url if url.startswith("http://") or url.startswith("https://") else "http://" + url


if __name__ == '__main__':
    u = UrlHelper()
    d = u.get_domain("http://localjhost.com:9100/")
    print(d)
