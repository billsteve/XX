#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/15 14:12
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : ComBasicModel.py
# @Software : PyCharm
# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ComBasicModel(Base, BaseModel):
    __tablename__ = 'com_basic'

    id = Column(Integer, primary_key=True)
    web_id = Column(Integer)
    batchid = Column(String(255))
    orpt_name = Column(String(255))
    oname = Column(String(255))
    regcode = Column(String(255), index=True)
    uccode = Column(String(255), index=True)
    etcode = Column(String(255))
    max_score = Column(String(255))
    is_del = Column(Integer)
    c_ts = Column(Integer)
    u_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.batchid = kw.get("batchid", None)
        self.c_ts = kw.get("c_ts", None)
        self.etcode = kw.get("etcode", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.max_score = kw.get("max_score", None)
        self.metadata = kw.get("metadata", None)
        self.oname = kw.get("oname", None)
        self.orpt_name = kw.get("orpt_name", None)
        self.regcode = kw.get("regcode", None)
        self.u_ts = kw.get("u_ts", None)
        self.uccode = kw.get("uccode", None)
        self.web_id = kw.get("web_id", None)

    @staticmethod
    def getByRegcodeOrUccode(regcode="", uccode="", session=None):
        return session.query(ComBasicModel).filter(or_(ComBasicModel.uccode == uccode, ComBasicModel.regcode == regcode)).limit(1).all()


if __name__ == '__main__':
    createInitFunction(ComBasicModel)
