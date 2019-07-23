#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/10/11 20:14
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : HeaderHelper.py
# @Software : PyCharm
import user_agent


def getRandomUA(**kw):
    return user_agent.generate_user_agent(**kw)


def getHtmlHeader(**kw):
    header = getAjaxHeader(**kw)
    header["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    return header


def getAjaxHeader(**kw):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": str(getRandomUA()),
    }
    return headers


def getAjaxAccept(header, **kw):
    header["Accept"] = "application/json, text/javascript, */*; q=0.01"
    return header


def getImgHeader(header=None):
    if not header:
        header = getAjaxHeader()
    header["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    return header


def getHostHeader(host, **kw):
    headers = getAjaxHeader(**kw)
    headers["Host"] = host
    return headers


def getRefererHeader(referer, **kw):
    headers = getAjaxHeader(**kw)
    headers["Referer"] = referer
    return headers


def getHostRefererHeader(host, referer, **kw):
    headers = getAjaxHeader(**kw)
    headers["Host"] = host
    headers["Referer"] = referer
    return headers


if __name__ == '__main__':
    import time

    while 1:
        print(getImgHeader((getAjaxHeader())))
        time.sleep(0.8)
