#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/5 15:43
# @Email     : billsteve@126.com
# @Des       : HBASE帮助类
# @File        : HBaseHelper
# @Software: PyCharm
import time
from hbase import Hbase
from hbase.ttypes import *
from thrift.transport import TSocket
import XX.Encrypt.EncryptHelper as enc


class HBaseHelper:
    client = None

    def __init__(self, **kw):
        self.transport = TSocket.TSocket(kw.get("host", "localhost"), kw.get("port", 9090))
        self.transport.open()
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(self.protocol)

    def getClinet(self, **kw):
        transport = TSocket.TSocket(kw.get("host", "localhost"), kw.get("port", 9090))
        transport.open()
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = Hbase.Client(protocol)
        return self.client

    def getClinetByCfg(self, cfg):
        return self.getClinet(**cfg)

    # 获取最近三天的新数据
    def getCrawlCacheResponse(self, tableName, spider_name, url, expire_seconds=86400, client=None):
        self.client = client if client else self.client
        result = self.client.getRowWithColumns(tableName, spider_name + "_" + enc.Encrypt.md5(url), ["data:json"])
        if result:
            if time.time() - result[0].columns.get('data:json').timestamp // 1000 <= expire_seconds:
                return result[0].columns.get('data:json').value

    # 添加缓存数据
    def addCrawlCacheReponse(self, project, spider_name, url, fc, value, client=None):
        self.client = client if client else self.client
        mutation = Mutation(column=fc, value=value)
        return self.client.mutateRow("crawl_cache_" + project, spider_name + "_" + enc.Encrypt.md5(url), [mutation])

    # 创建表
    def createTable(self, table_name, mcolumns, client=None):
        self.client = client if client else self.client
        self.client.createTable(table_name, mcolumns)

    # 获取表
    def getTables(self, client=None):
        self.client = client if client else self.client
        return self.client.getTableNames()

    # 删除整行
    def delRow(self, table_name, row, client=None):
        self.client = client if client else self.client
        return self.client.deleteAllRow(table_name, row)

    # 删除列
    def delRowColumns(self, table_name, row, column, client=None):
        self.client = client if client else self.client
        self.client.deleteAll(table_name, row, column)

    # 遍历表
    def getLists(self, table, startRow, scolumns, limit=10, client=None):
        self.client = client if client else self.client
        scan_id = self.client.scannerOpen(table, startRow, scolumns)
        return self.client.scannerGetList(scan_id, limit)

    # 添加列
    def addRowColumn(self, table, row, fc, value, client=None):
        self.client = client if client else self.client
        mutation = Mutation(column=fc, value=value)
        return self.client.mutateRow(table, row, [mutation])


if __name__ == '__main__':
    hb = HBaseHelper(host="zhihan00")
    print(hb.getTables())
    exit()
    columns = []
    columns.append(ColumnDescriptor(name='source'))
    columns.append(ColumnDescriptor(name='data'))
    hb.createTable("crawl_zhihan", columns)
    exit()
    startRow = ""
    while 1:
        results = hb.getLists("crawl_cache_zhihan", startRow, ["source"])
        if not results:
            print("All Over")
            break
        for result in results:
            startRow = result.row
            print(result.row, result.columns["source:url"].value)
        time.sleep(0.5)
        print("--")
