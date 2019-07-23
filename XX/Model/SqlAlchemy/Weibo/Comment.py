#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/11/22 17:34
# @Author   : Peter
# @Des       : 
# @File        : Comment
# @Software: PyCharm
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from XX.Model.SqlAlchemy.BaseModel import *

Base = declarative_base()
metadata = Base.metadata


class WeiboComment(Base, BaseModel):
    __tablename__ = 'weibo_comment'

    id = Column(INTEGER(11), primary_key=True)
    weibo_id = Column(INTEGER(11))
    web_id =  Column(String(255))
    user_id = Column(INTEGER(11))
    p_id = Column(INTEGER(11))
    comments_num = Column(INTEGER(11))
    created_at = Column(String(255))
    rootid = Column(String(255))
    floor_number = Column(INTEGER(11))
    text = Column(String(255))
    disable_reply = Column(INTEGER(11))
    mid = Column(String(255))
    max_id = Column(INTEGER(11))
    total_number = Column(INTEGER(11))
    isLikedByMblogAuthor = Column(String(255))
    more_info_type = Column(INTEGER(11))
    bid = Column(String(255))
    source = Column(String(255))
    like_count = Column(INTEGER(11))
    liked = Column(String(255))
    is_del = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.bid = kw.get("bid", None)
        self.comments_num = kw.get("comments_num", None)
        self.create_ts = kw.get("create_ts", None)
        self.created_at = kw.get("created_at", None)
        self.disable_reply = kw.get("disable_reply", None)
        self.floor_number = kw.get("floor_number", None)
        self.id = kw.get("id", None)
        self.isLikedByMblogAuthor = kw.get("isLikedByMblogAuthor", None)
        self.is_del = kw.get("is_del", None)
        self.like_count = kw.get("like_count", None)
        self.liked = kw.get("liked", None)
        self.max_id = kw.get("max_id", None)
        self.metadata = kw.get("metadata", None)
        self.mid = kw.get("mid", None)
        self.more_info_type = kw.get("more_info_type", None)
        self.p_id = kw.get("p_id", None)
        self.rootid = kw.get("rootid", None)
        self.source = kw.get("source", None)
        self.text = kw.get("text", None)
        self.total_number = kw.get("total_number", None)
        self.update_ts = kw.get("update_ts", None)
        self.user_id = kw.get("user_id", None)
        self.web_id = kw.get("web_id", None)
        self.weibo_id = kw.get("weibo_id", None)


if __name__ == '__main__':
    createInitFunction(WeiboComment)
