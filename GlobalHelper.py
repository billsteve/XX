#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time        : 2018/7/7 2:01
# @Email       : billsteve@126.com
# @File          : GlobalHelper.py
# @Software  : PyCharm
import time
import XX.DB.RedisHelper as credis
import XX.String.StringHelper as cstr


# 全局暂停功能
def global_sleep(ts=0, redis_conn=None, **kw):
    if not redis_conn:
        redis_conn = credis.RedisHelper.get_redis_connect(host=kw.get("redis_host", "localhost"))
    if not ts:
        ts = cstr.str2int(redis_conn.get("k_global_ts"))
        ts = ts if ts else 0
    time.sleep(ts)
