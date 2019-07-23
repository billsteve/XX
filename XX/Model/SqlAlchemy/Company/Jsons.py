#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/19 14:40
# @Email     : billsteve@126.com
# @Des       : 
# @File        : Jsons
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class JsonModel(Base):
    __tablename__ = 'jsons'

    id = Column(Integer, primary_key=True)
    jsons = Column(String(255))

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.jsons = kw.get("jsons", None)
        self.metadata = kw.get("metadata", None)


if __name__ == '__main__':
    createInitFunction(JsonModel)
