#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/21 14:07
import pymongo


class MongoHelper():
    def __init__(self, *arg, **kw):
        self.host = kw.get("host", "localhost")
        self.port = kw.get("host", 27017)

    @staticmethod
    def get_connection(host="localhost", port=2707, pwd=None):
        return pymongo.MongoClient(host, port)

    @staticmethod
    def get_connection_db(host="localhost", port=2707, db=None, pwd=None):
        conn = MongoHelper.get_connection(host, port)
        return conn.db

    @staticmethod
    def get_collection(host="localhost", port=2707, db=None, collection_name=None, username=None, password=None):
        db = MongoHelper.get_connection_db(host, port, db)
        return db.collection_name


if __name__ == '__main__':
    import XX.Model.Struct.MongoConn as MC

    config = MC.zhihan00_cfg
    client = MongoHelper.get_connection(**config)
    db = client.dbname
    col = db.col
    print(db)
    print(col)
    print(col.insert_one({"x": 12}).inserted_id)
