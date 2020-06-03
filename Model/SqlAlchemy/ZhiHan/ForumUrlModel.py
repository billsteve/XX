#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/2/27 15:35
# @File           : ForumUrlModel
# @Des           : 
# @Email        : billsteve@126.com
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Index, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ForumUrlModel(Base, BaseModel):
    __tablename__ = 'forum_url'
    __table_args__ = (
        Index('forum_id', 'forum_id', 'url'),
    )

    id = Column(INTEGER(11), primary_key=True)
    forum_id = Column(INTEGER(11))
    forum_name = Column(String(255))
    url = Column(String(255))
    is_del = Column(TINYINT(4))
    create_ts = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.forum_id = kw.get("forum_id", None)
        self.forum_name = kw.get("forum_name", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)


if __name__ == '__main__':
    createInitFunction(ForumUrlModel)
