#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:37
# @Author   : Peter
# @Des       : 
# @File        : PostPic
# @Software: PyCharm
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class PostPicModel(Base, BaseModel):
    __tablename__ = 'bbs_post_pic'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    pic_url = Column(String(100))
    location = Column(String(100))
    head_pic = Column(Integer)
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.post_id = kw.get("post_id", None)
        self.pic_url = kw.get("pic_url", None)
        self.location = kw.get("location", None)
        self.head_pic = kw.get("head_pic", None)
        self.is_del = kw.get("is_del", None)
        self.create_ts = kw.get("create_ts", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getByPostIdPicUrl(post_id, pic_url, session):
        return session.query(PostPicModel).filter(PostPicModel.post_id == post_id, PostPicModel.pic_url == pic_url).all()
