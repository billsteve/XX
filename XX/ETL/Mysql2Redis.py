#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/17 11:09
# @File           : Mysql2Redis
# @Des           : 
# @Email        : billsteve@126.com
# -*- coding:utf-8 -*-
import time
import traceback

import XX.DB.MysqlHelper as MH
import XX.DB.RedisHelper as  RH
import XX.File.FileHelper as FH
import redis
from logzero import logger


def getKeyType(key1):
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


def getKeyValue(key, r):
    keyType = getKeyType(key)
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


def setKeyValue(key, val, r, *arg, **kw):
    keyType = getKeyType(key)
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
    def ColumnToRedis(self, TableName, Column, KeyName="", KeyType="list", ExistsSetName=None, From0=False, DelKey=False, DelExistsKey=False, Total=0, ts=0, KeyFilter=None, KeyNameFilter=None, *arg, **kw):
        from_id_key = "k_add_" + self.db + "_" + TableName + "_" + KeyName + "_from_id"
        redis_from_id = self.ConnRedis.get(from_id_key) if self.ConnRedis.get(from_id_key) else 0
        from_id = 0 if From0 else redis_from_id
        k_ADDREDIS_FROM_ID = from_id if from_id else 0
        print(" ==== FROM_ID is " + str(from_id))

        sql = "Select id," + Column + " FROM " + TableName + " WHERE  ID > %s LIMIT 1000"
        keys = 1
        if DelKey:
            self.ConnRedis.delete(KeyName)
        if DelExistsKey:
            self.ConnRedis.delete(ExistsSetName)
        num = 0
        KeyType = KeyType if KeyType else getKeyType(KeyName)
        while keys:
            val = k_ADDREDIS_FROM_ID,
            keys = self.ConnMysql.getLists(sql, val)
            for one_key in keys:
                key = list(one_key)
                if KeyFilter:
                    key[1] = KeyFilter(key[1], **kw)
                k_ADDREDIS_FROM_ID = key[0]
                if key[1]:
                    if KeyNameFilter:
                        KeyName = KeyNameFilter(KeyName=KeyName, key=key[1])
                    if ts and ts < 0.01:
                        if k_ADDREDIS_FROM_ID % int(1 / ts) == 0:
                            time.sleep(1)
                    else:
                        time.sleep(ts)
                    res = 0
                    if ExistsSetName:
                        if self.ConnRedis.sismember(ExistsSetName, key[1]):
                            print("EXITS >>> " + key[1] + "  from _id >>  " + str(key[0]))
                            continue
                    if KeyType == "list":
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
                    elif KeyType == "set":
                        if kw.get("limit"):
                            if int(self.ConnRedis.scard(key)) > kw["limit"]:
                                print("Too Much")
                                return
                        res = self.ConnRedis.sadd(KeyName, key[1])
                    elif KeyType == "kv":
                        res = self.ConnRedis.set(key[1], key[2])
                    else:
                        logger.debug("????")
                    if res and ExistsSetName:
                        self.ConnRedis.sadd(ExistsSetName, key[1])
                    self.ConnRedis.set(from_id_key, k_ADDREDIS_FROM_ID)
                    print(kw.get("fn") + " add res :>> " + str(res) + "  now id :>> " + str(key[0]))
                    num += 1
                    if Total and num >= Total:
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

    def R12R2(self, key1, key2, ExistsSetName=None, Total=0, KeyFilter=None, DeleteSource=True, ts=0, *arg, **kw):
        Total = Total if not DeleteSource and Total else Total if DeleteSource else 1000
        val = 1
        num = 0
        while val:
            val = getKeyValue(key1, self.r1)
            if KeyFilter:
                val = KeyFilter(val, *arg, **kw)
            if val:
                if ExistsSetName:
                    if not self.r2.sadd(ExistsSetName, val):
                        continue
                if setKeyValue(key2, val, self.r2):
                    if not DeleteSource:
                        setKeyValue(key1, val, self.r1)
                    print("ok")
                    num += 1
                    if Total and num >= Total:
                        break
                else:
                    print(" fail to add val.")


class Redis2File():

    def __init__(self, Host="localhost", db=0, *arg, **kw):
        self.r = redis.Redis(Host, db=db, decode_responses=True)

    def R2File(self, key, FilePath, ExistsSetName=None, Total=0, KeyFilter=None, DeleteSource=True, ts=0, LineEnd="", *arg, **kw):
        Total = Total if not DeleteSource and Total else Total if DeleteSource else 1000
        val = 1
        num = 0
        while val:
            val = getKeyValue(key, self.r)
            val = KeyFilter(val, *arg, **kw) if KeyFilter else val
            try:
                if val:
                    if ExistsSetName:
                        if not self.r2.sadd(ExistsSetName, val):
                            continue
                    if FH.FileHelper.saveFile(FilePath, str(val)):
                        if not DeleteSource:
                            setKeyValue(key, val, self.r)
                        print("ok  =  " + str(num))
                        num += 1
                        if Total and num >= Total:
                            break
                    else:
                        print(" fail to add val.")
                else:
                    print(" over ")
            except:
                setKeyValue(key, val, self.r)
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
    # r2f.R2File("l_test", "E:\\l_test.txt", Total=100, KeyFilter=addN)
    import XX.Model.Struct.MysqlConn as MC
    import XX.Model.Struct.RedisConn as RC

    t2r = Table2Redis(mcfg=MC.qq_cfg(db="weibo"), rcfg=RC.ali_cfg(db=4))
    t2r.ColumnToRedis("weibo_info", "web_id", "s_crawled_wb_web_id", "set", limit=10, kv=False)
