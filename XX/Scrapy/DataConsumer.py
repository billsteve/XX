# -*- coding:utf-8 -*-
# 2018/12/2 16:26
import importlib
import json
import time

import XX.DB.SqlAlchemyHelper as sa
import XX.DB.RedisHelper as udr
import XX.Tools.BuiltinFunctions as bf
import XX.Threading.AsyncHelper as ah


class IDataCustomer:

    def customer(self, **kw):
        pass


class MQ2DB(IDataCustomer):

    def customer(self, **kw):
        pass

    @staticmethod
    def redis2mysql(*arg, **kw):
        pass

    @staticmethod
    def save2db(json_data, spider, mcfg):
        module = importlib.import_module("SpiderJson2DB")
        func = getattr(module, spider)
        if func:
            return func(json_data, mcfg, spider)
        else:
            print("No " + str(spider) + "'s  save 2 db")


class Redis2Mysql(MQ2DB):

    # 初始化redis和MySQL连接类
    def __init__(self, **kw):
        self.conn_redis = udr.RedisHelper.get_redis_connect_by_cfg(kw.get("rcfg"))
        self.conn_mysql = sa.SqlAlchemyHelper.get_session_by_cfg(kw.get("mcfg"))

    # def customer(self, **kw):
    #     self.redis2mysql(**kw)

    @ah.async_call
    def redis2mysql(self, **kw):
        while 1:
            spider = kw.get("spider")
            json_str = self.conn_redis.lpop(spider + ":items")
            if kw.get("debug"):
                # 放回
                self.conn_redis.lpush(spider + ":items", json_str)
            if json_str:
                json_data = json.loads(json_str, encoding="utf-8")
                func = kw.get("func")
                # func(json_data, kw.get("mcfg"))
                func(json_data, self.conn_mysql)
            else:
                bf.print_no_end(spider + "\tNo more item")
                time.sleep(kw.get("ts", 5))
                if kw.get("once"):
                    print("One circle over")
                    break


#
def redis2mysql(**kw):
    conn_redis = udr.RedisHelper.get_redis_connect_by_cfg(kw.get("rcfg"))
    conn_mysql = sa.SqlAlchemyHelper.get_session_by_cfg(kw.get("mcfg"))
    while 1:
        spider = kw.get("spider")
        json_str = conn_redis.rpop(spider + ":items")
        if kw.get("debug"):
            # 放回
            print("+++>>> Readd=====")
            conn_redis.lpush(spider + ":items", json_str)
        if json_str:
            json_data = json.loads(json_str, encoding="utf-8")
            func = kw.get("func")
            func(json_data, conn_mysql)
            conn_mysql.commit()
        else:
            # bf.printFromHead(spider + "\tNo more item")
            bf.print_from_head(spider + "\tNo more item \t")
            time.sleep(kw.get("ts", 5))
            if kw.get("once"):
                print("One circle over")
                break
