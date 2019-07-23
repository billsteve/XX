#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 13:50
# @Author   : Bill
# @Email      : billsteve@126.com
# @Des       : Redis的配置参数
# @File        : Redis
# @Software: PyCharm
import functools


def get_redis_conn_cfg(**kw):
    d = dict()
    d["host"] = kw.get("host", "localhost")
    d["pwd"] = kw.get("pwd", None)
    d["port"] = kw.get("port", 6379)
    d["db"] = kw.get("db", 0)
    d["decode_responses"] = kw.get("decode_responses", True)
    return d


ali_cfg = functools.partial(get_redis_conn_cfg, host="39.104.97.69", pwd="DRsXT5ZJ6Oi55LPQ", db=0)
ali2_cfg = functools.partial(get_redis_conn_cfg, host="39.104.57.130", pwd="DRsXT5ZJ6Oi55LPQ", db=0)
ubuntu_cfg = functools.partial(get_redis_conn_cfg, host="192.168.1.44", db=0)
local = functools.partial(get_redis_conn_cfg, host="localhost", db=0)
zhihan00 = functools.partial(get_redis_conn_cfg, host="zhihan00", db=0)
