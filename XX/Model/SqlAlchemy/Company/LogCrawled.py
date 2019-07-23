#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/10/12 11:22
# @Author   : Peter
# @Des       : 
# @File        : LogCrawled
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class LogCrawledModel(Base, BaseModel):
    __tablename__ = 'log_crawled'

    id = Column(Integer, primary_key=True)
    web_key = Column(String(40))
    spiders = Column(String(40))
    relation = Column(TINYINT(1))
    is_del = Column(TINYINT(1))
    c_ts = Column(Integer)
    u_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.c_ts = kw.get("c_ts", None)
        self.web_key = kw.get("web_key", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.relation = kw.get("relation", None)
        self.spiders = kw.get("spiders", None)
        self.u_ts = kw.get("u_ts", None)


if __name__ == '__main__':
    createInitFunction(LogCrawledModel)
