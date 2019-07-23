#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/17 11:09
# @File           : Mysql2Redis
# @Des           :
# @Email        : billsteve@126.com
import pymysql
import requests
from DBUtils.PooledDB import PooledDB
from XX.List.ListHelper import ListHelper


class MysqlPoolHelper:
    __pool = None
    db = None
    host = None

    def __init__(self, host="127.0.0.1", user="root", pwd="root", db="test", port=3306, charset="utf8", kv=1, **kw):
        self._conn = MysqlPoolHelper._getConn(host, user, pwd, db, port, charset.replace("-", ""))
        if kv:
            self.cur = self._conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            self.cur = self._conn.cursor()

    @staticmethod
    def _getConn(host, user, pwd, db, port=3306, charset="utf8"):
        if MysqlPoolHelper.__pool is None or MysqlPoolHelper.db != db or MysqlPoolHelper.host != host:
            MysqlPoolHelper.db = db
            MysqlPoolHelper.__pool = PooledDB(creator=pymysql, host=host, port=port, user=user, passwd=pwd, db=db, use_unicode=False, charset=charset)
            print(host, port, user, pwd, db, charset)
        return MysqlPoolHelper.__pool.connection() if MysqlPoolHelper.__pool else None

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


if __name__ == "__main__":
    DBHOST1 = "localhost"
    DBPORT = 3306
    DBUSER = "root"
    DBPWD = "DRsXT5ZJ6Oi55LPQ"
    DBNAME = "test"
    DBCHAR = "utf8"

    conn = MysqlPoolHelper(DBHOST1, DBUSER, DBPWD, DBNAME)
    print(conn)
