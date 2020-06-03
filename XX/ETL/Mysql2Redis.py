#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/17 11:09
# @File           : Mysql2Redis
# @Des           : 
# @Email        : billsteve@126.com
# -*- coding:utf-8 -*-
import time
import traceback

import redis
from logzero import logger

import XX.DB.MysqlHelper as MH
import XX.DB.RedisHelper as  RH
import XX.File.FileHelper as FH


def get_key_type(key1):
    if key1.startswith("l"):
        key1Type = "list"
    elif key1.startswith("s"):
        key1Type = "set"
    elif key1.startswith("k"):
        key1Type = "kv"
    elif key1.startswith("z"):
        # TODO:
        key1Type = "zset"
    elif key1.startswith("h"):
        # TODO:
        key1Type = "hash"
    else:
        key1Type = None
    return key1Type


def get_key_value(key, r):
    keyType = get_key_type(key)
    try:
        if keyType == "list":
            return r.lpop(key)
        elif keyType == "set":
            return r.spop(key)
        elif keyType == "kv":
            return r.get(key)
        elif keyType == "zset":
            return r.zrange(key, 0, 1)
        elif keyType == "hash":
            return r.hget(key)
        else:
            return None
    except:
        return None


def set_key_value(key, val, r, *arg, **kw):
    keyType = get_key_type(key)
    try:
        if keyType == "list":
            return r.rpush(key, val)
        elif keyType == "set":
            return r.sadd(key, val)
        elif keyType == "kv":
            return r.set(key, val)
        elif keyType == "zset":
            if kw.get("score"):
                return r.zset(key, val, kw.get("score"))
            return
        elif keyType == "hash":
            return r.hset(key, val)
        else:
            print(" Not allowled keyType " + key)
            return None
    except:
        traceback.print_exc()
        return None
    pass


# DB 2 Redis
class Table2Redis():
    def __init__(self, *argvs, **kw):
        self.db = kw.get("mcfg", {}).get("db")
        self.ConnRedis = RH.RedisHelper.getRedisConnectByCfg(kw.get("rcfg"))
        self.ConnMysql = MH.MysqlHelper(**kw.get("mcfg"))

    # 把某一列加到redis中:
    # TODO: add zset hash other.......设计其他的类型
    def column_to_redis(
            self, table_name, column, key_name="",
            key_type="list",
            exists_set_name=None,
            from_0=False,
            del_key=False,
            del_exists_key=False,
            total=0, ts=0,
            key_filter=None,
            key_name_filter=None, *arg, **kw):
        from_id_key = "k_add_" + self.db + "_" + table_name + "_" + key_name + "_from_id"
        redis_from_id = self.ConnRedis.get(from_id_key) if self.ConnRedis.get(from_id_key) else 0
        from_id = 0 if from_0 else redis_from_id
        k_ADDREDIS_FROM_ID = from_id if from_id else 0
        print(" ==== FROM_ID is " + str(from_id))

        sql = "Select id," + column + " FROM " + table_name + " WHERE  ID > %s LIMIT 1000"
        keys = 1
        if del_key:
            self.ConnRedis.delete(key_name)
        if del_exists_key:
            self.ConnRedis.delete(exists_set_name)
        num = 0
        key_type = key_type if key_type else get_key_type(key_name)
        while keys:
            val = k_ADDREDIS_FROM_ID,
            keys = self.ConnMysql.get_lists(sql, val)
            for one_key in keys:
                key = list(one_key)
                if key_filter:
                    key[1] = key_filter(key[1], **kw)
                k_ADDREDIS_FROM_ID = key[0]
                if key[1]:
                    if key_name_filter:
                        KeyName = key_name_filter(KeyName=KeyName, key=key[1])
                    if ts and ts < 0.01:
                        if k_ADDREDIS_FROM_ID % int(1 / ts) == 0:
                            time.sleep(1)
                    else:
                        time.sleep(ts)
                    res = 0
                    if exists_set_name:
                        if self.ConnRedis.sismember(exists_set_name, key[1]):
                            print("EXITS >>> " + key[1] + "  from _id >>  " + str(key[0]))
                            continue
                    if key_type == "list":
                        if kw.get("limit"):
                            if int(self.ConnRedis.llen(key)) > kw["limit"]:
                                print("Too Much")
                                return
                        # 把某列添加到队列中
                        if len(key) == 2:
                            res = self.ConnRedis.rpush(KeyName, key[1])
                        # 某两列中的一列添加到队列中
                        elif len(key) == 3:
                            value = key[1] if key[1] else key[2]
                            res = self.ConnRedis.lpush(KeyName, value)
                        # 某三列中的一列添加到队列中
                        elif len(key) == 4:
                            value = key[1] if key[1] else key[2] if key[2] else key[3]
                            res = self.ConnRedis.lpush(KeyName, value)
                    elif key_type == "set":
                        if kw.get("limit"):
                            if int(self.ConnRedis.scard(key)) > kw["limit"]:
                                print("Too Much")
                                return
                        res = self.ConnRedis.sadd(KeyName, key[1])
                    elif key_type == "kv":
                        res = self.ConnRedis.set(key[1], key[2])
                    else:
                        logger.debug("????")
                    if res and exists_set_name:
                        self.ConnRedis.sadd(exists_set_name, key[1])
                    self.ConnRedis.set(from_id_key, k_ADDREDIS_FROM_ID)
                    print(kw.get("fn") + " add res :>> " + str(res) + "  now id :>> " + str(key[0]))
                    num += 1
                    if total and num >= total:
                        print(" Done --- ")
                        return
                else:
                    print("Error key" + str(key[1]))


# Redis 2 Redis
class Redis2Redis():
    def __init__(self, Host1="localhost", Host2="localhost", db1=0, db2=0, *arg, **kw):
        if not db2:
            db2 = db1
        self.r1 = redis.Redis(Host1, db=db1, decode_responses=True)
        self.r2 = redis.Redis(Host2, db=db2, decode_responses=True)

    def r1_2_r2(self, key1, key2, exists_set_name=None, total=0, key_filter=None, delete_source=True, ts=0, *arg, **kw):
        Total = total if not delete_source and total else total if delete_source else 1000
        val = 1
        num = 0
        while val:
            val = get_key_value(key1, self.r1)
            if key_filter:
                val = key_filter(val, *arg, **kw)
            if val:
                if exists_set_name:
                    if not self.r2.sadd(exists_set_name, val):
                        continue
                if set_key_value(key2, val, self.r2):
                    if not delete_source:
                        set_key_value(key1, val, self.r1)
                    print("ok")
                    num += 1
                    if Total and num >= Total:
                        break
                else:
                    print(" fail to add val.")


class Redis2File():

    def __init__(self, Host="localhost", db=0, *arg, **kw):
        self.r = redis.Redis(Host, db=db, decode_responses=True)

    def r_2_file(self, key, FilePath, ExistsSetName=None, Total=0, KeyFilter=None, DeleteSource=True, ts=0, LineEnd="", *arg, **kw):
        Total = Total if not DeleteSource and Total else Total if DeleteSource else 1000
        val = 1
        num = 0
        while val:
            val = get_key_value(key, self.r)
            val = KeyFilter(val, *arg, **kw) if KeyFilter else val
            try:
                if val:
                    if ExistsSetName:
                        if not self.r2.sadd(ExistsSetName, val):
                            continue
                    if FH.FileHelper.saveFile(FilePath, str(val)):
                        if not DeleteSource:
                            set_key_value(key, val, self.r)
                        print("ok  =  " + str(num))
                        num += 1
                        if Total and num >= Total:
                            break
                    else:
                        print(" fail to add val.")
                else:
                    print(" over ")
            except:
                set_key_value(key, val, self.r)
                traceback.print_exc()


if __name__ == "__main__":
    local = "localhost"
    pass
    # 把info 和 info12315的添加进去
    # redisHelper = AddRedisHelper(MYSQL_HOST13, MYSQL_USER13, MYSQL_PWD13, "gov", REDIS_HOST13, 9)
    # redisHelper.AddColumnToRedis("info12315", "REGNO", KeyName="l_123415_to_crawl_code", ExistsSetName="s_123415_crawled_code")
    # redisHelper.AddColumnToRedis("info", "REGNO", "l_123415_to_crawl_code", "s_123415_crawled_code")

    # 把qcc的号添加进去
    # redisHelper = AddRedisHelper(MYSQL_HOST13, MYSQL_USER13, MYSQL_PWD13, "qcc", REDIS_HOST13, 9)
    # redisHelper.AddColumnToRedis("com_info", "No,CreditCode", KeyName="l_123415_to_crawl_code", ExistsSetName="s_123415_crawled_code")

    # 吧info123添加到 已抓列表
    # redisHelper = AddRedisHelper(MYSQL_HOST13, MYSQL_USER13, MYSQL_PWD13, "gov", REDIS_HOST13, 9)
    # redisHelper.AddColumnToRedis("info", "REGNO", "s_123415_crawled_code", KeyType="set", From0=True)

    # qcc 添加
    # redisHelper = AddRedisHelper(
    #     MYSQL_HOST13, MYSQL_USER13, MYSQL_PWD13, "qcc", REDIS_HOST13, 9)
    # redisHelper.AddColumnToRedis(
    #     "com_info", "No,CreditCode", KeyName="s_123415_crawled_code", KeyType="set", From0=True)

    # r2r = Redis2RedisHelper(Host1=local, Host2=local, db1=1, db2=2)
    # r2r.R12R2("l_test", "l_test",ts=0.1,DeleteSource=False)

    # def addN(key):
    #     return str(key)+"\n" if key else key

    # r2f = Redis2FileHelper(local, 2)
    # r2f.R2File("l_test", "E:\\l_test.log", Total=100, KeyFilter=addN)
    import XX.Model.Struct.MysqlConn as MC
    import XX.Model.Struct.RedisConn as RC

    t2r = Table2Redis(mcfg=MC.qq_cfg(db="weibo"), rcfg=RC.ali_cfg(db=4))
    t2r.ColumnToRedis("weibo_info", "web_id", "s_crawled_wb_web_id", "set", limit=10, kv=False)
