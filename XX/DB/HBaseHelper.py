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

    def get_client(self, **kw):
        transport = TSocket.TSocket(kw.get("host", "localhost"), kw.get("port", 9090))
        transport.open()
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = Hbase.Client(protocol)
        return self.client

    def get_client_by_cfg(self, cfg):
        return self.get_client(**cfg)

    # 获取最近三天的新数据
    def get_crawl_cache_response(self, table_name, spider_name, url, expire_seconds=86400, client=None):
        self.client = client if client else self.client
        result = self.client.getRowWithColumns(table_name, spider_name + "_" + enc.Encrypt.md5(url), ["data:json"])
        if result:
            if time.time() - result[0].columns.get('data:json').timestamp // 1000 <= expire_seconds:
                return result[0].columns.get('data:json').value

    # 添加缓存数据
    def add_crawl_cache_response(self, project, spider_name, url, fc, value, client=None):
        self.client = client if client else self.client
        mutation = Mutation(column=fc, value=value)
        return self.client.mutateRow("crawl_cache_" + project, spider_name + "_" + enc.Encrypt.md5(url), [mutation])

    # 创建表
    def create_table(self, table_name, columns, client=None):
        self.client = client if client else self.client
        self.client.createTable(table_name, columns)

    # 获取表
    def get_tables(self, client=None):
        self.client = client if client else self.client
        return self.client.getTableNames()

    # 删除整行
    def del_row(self, table_name, row, client=None):
        self.client = client if client else self.client
        return self.client.deleteAllRow(table_name, row)

    # 删除列
    def del_row_columns(self, table_name, row, column, client=None):
        self.client = client if client else self.client
        self.client.deleteAll(table_name, row, column)

    # 遍历表
    def get_lists(self, table, start_row, columns, limit=10, client=None):
        self.client = client if client else self.client
        scan_id = self.client.scannerOpen(table, start_row, columns)
        return self.client.scannerGetList(scan_id, limit)

    # 添加列
    def add_row_column(self, table, row, fc, value, client=None):
        self.client = client if client else self.client
        mutation = Mutation(column=fc, value=value)
        return self.client.mutateRow(table, row, [mutation])


if __name__ == '__main__':
    hb = HBaseHelper(host="zhihan00")
    print(hb.get_tables())
    exit()
    columns = list()
    columns.append(ColumnDescriptor(name='source'))
    columns.append(ColumnDescriptor(name='data'))
    hb.create_table("crawl_zhihan", columns)
    exit()
    start_row = ""
    while 1:
        results = hb.get_lists("crawl_cache_zhihan", start_row, ["source"])
        if not results:
            print("All Over")
            break
        for result in results:
            startRow = result.row
            print(result.row, result.columns["source:url"].value)
        time.sleep(0.5)
        print("--")
