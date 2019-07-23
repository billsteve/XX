#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/8/17 0:28
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : City.py
# @Software : PyCharm

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from .BaseModel import *

Base = declarative_base()
metadata = Base.metadata


class TestModel(Base, BaseModel):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    is_del = Column(Integer)
    cts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.name = kw.get("name", None)
        self.age = kw.get("age", None)
        self.is_del = kw.get("is_del", None)
        self.cts = kw.get("cts", None)


if __name__ == '__main__':
    createInitFunction(TestModel)
