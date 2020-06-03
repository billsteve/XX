#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/2/20 15:14
# @File           : DataSheet
# @Des           : 
# @Email        : billsteve@126.com
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Key(Base, BaseModel):
    __tablename__ = 'keys'

    id = Column(INTEGER(11), primary_key=True)
    k1 = Column(String(20))
    k2 = Column(String(100))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.k1 = kw.get("k1", None)
        self.k2 = kw.get("k2", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)


class Info(Base, BaseModel):
    __tablename__ = 'info'

    id = Column(INTEGER(11), primary_key=True)
    k_id = Column(INTEGER(11))
    k1 = Column(INTEGER(11))
    v1 = Column(INTEGER(11))
    PartNo = Column(String(100))
    Brand = Column(String(100))
    CategoryName = Column(String(100))
    DataParam = Column(Text)
    Description = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.Brand = kw.get("Brand", None)
        self.CategoryName = kw.get("CategoryName", None)
        self.DataParam = kw.get("DataParam", None)
        self.Description = kw.get("Description", None)
        self.k_id = kw.get("k_id", None)
        self.k1 = kw.get("k1", None)
        self.v1 = kw.get("v1", None)
        self.PartNo = kw.get("PartNo", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)


class Snapshot(Base, BaseModel):
    __tablename__ = 'snapshot'

    id = Column(INTEGER(11), primary_key=True)
    kid = Column(INTEGER(11), index=True)
    source_url = Column(String(190), index=True)
    baidu_url = Column(String(190))
    title = Column(String(190), index=True)
    snapshot_url = Column(String(2000))
    crawl_ts = Column(INTEGER(11))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.baidu_url = kw.get("baidu_url", None)
        self.crawl_ts = kw.get("crawl_ts", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.kid = kw.get("kid", None)
        self.metadata = kw.get("metadata", None)
        self.snapshot_url = kw.get("snapshot_url", None)
        self.source_url = kw.get("source_url", None)
        self.title = kw.get("title", None)
        self.update_ts = kw.get("update_ts", None)


if __name__ == '__main__':
    createInitFunction(Snapshot)
