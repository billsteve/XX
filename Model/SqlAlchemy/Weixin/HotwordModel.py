#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/1/3 10:20
# @Email     : billsteve@126.com
# @Des       : 热点
# @File        : HotwordModel
# @Software: PyCharm
from sqlalchemy import Column, Date, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base
import XX.Model.SqlAlchemy.BaseModel as BaseModel

Base = declarative_base()
metadata = Base.metadata


class HotwordModel(Base, BaseModel.BaseModel):
    __tablename__ = 'hotword'

    id = Column(INTEGER(11), primary_key=True)
    word = Column(String(180))
    day = Column(Date)
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.day = kw.get("day", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)
        self.word = kw.get("word", None)


if __name__ == '__main__':
    BaseModel.createInitFunction(HotwordModel)
