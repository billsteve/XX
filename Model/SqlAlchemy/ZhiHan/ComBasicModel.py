#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/8/25 2:42
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : ComBasic1.py
# @Software : PyCharm
import time

from XX.Model.SqlAlchemy.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ComBasic1Model(Base, BaseModel):
    __tablename__ = 'com_basic1'

    id = Column(Integer, primary_key=True)
    web_id = Column(String(255), unique=True)
    batchid = Column(String(255))
    oaddress = Column(String(255))
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
        self.oaddress = kw.get("oaddress", None)
        self.oname = kw.get("oname", None)
        self.orpt_name = kw.get("orpt_name", None)
        self.regcode = kw.get("regcode", None)
        self.u_ts = kw.get("u_ts", None)
        self.uccode = kw.get("uccode", None)
        self.web_id = kw.get("web_id", None)


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(ComBasic1Model):
        if not (str(k).startswith("_") or isinstance(getattr(ComBasic1Model, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
