#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/13 14:44
# @Email     : billsteve@126.com
# @Des       : 
# @File        : ComKeysModel
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ComKey(Base, BaseModel):
    __tablename__ = 'com_keys'

    id = Column(Integer, primary_key=True)
    com_name = Column(VARCHAR(200))
    short_name = Column(VARCHAR(100))
    web_id = Column(Integer)
    web_url = Column(VARCHAR(100))
    web_key = Column(VARCHAR(100), unique=True)
    cassets = Column(Integer)
    cinvestment = Column(Integer)
    cjob = Column(Integer)
    clawsuit = Column(Integer)
    creport = Column(Integer)
    crun = Column(Integer)
    firm = Column(Integer)
    info = Column(VARCHAR(40))
    is_del = Column(Integer)
    level = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.cassets = kw.get("cassets", None)
        self.cinvestment = kw.get("cinvestment", None)
        self.cjob = kw.get("cjob", None)
        self.clawsuit = kw.get("clawsuit", None)
        self.com_name = kw.get("com_name", None)
        self.create_ts = kw.get("create_ts", None)
        self.creport = kw.get("creport", None)
        self.crun = kw.get("crun", None)
        self.firm = kw.get("firm", None)
        self.get = kw.get("get", None)
        self.getAll = kw.get("getAll", None)
        self.getAllIds = kw.get("getAllIds", None)
        self.getByFromId = kw.get("getByFromId", None)
        self.getByFromIdAndMod = kw.get("getByFromIdAndMod", None)
        self.getByName = kw.get("getByName", None)
        self.id = kw.get("id", None)
        self.info = kw.get("info", None)
        self.is_del = kw.get("is_del", None)
        self.level = kw.get("level", None)
        self.metadata = kw.get("metadata", None)
        self.short_name = kw.get("short_name", None)
        self.update_ts = kw.get("update_ts", None)
        self.web_key = kw.get("web_key", None)
        self.web_url = kw.get("web_url", None)
        self.web_id = kw.get("web_id", None)

    @staticmethod
    def saveComKey(data, session):
        web_key = data["web_key"]
        if web_key:
            exists = ComKey.getByKV("web_key", web_key, session)
            if not exists:
                web_key = ComKey(**data)
                ComKey.addModel(web_key, session)
                return web_key.id
            else:
                return exists[0].id
