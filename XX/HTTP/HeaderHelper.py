#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/10/11 20:14
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : HeaderHelper.py
# @Software : PyCharm
import user_agent


def create_random_ua(**kw):
    return user_agent.generate_user_agent(**kw)


def create_html_header(**kw):
    header = create_ajax_header(**kw)
    header["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    return header


def create_ajax_header(**kw):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": str(create_random_ua()),
    }
    return headers


def create_ajax_accept(header, **kw):
    header["Accept"] = "application/json, text/javascript, */*; q=0.01"
    return header


def create_img_header(header=None):
    if not header:
        header = create_ajax_header()
    header["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    return header


def create_host_header(host, **kw):
    headers = create_ajax_header(**kw)
    headers["Host"] = host
    return headers


def create_referer_header(referer, **kw):
    headers = create_ajax_header(**kw)
    headers["Referer"] = referer
    return headers


def create_host_referer_header(host, referer, **kw):
    headers = create_ajax_header(**kw)
    headers["Host"] = host
    headers["Referer"] = referer
    return headers


def get_header_from_line_str(headers):
    return {each.split(':', 1)[0].strip(): each.split(':', 1)[1].strip()
            for each in headers.split('\n') if each.split()}


if __name__ == '__main__':
    import time

    while 1:
        print(create_img_header((create_ajax_header())))
        time.sleep(0.8)
