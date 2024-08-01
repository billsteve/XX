#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 13:50
# @Author   : Bill
# @Email    : billsteve@126.com
# @Des      : MySQL数据库连接配置对象
# @File     : Mysql
# @Software: PyCharm
import functools


def get_mysql_conn_cfg(**kw):
    d = dict()
    d["host"] = kw.get("host", "localhost")
    d["user"] = kw.get("user", "root")
    d["password"] = kw.get("password", "root")
    d["port"] = kw.get("port", 3306)
    d["charset"] = kw.get("charset", "utf-8")
    d["db"] = kw.get("db", "test")
    d["echo"] = kw.get("echo", False)
    return d


local_mcf = functools.partial(get_mysql_conn_cfg, host="localhost", user="root", password="DRsXT5ZJ6Oi55LPQ", port=3306, db="net_scan", echo=False, charset="utf-8")
