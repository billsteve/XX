#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:42
# @Author   : Peter
# @Des       : 
# @File        : User
# @Software: PyCharm
from sqlalchemy import Column, Integer, String, Text, Index
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class PostUserModel(Base, BaseModel):
    __tablename__ = 'bbs_post_user'
    __table_args__ = (
        Index('wy', 'forum_id', 'bbs_postor_web_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    forum_id = Column(Integer)
    bbs_postor_name = Column(String(60))
    bbs_postor_head_pic = Column(String(200))
    post_num = Column(Integer)
    regTime = Column(String(20))
    addr = Column(String(20))
    signature = Column(String(300))
    bbs_postor_web_id = Column(String(200))
    bbs_postor_homepage = Column(String(200))
    bbs_postor_info = Column(Text)
    is_vip = Column(Integer)
    is_locked = Column(Integer)
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.addr = kw.get("addr", None)
        self.bbs_postor_head_pic = kw.get("bbs_postor_head_pic", None)
        self.bbs_postor_homepage = kw.get("bbs_postor_homepage", None)
        self.bbs_postor_info = kw.get("bbs_postor_info", None)
        self.bbs_postor_name = kw.get("bbs_postor_name", None)
        self.bbs_postor_web_id = kw.get("bbs_postor_web_id", None)
        self.create_ts = kw.get("create_ts", None)
        self.forum_id = kw.get("forum_id", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.post_num = kw.get("post_num", None)
        self.regTime = kw.get("regTime", None)
        self.signature = kw.get("signature", None)
        self.update_ts = kw.get("update_ts", None)
        self.is_vip = kw.get("is_vip", None)
        self.is_locked = kw.get("is_locked", None)

    @staticmethod
    def getByForumIdAndPostorWebId(forum_id, bbs_postor_web_id, session):
        return session.query(PostUserModel).filter(PostUserModel.forum_id == forum_id, PostUserModel.bbs_postor_web_id == bbs_postor_web_id).all()


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(PostUserModel):
        if not (str(k).startswith("_") or isinstance(getattr(PostUserModel, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
