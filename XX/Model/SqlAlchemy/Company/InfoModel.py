#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/10/26 15:12
# @Author   : Peter
# @Des       : 
# @File        : InfoModel
# @Software: PyCharm
# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, Index, TEXT, VARCHAR, text
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Info12315(Base, BaseModel):
    __tablename__ = 'info12315'
    __table_args__ = (
        Index('wy', 'NBXH', 'REGNO', unique=True),
        Index('REGNO', 'REGNO', 'NBXH')
    )

    id = Column(Integer, primary_key=True)
    ADDR = Column(VARCHAR(255))
    ANADDR = Column(VARCHAR(255))
    ENTTYPE = Column(VARCHAR(255))
    ENTTYPENAME = Column(VARCHAR(255))
    HIGHLIGHTTITLE = Column(VARCHAR(255))
    INVOPT = Column(VARCHAR(255))
    JYFW = Column(TEXT)
    NBXH = Column(VARCHAR(80))
    PRIPID = Column(VARCHAR(255))
    QYBM = Column(VARCHAR(255))
    QYWZ = Column(VARCHAR(255))
    REGNO = Column(VARCHAR(80))
    REGSTATECODE = Column(VARCHAR(255))
    REGSTATE_CN = Column(VARCHAR(255))
    REGUNIT = Column(VARCHAR(255))
    REGUNITNAME = Column(VARCHAR(255))
    SQ = Column(VARCHAR(255))
    S_EXT_NODENUM = Column(VARCHAR(255))
    TEL = Column(VARCHAR(255))
    UBINDTYPE = Column(VARCHAR(255))
    UBINDTYPENAME = Column(VARCHAR(255))
    UNITCODE = Column(VARCHAR(255))
    UNITNAME = Column(VARCHAR(255))
    XZQHBM = Column(VARCHAR(255))
    is_del = Column(Integer)
    u_ts = Column(Integer)
    c_ts = Column(Integer)
    crawl_detail = Column(TINYINT(4), server_default=text("'0'"))

    def __init__(self, *arg, **kw):
        self.ADDR = kw.get("ADDR", None)
        self.ANADDR = kw.get("ANADDR", None)
        self.ENTTYPE = kw.get("ENTTYPE", None)
        self.ENTTYPENAME = kw.get("ENTTYPENAME", None)
        self.HIGHLIGHTTITLE = kw.get("HIGHLIGHTTITLE", None)
        self.INVOPT = kw.get("INVOPT", None)
        self.JYFW = kw.get("JYFW", None)
        self.NBXH = kw.get("NBXH", None)
        self.PRIPID = kw.get("PRIPID", None)
        self.QYBM = kw.get("QYBM", None)
        self.QYWZ = kw.get("QYWZ", None)
        self.REGNO = kw.get("REGNO", None)
        self.REGSTATECODE = kw.get("REGSTATECODE", None)
        self.REGSTATE_CN = kw.get("REGSTATE_CN", None)
        self.REGUNIT = kw.get("REGUNIT", None)
        self.REGUNITNAME = kw.get("REGUNITNAME", None)
        self.SQ = kw.get("SQ", None)
        self.S_EXT_NODENUM = kw.get("S_EXT_NODENUM", None)
        self.TEL = kw.get("TEL", None)
        self.UBINDTYPE = kw.get("UBINDTYPE", None)
        self.UBINDTYPENAME = kw.get("UBINDTYPENAME", None)
        self.UNITCODE = kw.get("UNITCODE", None)
        self.UNITNAME = kw.get("UNITNAME", None)
        self.XZQHBM = kw.get("XZQHBM", None)
        self.c_ts = kw.get("c_ts", None)
        self.crawl_detail = kw.get("crawl_detail", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.u_ts = kw.get("u_ts", None)


if __name__ == '__main__':
    createInitFunction(Info12315)
