#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/11/1 11:35
# @Author   : Peter
# @Des       : 
# @File        : UserInfo
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import BaseModel
from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserInfo(Base, BaseModel):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    web_id = Column(BigInteger, unique=True)
    fans_scheme = Column(String(255))
    follow_scheme = Column(String(255))
    showAppTips = Column(Integer)
    scheme = Column(String(255))
    screen_name = Column(String(255), index=True)
    profile_image_url = Column(String(255))
    profile_url = Column(String(255))
    statuses_count = Column(Integer)
    verified = Column(String(255))
    verified_type = Column(Integer)
    verified_type_ext = Column(Integer)
    verified_reason = Column(String(255))
    close_blue_v = Column(String(255))
    description = Column(String(255))
    gender = Column(String(255))
    mbtype = Column(Integer)
    urank = Column(Integer)
    mbrank = Column(Integer)
    follow_me = Column(String(255))
    following = Column(String(255))
    followers_count = Column(Integer)
    follow_count = Column(Integer)
    cover_image_phone = Column(String(255))
    avatar_hd = Column(String(255))
    like = Column(String(255))
    like_me = Column(String(255))
    containid = Column(String(30))
    home_page_containid = Column(String(30))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.avatar_hd = kw.get("avatar_hd", None)
        self.close_blue_v = kw.get("close_blue_v", None)
        self.containid = kw.get("containid", None)
        self.cover_image_phone = kw.get("cover_image_phone", None)
        self.create_ts = kw.get("create_ts", None)
        self.description = kw.get("description", None)
        self.fans_scheme = kw.get("fans_scheme", None)
        self.follow_count = kw.get("follow_count", None)
        self.follow_me = kw.get("follow_me", None)
        self.follow_scheme = kw.get("follow_scheme", None)
        self.followers_count = kw.get("followers_count", None)
        self.following = kw.get("following", None)
        self.gender = kw.get("gender", None)
        self.home_page_containid = kw.get("home_page_containid", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.like = kw.get("like", None)
        self.like_me = kw.get("like_me", None)
        self.mbrank = kw.get("mbrank", None)
        self.mbtype = kw.get("mbtype", None)
        self.metadata = kw.get("metadata", None)
        self.profile_image_url = kw.get("profile_image_url", None)
        self.profile_url = kw.get("profile_url", None)
        self.scheme = kw.get("scheme", None)
        self.screen_name = kw.get("screen_name", None)
        self.showAppTips = kw.get("showAppTips", None)
        self.statuses_count = kw.get("statuses_count", None)
        self.update_ts = kw.get("update_ts", None)
        self.urank = kw.get("urank", None)
        self.verified = kw.get("verified", None)
        self.verified_reason = kw.get("verified_reason", None)
        self.verified_type = kw.get("verified_type", None)
        self.verified_type_ext = kw.get("verified_type_ext", None)
        self.web_id = kw.get("web_id", None)


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(UserInfo):
        if not (str(k).startswith("_") or isinstance(getattr(UserInfo, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
