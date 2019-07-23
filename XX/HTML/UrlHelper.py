#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 18:11
# @Author   : Peter
# @Des       : 
# @File        : UrlHelper
# @Software: PyCharm
import urllib.parse as parse

import XX.Dict.DictHelper as hdict
import XX.RegExp.RegExp as RE
from tld import parse_tld, get_tld


class UrlHelper():

    # 检验是否是一个合法URL
    @staticmethod
    def checkUrl(url):
        if RE.RegExpHelper.isUrl(url):
            return 1

    # 是否有参数列表
    @staticmethod
    def hasParams(url):
        return

    # 获取域名
    @staticmethod
    def getDomain(url):
        url = UrlHelper.addSchema(url)
        try:
            from tld import get_tld
            res = get_tld(url, as_object=True)
            return res.fld
        except Exception as e:
            raise e

    # 获取协议
    @staticmethod
    def getProtocol(url):
        protocol = url.split(":")[0]
        if protocol.startswith("http"):
            return protocol

    # 删除参数:保留协议和基本网址
    @staticmethod
    def getWithoutParams(url):
        if not url:
            return ""
        url = url.split(UrlHelper.getDomain(url))[0] + UrlHelper.getDomain(url)
        return url if not url.endswith("/") else url[:-1]
        # return url.split("#")[0].split("?")[0]

    # 获取参数列表
    @staticmethod
    def getParams(url):
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
    def setParams(url, params):
        if not str(url).endswith("?"):
            url = url + "?"
        for k, v in dict(params).items():
            url = url + "&" + str(k) + "=" + str(v)
        url = str(url).replace("?&", "?")
        return url

    # 添加参数
    @staticmethod
    def addParams(url, d):
        params = UrlHelper.getParams(url.split("#")[0])
        main_url = UrlHelper.getWithoutParams(url)
        params = dict(params, **d)
        d = hdict.DictHelper.sortedDictKey(params)
        params_str = ""
        for k, v in d.items():
            params_str += "&" + str(k) + "=" + str(v)
        return main_url + "?" + params_str.lstrip("&")

    @staticmethod
    def urlDecode(k):
        return parse.unquote(str(k))

    @staticmethod
    def urlEncode(k):
        return parse.quote(str(k))

    @staticmethod
    def parseDict(item):
        for k in item:
            if isinstance(item[k], str):
                item[k] = UrlHelper.urlDecode(item[k])
            elif isinstance(item[k], dict):
                item[k] = UrlHelper.parseDict(item[k])
        return item

    # 从url中获取参数列表
    @staticmethod
    def formatUrlToDict(url):
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
    def getUrlLevel(url):
        url = UrlHelper.addSchema(url)
        if parse_tld(url)[2] == "" or parse_tld(url)[2] == "www":
            return 1
        elif parse_tld(url)[2]:
            return 2
        else:
            return 0

    @staticmethod
    def getTopLevelUrl(url):
        lurl = parse_tld(UrlHelper.addSchema(url))
        return lurl[1] + "." + lurl[0]

    # 域名的所有部分
    @staticmethod
    def getMainUrl(url):
        url = UrlHelper.getAbsoluteUrl(url)
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
    def getScheme(url):
        return get_tld(url, as_object=True).parsed_url.scheme

    @staticmethod
    def getAbsoluteUrl(url, main_url=""):
        if url.startswith("#") or url.find("javascript") >= 0 or url.startswith("mailto"):
            return ""
        if url.startswith("/"):
            url = main_url + url
        if not url.startswith("http") or url.startswith("//"):
            url = "https://" + str(url).lstrip("//")
        return url

    @staticmethod
    def getRelativelUrl(url_source, url_new):
        if UrlHelper.getAbsoluteUrl(url_new, url_source):
            return parse.urljoin(url_source, url_new)

    @staticmethod
    def addSchema(url, schema="http://"):
        return url if url.startswith("http://") or url.startswith("https://") else "http://" + url


if __name__ == "__main__":
    url = "https://www.intel.cn/content/www/cn/zh/communications/sds-ubs-coho-data-case-study.html"
    print(UrlHelper.getWithoutParams(url))
    # print(url.split(UrlHelper.getDomain(url))[0]+UrlHelper.getDomain(url))
    exit()
    url = "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D3%26q%3D%E6%9C%AC%E7%94%B0%26t%3D0&page_type=searchall&page=1"
    url = "http://db.auto.sina.com.cn/2701"
    domain = UrlHelper.getMainUrl(url)
    domain = ".".join(domain.split(".")[::-1])
    print(domain)
    exit()
    import pprint

    url = "https://w2.www1.sxmty.com"
    print(UrlHelper.getMainUrl(url))
    exit()
    p = UrlHelper.getParams(url)
    print(p)
    exit()
    p["f"] = "8888"
    pprint.pprint(UrlHelper.setParams("https://www.baidu.com/s", p))
    # url = str(url).strip("http://").strip("https://").split("/")[0]
    # print(url.strip("/"))
    # print(UrlHelper.getScheme(url) + "://" + UrlHelper.getMainUrl(url))
