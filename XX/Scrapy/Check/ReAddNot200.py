#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/22 10:16
# @File           : RecrawlNot200
# @Des           : 
# @Email        : billsteve@126.com
import time

import XX.Model.Struct.RedisConn as RC
import XX.Tools.BuiltinFunctions as BF
from XX.DB.RedisHelper import *
from logzero import logger


# @deprecated
def re_add_not200(rcfg=RC.ali2_cfg(db=0), ts=10):
    conn_redis = RedisHelper.get_redis_connect_by_cfg(rcfg)
    while 1:
        keys = conn_redis.keys("*not200*")
        if not keys:
            BF.print_from_head("No More not 200 Spider in " + str(rcfg["host"]), ts=ts)
            continue
        for key in keys:
            url = conn_redis.spop(key)
            if url:
                if conn_redis.sadd("s_not_200_urls", url):
                    logger.info("Readd url res is\t" + str(conn_redis.lpush(key[:-7], url)) + "\tkey is\t" + key[:-7] + "\t url is \t" + url)
                else:
                    print("Retry already!")
            else:
                logger.info("No url in set \t" + str(key))
            time.sleep(ts)
