#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/5 15:43
# @Email     : billsteve@126.com
# @Des       : HBASE帮助类
# @File        : HBaseHelper
# @Software: PyCharm
import happybase


class HappyBaseHeleper:
    # TODO:Check 是否是一个pool
    _pool = None
    connection = None
    table = None

    def __init__(self, **kw):
        if kw.get("host"):
            if not self._pool:
                self.pool = happybase.ConnectionPool(size=3, host=kw.get("host", "localhost"), port=kw.get("port", 9090), protocol='binary', transport='buffered')
            self.connection = self.pool._acquire_connection()
        if self.connection and kw.get("table"):
            self.table = self.connection.table(kw.get("table"))

    def getConnection(self, host=None, port=None):
        self.__init__(host=host, port=port)
        return self.connection

    def getConnectionByCfg(self, cfg):
        return self.getConnection(**cfg)

    def getPoolByCfg(self, **kw):
        if kw.get("host"):
            if not self._pool:
                self.pool = happybase.ConnectionPool(size=kw.get("size", 3), host=kw.get("host", "localhost"), port=kw.get("port", 9090), protocol='binary', transport='buffered')
            return self.pool

    def getTable(self, table, conn=None, pool=None):
        self.connection = conn if conn else self.connection
        # TODO:CHECK, return in with
        if pool:
            with self.pool.connection() as conn:
                return conn.table(table)
        return self.connection.table(table)

    # 创建表
    def createTable(self, table_name, mcolumns, conn=None):
        self.connection = conn if conn else self.connection
        return self.connection.createTable(table_name, mcolumns)

    # 获取表
    def getTables(self, conn=None):
        self.connection = conn if conn else self.connection
        return self.connection.getTableNames()

    # 获取行
    def getRow(self, row, conn=None, table=None):
        self.connection = conn if conn else self.connection
        self.table = table if table else self.table
        return self.table.get(row)

    # 删除行
    def delRow(self, table_name, row, conn=None):
        self.connection = conn if conn else self.connection
        return self.connection.deleteAllRow(table_name, row)

    # 删除列
    def delRowColumns(self, table_name, row, column, conn=None):
        self.connection = conn if conn else self.connection
        return self.connection.deleteAll(table_name, row, column)

    # 遍历表
    def getLists(self, table, startRow, scolumns, limit=10, conn=None):
        self.connection = conn if conn else self.connection
        scan_id = self.connection.scannerOpen(table, startRow, scolumns)
        return self.connection.scannerGetList(scan_id, limit)

    # 添加行
    def addRowColumn(self, row, data, conn=None, table=None):
        self.connection = conn if conn else self.connection
        self.table = table if table else self.table
        return self.table.put(row, data)

    # 表总数统计
    def countTable(self):
        pass

    # row_key前缀总数统计
    def countPrefix(self):
        pass


if __name__ == '__main__':
    conn = HappyBaseHeleper()
    conn.getConnection(host="zhihan00", port=9090)
    conn.table = conn.connection.table("crawl_CrawlWeibo")
    pass
