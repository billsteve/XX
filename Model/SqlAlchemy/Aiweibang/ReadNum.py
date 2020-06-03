#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/13 19:18
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : ReadNum.py
# @Software : PyCharm
# coding: utf-8
from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.ext.declarative import declarative_base
from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class ReadNum(Base, BaseModel):
    __tablename__ = 'read_num'
    __table_args__ = (
        Index('wy', 'UserId', 'Idx', unique=True),
    )

    id = Column(Integer, primary_key=True)
    UserId = Column(String(255))
    Idx = Column(Integer)
    ReadSumType = Column(Integer)
    ReadSumTypeDesc = Column(String(255))
    ArticleCount = Column(Integer)
    ReadNumMax = Column(Integer)
    ReadNumAvg = Column(Integer)
    LikeNumMax = Column(Integer)
    LikeNumAvg = Column(Integer)
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.ArticleCount = kw.get("ArticleCount", None)
        self.Idx = kw.get("Idx", None)
        self.LikeNumAvg = kw.get("LikeNumAvg", None)
        self.LikeNumMax = kw.get("LikeNumMax", None)
        self.ReadNumAvg = kw.get("ReadNumAvg", None)
        self.ReadNumMax = kw.get("ReadNumMax", None)
        self.ReadSumType = kw.get("ReadSumType", None)
        self.ReadSumTypeDesc = kw.get("ReadSumTypeDesc", None)
        self.UserId = kw.get("UserId", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getInfoByUserIdAndIdx(UserId, Idx, session):
        infos = session.query(ReadNum).filter(ReadNum.UserId == UserId, ReadNum.Idx == Idx).all()
        return infos[0].id if infos else None


if __name__ == '__main__':
    import types

    print("""\n\n\ndef __init__(self, *arg, **kw):""")
    for k in dir(ReadNum):
        if not (str(k).startswith("_") or isinstance(getattr(ReadNum, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
