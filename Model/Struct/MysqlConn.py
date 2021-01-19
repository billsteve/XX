#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 13:50
# @Author   : Bill
# @Email      : billsteve@126.com
# @Des       : MySQL数据库连接配置对象
# @File        : Mysql
# @Software: PyCharm
import functools


def get_mysql_conn_cfg(**kw):
    d = dict()
    d["host"] = kw.get("host", "localhost")
    d["user"] = kw.get("user", "root")
    d["pwd"] = kw.get("pwd", "root")
    d["port"] = kw.get("port", 3306)
    d["charset"] = kw.get("charset", "utf-8")
    d["db"] = kw.get("db", "test")
    d["echo"] = kw.get("echo", False)
    return d


qq_cfg = functools.partial(get_mysql_conn_cfg, host="cd-cdb-f41yw26m.sql.tencentcdb.com", user="root", pwd="HBroot21", db="company", port=63626, echo=False, charset="utf-8")
ubuntu_cfg = functools.partial(get_mysql_conn_cfg, host="192.168.1.44", user="root", pwd="rebind1234", port=3306, db="car", echo=False, charset="utf-8")
baidu_mysql = functools.partial(get_mysql_conn_cfg, host="106.12.154.163", user="root", pwd="HBroot21", port=3306, db="tyc", echo=False, charset="utf-8")
local_mcf = functools.partial(get_mysql_conn_cfg, host="localhost", user="root", pwd="DRsXT5ZJ6Oi55LPQ", port=3306, db="net_scan", echo=False, charset="utf-8")
ali_cfg_tmp = functools.partial(get_mysql_conn_cfg, host="rm-8vbzabox9s9kvomq61o.mysql.zhangbei.rds.aliyuncs.com", user="root", pwd="HBroot21", port=3306, db="data_sheet", echo=False, charset="utf-8")
ali_zhihan_cfg = functools.partial(get_mysql_conn_cfg, host="39.104.97.69", user="root", pwd="rebind1234", port=3366, db="data_sheet", echo=False, charset="utf-8")
