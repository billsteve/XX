#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/19 18:00
# @Author   : Peter
# @Des       : 
# @File        : EleModel
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ComInfo(Base, BaseModel):
    __tablename__ = 'com_info'

    id = Column(Integer, primary_key=True)
    OPSCOPE = Column(TEXT)
    entid = Column(VARCHAR(32), unique=True)
    DOM = Column(VARCHAR(255))
    ENTTYPE = Column(Integer)
    ESDATE = Column(VARCHAR(60))
    EMPNUM = Column(VARCHAR(60))
    logo = Column(VARCHAR(255))
    ENTSTATUS = Column(TINYINT(4))
    ENTNAME = Column(VARCHAR(255))
    DOMDISTRICT = Column(VARCHAR(20))
    fstatus = Column(TINYINT(4))
    faren = Column(VARCHAR(255))
    INDUSTRYCO = Column(VARCHAR(40))
    REGCAP = Column(VARCHAR(40))
    isent = Column(VARCHAR(40))
    is_del = Column(TINYINT(4))
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.DOM = kw.get("DOM", None)
        self.DOMDISTRICT = kw.get("DOMDISTRICT", None)
        self.EMPNUM = kw.get("EMPNUM", None)
        self.ENTNAME = kw.get("ENTNAME", None)
        self.ENTSTATUS = kw.get("ENTSTATUS", None)
        self.ENTTYPE = kw.get("ENTTYPE", None)
        self.ESDATE = kw.get("ESDATE", None)
        self.INDUSTRYCO = kw.get("INDUSTRYCO", None)
        self.OPSCOPE = kw.get("OPSCOPE", None)
        self.REGCAP = kw.get("REGCAP", None)
        self.create_ts = kw.get("create_ts", None)
        self.entid = kw.get("entid", None)
        self.faren = kw.get("faren", None)
        self.fstatus = kw.get("fstatus", None)
        self.getByFromId = kw.get("getByFromId", None)
        self.getByFromIdAndMod = kw.get("getByFromIdAndMod", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.isent = kw.get("isent", None)
        self.logo = kw.get("logo", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)


class ComInfoLes(Base, BaseModel):
    __tablename__ = 'com_info_less'

    id = Column(Integer, primary_key=True)
    entid = Column(VARCHAR(32), unique=True)
    DOM = Column(VARCHAR(255))
    REGCAP = Column(VARCHAR(40))
    faren = Column(VARCHAR(255))
    ESDATE = Column(VARCHAR(60))
    logo = Column(VARCHAR(255))
    ENTNAME = Column(VARCHAR(255))
    is_del = Column(TINYINT(4))
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.DOM = kw.get("DOM", None)
        self.ENTNAME = kw.get("ENTNAME", None)
        self.ESDATE = kw.get("ESDATE", None)
        self.REGCAP = kw.get("REGCAP", None)
        self.create_ts = kw.get("create_ts", None)
        self.entid = kw.get("entid", None)
        self.faren = kw.get("faren", None)
        self.getByFromId = kw.get("getByFromId", None)
        self.getByFromIdAndMod = kw.get("getByFromIdAndMod", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.logo = kw.get("logo", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)


class ComInfo2(Base, BaseModel):
    __tablename__ = 'com_info2'

    id = Column(Integer, primary_key=True)
    entid = Column(VARCHAR(32), unique=True)
    DOM = Column(VARCHAR(255))
    REGCAP = Column(VARCHAR(40))
    faren = Column(VARCHAR(255))
    ESDATE = Column(VARCHAR(60))
    logo = Column(VARCHAR(255))
    ENTNAME = Column(VARCHAR(255))
    is_del = Column(TINYINT(4))
    create_ts = Column(Integer)
    update_ts = Column(Integer)


class ComList(Base, BaseModel):
    __tablename__ = 'com_list'

    id = Column(Integer, primary_key=True)
    com_name = Column(VARCHAR(255))
    entid = Column(VARCHAR(40))
    is_del = Column(TINYINT(4))
    create_ts = Column(Integer)
    update_ts = Column(Integer)


if __name__ == '__main__':
    createInitFunction(ComList)
