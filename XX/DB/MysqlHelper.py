#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/17 11:09
# @File           : Mysql2Redis
# @Des           :
# @Email        : billsteve@126.com
import pymysql
import requests
from XX.List.ListHelper import ListHelper


class MysqlHelper:
    pool = None
    db = None
    host = None

    def __init__(self, host="127.0.0.1", user="root", pwd="root", db="test", port=3306, charset="utf8",**kw):
        self._conn = pymysql.connect(host, user, pwd, db, port=port, charset=charset.replace("-", ""))
        if kw.get("kv"):
            self.cur = self._conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            self.cur = self._conn.cursor()

    def getLists(self, sql, vals=None, cursor=None):
        self.cur.execute(sql, vals)
        res = ListHelper.decodeV(self.cur.fetchall())
        return res

    def execQuery(self, sql, vals=None, cursor=None):
        res = self.cur.execute(sql, vals)
        self._conn.commit()
        return res

    def execQueryNoCommit(self, sql, vals=None, cursor=None):
        return self.cur.execute(sql, vals)

    def commitQuery(self):
        self._conn.commit()

    def rollbackQuery(self):
        self._conn.rollback()

    def getLastInsertId(self):
        return self.cur.lastrowid

    def closeConn(self):
        self._conn.close()

    def dispose(self, method="commit"):
        if method == "commit":
            self._conn.commit()
        else:
            self._conn.rollback()
        self.cur.close()
        self._conn.close()

    def CheckInfo(self, url, data):
        requests.post(url, data=data)

class DDLHelper:
    def get_less_columns(jd, ddl):
        t = set()
        for line in ddl.split("\n"):
            if line and line.find("`") >= 0:
                t.add(line.split("`")[1])
        return set(jd.keys()) - t
    
    def getColumnsList(ddl):
        t = []
        for line in ddl.split("\n"):
            if line and line.find("`") >= 0:
                t.append(line.split("`")[1])
        return t
