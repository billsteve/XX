#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:34
# @Author   : Peter
# @Des       : 
# @File        : PostInfo
# @Software: PyCharm

from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class PostInfoModel(Base, BaseModel):
    __tablename__ = 'bbs_post_info'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    bbs_read_num = Column(Integer)
    bbs_like_num = Column(Integer)
    bbs_comment_num = Column(Integer)
    bbs_forward_num = Column(Integer)
    tendays_weight = Column(Float)
    month_weight = Column(Float)
    total_weight = Column(Float)
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.post_id = kw.get("post_id", None)
        self.bbs_read_num = kw.get("bbs_read_num", None)
        self.bbs_like_num = kw.get("bbs_like_num", None)
        self.bbs_comment_num = kw.get("bbs_comment_num", None)
        self.bbs_forward_num = kw.get("bbs_forward_num", None)
        self.tendays_weight = kw.get("tendays_weight", None)
        self.month_weight = kw.get("month_weight", None)
        self.total_weight = kw.get("total_weight", None)
        self.is_del = kw.get("is_del", None)
        self.create_ts = kw.get("create_ts", None)
        self.update_ts = kw.get("update_ts", None)


class PostInfosModel(Base, BaseModel):
    __tablename__ = 'bbs_post_infos'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(35))
    post_id = Column(Integer)
    bbs_read_num = Column(Integer)
    bbs_like_num = Column(Integer)
    bbs_comment_num = Column(Integer)
    bbs_forward_num = Column(Integer)
    tendays_weight = Column(Float)
    month_weight = Column(Float)
    total_weight = Column(Float)
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.uuid = kw.get("uuid", None)
        self.post_id = kw.get("post_id", None)
        self.bbs_read_num = kw.get("bbs_read_num", None)
        self.bbs_like_num = kw.get("bbs_like_num", None)
        self.bbs_comment_num = kw.get("bbs_comment_num", None)
        self.bbs_forward_num = kw.get("bbs_forward_num", None)
        self.tendays_weight = kw.get("tendays_weight", None)
        self.month_weight = kw.get("month_weight", None)
        self.total_weight = kw.get("total_weight", None)
        self.is_del = kw.get("is_del", None)
        self.create_ts = kw.get("create_ts", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getByUuid(uuid, session):
        return session.query(PostInfosModel).filter(PostInfosModel.uuid == uuid).all()
