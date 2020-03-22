#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/3 13:24
# @Email     : billsteve@126.com
# @Des       : 添加入口URL
# @File        : InitUrl
# @Software: PyCharm
import importlib
import json
import time

import XX.DB.RedisHelper as ur
import XX.DB.SqlAlchemyHelper as sa
import XX.Tools.BloomFilter as BloomFilter
import XX.Tools.BuiltinFunctions as BF
from XX.DB.RedisHelper import *
from logzero import logger


# 添加入库url
class AddInitUrl:

    def __init__(self):
        self.spider = None
        self.url = None
        self.conn_redis = None

    def add(self, **kwargs):
        return self.conn_redis.lpush(self.spider + kwargs.get("suffix", ":start_urls"), self.url)

    # url2redis
    @staticmethod
    def add_url2redis(spider, url, conn_redis, **kwargs):
        return conn_redis.lpush(spider + kwargs.get("suffix", ":start_urls"), url)

    # URL到rcfg
    @staticmethod
    def add_url2rediscfg(spider, url, cfg, **kwargs):
        conn_redis = ur.RedisHelper.get_redis_connect_by_cfg(cfg)
        return conn_redis.lpush(spider + kwargs.get("suffix", ":start_urls"), url)

    # 把数据库中的某一列添加到某个队列中，并且值作为url_fun的参数，添加的是返回值
    @staticmethod
    def add_table_column2redis(pro_num, *args, column=None, url_fun=None, process_num=10, fn="", spider="", module_name="",
                               class_name=None, r_cfg=None, m_cfg=None, service=True, from_id=None, limit=3000, **kwargs):
        session = sa.SqlAlchemyHelper.get_session_by_cfg(m_cfg)
        conn_redis = ur.RedisHelper.get_redis_connect_by_cfg(r_cfg)
        if kwargs.get("del_q"):
            conn_redis.delete(spider + kwargs.get("suffix", ":start_urls"))
        if from_id is None:
            from_id = conn_redis.get("kid_" + str(fn) + "_" + class_name + "_" + str(pro_num) + "_from_id")
            from_id = from_id if from_id else 0
            logger.info("From id is \t" + str(from_id))

        while 1:
            if conn_redis.llen(spider + kwargs.get("suffix", ":start_urls")) > limit:
                BF.print_from_head("===Too much\t" + class_name + "\t")
                time.sleep(2 * (pro_num + 1))
                continue
            model_class = getattr(importlib.import_module(module_name), class_name)
            infos = model_class.getByFromIdAndMod(from_id, process_num, pro_num, session, limit=10)
            if infos:
                for info in infos:
                    if url_fun:
                        url = url_fun(info.__dict__.get(column))
                    else:
                        url = info.__dict__.get(column)
                    if url:
                        url = url.strip()
                        if kwargs.get("bf"):
                            bloomFilter = BloomFilter.BloomFilter(conn_redis, key=spider)
                            if bloomFilter.is_exists(url):
                                BF.print_no_end("-")
                            else:
                                res = conn_redis.lpush(spider + kwargs.get("suffix", ":start_urls"), url)
                                logger.info(str((spider, res, info.id, url)))
                                bloomFilter.add(url)
                        else:
                            res = conn_redis.lpush(spider + kwargs.get("suffix", ":start_urls"), url)
                            logger.info(str((spider, res, info.id, url)))

                    from_id = info.id
                    conn_redis.set("kid_" + str(fn) + "_" + class_name + "_" + str(pro_num) + "_from_id", from_id)
            else:
                if service:
                    BF.print_from_head("No More\t" + class_name + "\t")
                    time.sleep(2 * (pro_num + 1))
                    session.commit()
                else:
                    return

    # 文件到队列
    @staticmethod
    def add_file2redis(spider, fp, conn_redis, line_func=None):
        for url in open(fp, encoding="utf-8"):
            if line_func:
                url = line_func(url)
            AddInitUrl.add_url2redis(spider, url, conn_redis)

    # 添加check url
    @staticmethod
    def addCheckUrl(project, url, spider, conn, suffix=":start_urls:check"):
        d = dict()
        d["url"] = url
        d["project"] = project
        d["spider"] = spider
        url = json.dumps(d, ensure_ascii=False)
        return conn.lpush(spider + suffix, url)

    # 把check的URL添加到IU中
    @staticmethod
    def addInitUrlFromCheck(hcfg, rcfg, getRow, ts=0):
        import XX.DB.HappyBaseHelper as HaB

        conn_redis = RedisHelper.get_redis_connect_by_cfg(rcfg)
        conn_hbase = HaB.HappyBaseHeleper.get_connection_by_cfg(hcfg)
        # pool = HaB.HappyBaseHeleper.getPoolByCfg(hcfg)
        while 1:
            keys = conn_redis.keys("*:start_urls:check")
            if not keys:
                BF.print_from_head("No More Check IU in " + str(rcfg["host"]), ts=ts)
                continue
            for key in keys:
                jd = json.loads(conn_redis.lpop(key))
                url = jd["url"]
                if url:
                    # table = HaB.HappyBaseHeleper.getTable("crawl_" + jd["project"], pool=pool)
                    table = HaB.HappyBaseHeleper.get_table("crawl_" + jd["project"], conn=conn_hbase)
                    # HBase是否存在
                    row = getRow(url=url)
                    if row:
                        exists = HaB.HappyBaseHeleper.get_row(row)
                        if not exists:
                            res = conn_redis.lpush(key[:-6], url)
                            print("Add new IU res \t\t" + str(res))
                        else:
                            print("Already Crawled!\t\t" + url)
                    else:
                        print("==== No row key", jd)
                time.sleep(ts)

    # 重新添加不是200的url到Check
    @staticmethod
    def readdNot200(rcfg, ts=10, suffix=":init_urls"):
        conn_redis = RedisHelper.get_redis_connect_by_cfg(rcfg)
        while 1:
            keys = conn_redis.keys("*not200*")
            if not keys:
                BF.print_from_head("No More Spider in " + str(rcfg["host"]), ts=ts)
                continue
            for key in keys:
                url = conn_redis.spop(key)
                if url:
                    if conn_redis.sadd("s_not_200_urls", url):
                        logger.info("Readd url res is\t" + str(conn_redis.lpush(key.split(":")[0] + suffix, url)) + "\tkey is\t" + key[:-7] + "\t url is \t" + url)
                    else:
                        print("Retry already!")
                else:
                    logger.info("No url in set \t" + str(key))
                time.sleep(ts)
