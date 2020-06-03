#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/13 20:10
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : CountInfo.py
# @Software : PyCharm
# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class WxCountInfo(Base, BaseModel):
    __tablename__ = 'wx_count_info'

    id = Column(Integer, primary_key=True)
    count_id = Column(Integer)
    description = Column(String(255))
    company = Column(String(255))
    register_date = Column(String(255))
    qr = Column(String(255))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.company = kw.get("company", None)
        self.count_id = kw.get("count_id", None)
        self.create_ts = kw.get("create_ts", None)
        self.description = kw.get("description", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.qr = kw.get("qr", None)
        self.register_date = kw.get("register_date", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getInfoByCountId(count_id, session):
        infos = session.query(WxCountInfo).filter(WxCountInfo.count_id == count_id).all()
        return infos[0].id if infos else None


if __name__ == '__main__':
    import types

    print("""\n\n\ndef __init__(self, *arg, **kw):""")
    for k in dir(WxCountInfo):
        if not (str(k).startswith("_") or isinstance(getattr(WxCountInfo, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
