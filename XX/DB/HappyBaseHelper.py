#!/usr/bin/env python
# -*- coding: utf-8 -*-
import happybase


class HappyBaseHeleper:
    connection = None
    table = None
    pool = None

    def __init__(self, **kw):
        if kw:
            self.connection = happybase.Connection(**kw)

    def get_connection_pool(self, size=128, **kw):
        self.pool = happybase.ConnectionPool(**kw, size=size)
        return self.pool

    def get_connection(self, **kwargs):
        if kwargs.get("host"):
            self.connection = happybase.Connection(**kwargs)
            return self.connection

    def get_table(self, table_name, conn=None, pool=None):
        self.connection = conn if conn else self.connection
        return self.connection.table(table_name)

    # 创建表
    def create_table(self, table_name, columns, conn=None):
        self.connection = conn if conn else self.connection
        return self.connection.create_table(table_name, columns)

    # 获取表
    def get_tables(self, conn=None):
        self.connection = conn if conn else self.connection
        return self.connection.tables()

    # 删除表
    def del_table(self, table_name, disable=False, conn=None):
        self.table = self.get_table(table_name, conn) if table_name else self.table
        return self.connection.delete_table(self.table, disable)

    # 获取行
    def get_row(self, row, conn=None, table_name=None):
        self.table = self.get_table(table_name, conn) if table_name else self.table
        return self.table.row(row)

    # 获取列表
    def get_rows(self, row, conn=None, table_name=None):
        self.table = self.get_table(table_name, conn) if table_name else self.table
        return self.table.row(row)

    # 删除行或列
    def del_row(self, row, columns=None, conn=None, table_name=None):
        self.table = self.get_table(table_name, conn) if table_name else self.table
        return self.table.delete(row, columns)

    # 添加行
    def add_row(self, row, data, timestamp=None, wal=True, conn=None, table_name=None):
        self.table = self.get_table(table_name, conn) if table_name else self.table
        return self.table.put(row, data, timestamp=None, wal=True)
