#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/18 11:00
# @Author   : Peter
# @Des       : 
# @File        : ComModel
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String, Integer, or_
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ComModel(Base, BaseModel):
    __tablename__ = 'com'

    id = Column(Integer, primary_key=True)
    regno = Column(String(20), index=True)
    creditno = Column(String(20), index=True)
    other = Column(String(20), index=True)
    is_del = Column(Integer)
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.creditno = kw.get("creditno", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.other = kw.get("other", None)
        self.regno = kw.get("regno", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getByRegcodeOrUccode(regno="", creditno="", other="", session=None):
        return session.query(ComModel).filter(or_(ComModel.regno == regno, ComModel.creditno == creditno, ComModel.other == other)).limit(1).all()


if __name__ == '__main__':
    createInitFunction(ComModel)
