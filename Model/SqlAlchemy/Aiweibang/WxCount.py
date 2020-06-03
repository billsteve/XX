#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/12 22:43
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : WxCount.py
# @Software : PyCharm
# coding: utf-8
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class WxCount(Base, BaseModel):
    __tablename__ = 'wx_count'

    id = Column(Integer, primary_key=True)
    ReportMonth = Column(String(255))
    UserId = Column(String(255))
    PostTimes = Column(Integer)
    ArticleCount = Column(Integer)
    ReadNumSum = Column(String(255))
    ReadNumMax = Column(Integer)
    ReadNumAvg = Column(Integer)
    LikeNumSum = Column(String(255))
    TopReadNumAvg = Column(Integer)
    BangIndex = Column(Float)
    UserName = Column(String(255))
    Alias = Column(String(255))
    Description = Column(String(255))
    HeadImgUrl = Column(String(255))
    WechatId = Column(String(255))

    def __init__(self, *arg, **kw):
        self.Alias = kw.get("Alias", None)
        self.ArticleCount = kw.get("ArticleCount", None)
        self.BangIndex = kw.get("BangIndex", None)
        self.Description = kw.get("Description", None)
        self.HeadImgUrl = kw.get("HeadImgUrl", None)
        self.LikeNumSum = kw.get("LikeNumSum", None)
        self.PostTimes = kw.get("PostTimes", None)
        self.ReadNumAvg = kw.get("ReadNumAvg", None)
        self.ReadNumMax = kw.get("ReadNumMax", None)
        self.ReadNumSum = kw.get("ReadNumSum", None)
        self.ReportMonth = kw.get("ReportMonth", None)
        self.TopReadNumAvg = kw.get("TopReadNumAvg", None)
        self.UserId = kw.get("UserId", None)
        self.UserName = kw.get("UserName", None)
        self.WechatId = kw.get("WechatId", None)
        self.id = kw.get("id", None)
        self.metadata = kw.get("metadata", None)

    @staticmethod
    def getInfoByUserId(UserId, session):
        infos = session.query(WxCount).filter(WxCount.UserId == UserId).all()
        return infos[0].id if infos else None

    @staticmethod
    def getInfoByAlias(Alias, session):
        infos = session.query(WxCount).filter(WxCount.Alias == Alias).all()
        return infos[0].id if infos else None

    @staticmethod
    def getByFromId(from_id, session):
        return session.query(WxCount).filter(WxCount.id > from_id).limit(100).all()


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(WxCount):
        if not (str(k).startswith("_") or isinstance(getattr(WxCount, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
