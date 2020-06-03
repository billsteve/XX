#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/10/18 14:58
# @Author   : Peter
# @Des       : 
# @File        : WeiboUser
# @Software: PyCharm
# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class WeiboUserModel(Base, BaseModel):
    __tablename__ = 'weibo_account'

    id = Column(Integer, primary_key=True)
    userName = Column(String(20))
    posts = Column(Integer)
    focus_num = Column(Integer)
    funs_num = Column(Integer)
    regTime = Column(String(20))
    addr = Column(String(20))
    signature = Column(String(300))
    tag_web = Column(String(255))
    tag_user = Column(String(255))
    intro = Column(String(255))
    uid = Column(Integer)
    fid = Column(Integer)
    authen_type = Column(Integer)
    gender = Column(Integer)
    level = Column(Integer)
    is_del = Column(Integer)
    update_ts = Column(Integer)
    containerid = Column(String(255))
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.addr = kw.get("addr", None)
        self.authen_type = kw.get("authen_type", None)
        self.containerid = kw.get("containerid", None)
        self.create_ts = kw.get("create_ts", None)
        self.fid = kw.get("fid", None)
        self.focus_num = kw.get("focus_num", None)
        self.funs_num = kw.get("funs_num", None)
        self.gender = kw.get("gender", None)
        self.id = kw.get("id", None)
        self.intro = kw.get("intro", None)
        self.is_del = kw.get("is_del", None)
        self.level = kw.get("level", None)
        self.metadata = kw.get("metadata", None)
        self.posts = kw.get("posts", None)
        self.regTime = kw.get("regTime", None)
        self.signature = kw.get("signature", None)
        self.tag_user = kw.get("tag_user", None)
        self.tag_web = kw.get("tag_web", None)
        self.uid = kw.get("uid", None)
        self.update_ts = kw.get("update_ts", None)
        self.userName = kw.get("userName", None)


if __name__ == '__main__':
    BaseModel.createInitFunction(WeiboUserModel)
