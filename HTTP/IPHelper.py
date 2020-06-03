#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/17 11:47
# @Email     : billsteve@126.com
# @Des       : 
# @File        : IPHelper
# @Software: PyCharm
import socket


def getUrlIpList(domain):  # 获取域名解析出的IP列表
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_list.append(item[4][0])
    except Exception as e:
        pass
    return ip_list


if __name__ == '__main__':
    ips = getUrlIpList("www.zgjsks.com")
    print(ips)
