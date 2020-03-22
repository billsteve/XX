#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/12/2 16:10
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
    def json_2_redis(*args, **kw):
        pass

    @staticmethod
    def json_2_kafka(*args, **kw):
        pass


class JsonFileProducer(DataProducer):
    @staticmethod
    def json_2_redis(*args, **kw):
        rcfg = kw.get("rcfg")
        if not rcfg:
            print("No rcfg" + "===" * 10)
            return
        rename = kw.get("rename", 0)
        conn_redis = dr.RedisHelper.get_redis_connect_by_cfg(rcfg)
        fp = kw.get("fp", "")
        ts = kw.get("ts", 1)
        spider = kw.get("spider")
        if rename and str(fp).startswith(dt.get_today().replace("-", "_")):
            return

        for line in open(fp, encoding="utf-8"):
            length = conn_redis.llen(spider + ":items")
            if length > 50000:
                bf.print_from_head(fp + "\t Too much,Please customer\t" + str(length) + "\t\t")
                time.sleep(ts)
            bf.print_blank_end(conn_redis.lpush(spider + ":items", line))
        if rename:
            uf.FileHelper.rename_file(fp, str(fp) + "1")
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

    def json_2_hbase(self, *args, **kwargs):
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


def json_file_line_2_redis(fp, spider, rcfg, fn, rename=1, ts=10):
    JsonFileProducer.json_2_redis(fp, spider, rcfg, fn, rename=1, ts=10)

# TODO:再抽象一层，就是把某个文件夹下的所有json添加到对应的文件夹队列中
# def run(process_num=10, rp):
# pass
