#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/6 10:05
# @Author   : Peter
# @Des       : 
# @File        : CarTip
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CarDictModel(Base, BaseModel):
    __tablename__ = 'car_dict'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    score = Column(String(255))
    is_del = Column(Integer)
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.score = kw.get("score", None)
        self.update_ts = kw.get("update_ts", None)


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(CarDictModel):
        if not (str(k).startswith("_") or isinstance(getattr(CarDictModel, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
