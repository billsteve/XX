#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/12/2 16:10
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : DataProductor.py
# @Des         : 
# @Software : PyCharm
import json
import time

import XX.DB.RedisHelper as dr
import XX.Date.DatetimeHelper as dt
import XX.Encrypt.EncryptHelper as enc
import XX.File.FileHelper as uf
import XX.Tools.BuiltinFunctions as bf
from logzero import logger
from thrift.transport import TSocket

try:
    from hbase import Hbase
    from hbase.ttypes import *
except ImportError as e:
    pass


class DataProducer:
    @staticmethod
    def Json2Redis(*args, **kw):
        pass

    @staticmethod
    def Json2Kafka(*args, **kw):
        pass


class JsonFileProducer(DataProducer):
    @staticmethod
    def Json2Redis(*args, **kw):
        rcfg = kw.get("rcfg")
        if not rcfg:
            print("No rcfg" + "===" * 10)
            return
        rename = kw.get("rename", 0)
        conn_redis = dr.RedisHelper.getRedisConnectByCfg(rcfg)
        fp = kw.get("fp", "")
        ts = kw.get("ts", 1)
        spider = kw.get("spider")
        if rename and str(fp).startswith(dt.GetToday().replace("-", "_")):
            return

        for line in open(fp, encoding="utf-8"):
            length = conn_redis.llen(spider + ":items")
            if length > 50000:
                bf.printFromHead(fp + "\t Too much,Please customer\t" + str(length) + "\t\t")
                time.sleep(ts)
            bf.printBlankEnd(conn_redis.lpush(spider + ":items", line))
        if rename:
            uf.FileHelper.renameFile(fp, str(fp) + "1")
        print("=====File Over\t" + fp + "=====")
        conn_redis.connection_pool.disconnect()


class JsonFile2HBase(JsonFileProducer):

    def __init__(self, *args, **kwargs):
        transport = TSocket.TSocket(kwargs.get("hbase_host", "localhost"), kwargs.get("hbase_port", 9090))
        transport.open()
        self.protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = Hbase.Client(self.protocol)

        # 判断是否有表，没有则生成
        tables = self.client.getTableNames()
        self.table_name = "crawl_" + kwargs.get("project", "test")
        if self.table_name not in tables:
            source = ColumnDescriptor(name='source')
            data = ColumnDescriptor(name='data')
            self.client.createTable(self.table_name, [source, data])

    def json2Hbase(self, *args, **kwargs):
        fp = kwargs.get("fp", "")
        if fp:
            for line in open(fp, encoding="utf-8"):
                url = json.loads(line).get("url")
                if url:
                    row = kwargs.get("spider") + "_" + enc.Encrypt.md5(url)
                    mutations = list()
                    mutations.append(Mutation(column="data:json", value=str(line)))
                    self.client.mutateRow(self.table_name, row, mutations)
                    logger.info("Json  2 hbase " + row)
                else:
                    print("No url")
        else:
            print("No fp")


def JsonFileLine2Redis(fp, spider, rcfg, fn, rename=1, ts=10):
    JsonFileProducer.Json2Redis(fp, spider, rcfg, fn, rename=1, ts=10)

# TODO:再抽象一层，就是把某个文件夹下的所有json添加到对应的文件夹队列中
# def run(process_num=10, rp):
# pass
