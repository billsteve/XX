#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/14 13:49
# @Author   : Peter
# @Des       : 
# @File        : CarConfig
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CarConfigModel(Base, BaseModel):
    __tablename__ = 'car_config'

    id = Column(Integer, primary_key=True)
    p_id = Column(Integer)
    web_id = Column(Integer)
    name = Column(String(255))
    is_del = Column(Integer)
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.p_id = kw.get("p_id", None)
        self.update_ts = kw.get("update_ts", None)
        self.web_id = kw.get("web_id", None)

    @staticmethod
    def getInfoByName(name, session):
        info = session.query(CarConfigModel).filter(CarConfigModel.name == name).all()
        return info[0] if info else None

    @staticmethod
    def getInfoByNameAndWebId(name, web_id, session):
        return session.query(CarConfigModel).filter(CarConfigModel.name == name, CarConfigModel.web_id == web_id).all()

    @staticmethod
    def getInfoByNameAndPid(name, pid, session):
        return session.query(CarConfigModel).filter(CarConfigModel.name == name, CarConfigModel.p_id == pid).all()


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(CarConfigModel):
        if not (str(k).startswith("_") or isinstance(getattr(CarConfigModel, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
