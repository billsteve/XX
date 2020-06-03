#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:30
# @Author   : Peter
# @Des       : 
# @File        : Forum
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Forum(Base, BaseModel):
    __tablename__ = 'forum'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    spider_name = Column(String(255))
    domain = Column(String(255))
    logo = Column(String(255))
    thread_count = Column(TINYINT(4), server_default=text("'1'"))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.name = kw.get("name", None)
        self.spider_name = kw.get("spider_name", None)
        self.domain = kw.get("domain", None)
        self.logo = kw.get("logo", None)
        self.thread_count = kw.get("thread_count", None)
        self.is_del = kw.get("is_del", None)
        self.create_ts = kw.get("create_ts", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getSpiderNameByForumId(_id, session):
        return session.query(Forum.spider_name).filter(Forum.id == _id).all()
