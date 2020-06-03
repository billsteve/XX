#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/11/20 16:51
# @Author   : Peter
# @Des       : 
# @File        : WeiboInfo
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class WeiboInfo(Base, BaseModel):
    __tablename__ = 'weibo_info'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11))
    created_at = Column(String(255))
    web_id = Column(String(255))
    idstr = Column(String(255))
    mid = Column(String(255))
    can_edit = Column(String(255))
    show_additional_indication = Column(INTEGER(11))
    text = Column(String(255))
    textLength = Column(INTEGER(11))
    source = Column(String(255))
    favorited = Column(String(255))
    thumbnail_pic = Column(String(255))
    bmiddle_pic = Column(String(255))
    original_pic = Column(String(255))
    is_paid = Column(String(255))
    mblog_vip_type = Column(INTEGER(11))
    reposts_count = Column(INTEGER(11))
    comments_count = Column(INTEGER(11))
    attitudes_count = Column(INTEGER(11))
    pending_approval_count = Column(INTEGER(11))
    isLongText = Column(String(255))
    reward_exhibition_type = Column(INTEGER(11))
    hide_flag = Column(INTEGER(11))
    expire_time = Column(INTEGER(11))
    mblogtype = Column(INTEGER(11))
    more_info_type = Column(INTEGER(11))
    cardid = Column(String(255))
    extern_safe = Column(INTEGER(11))
    content_auth = Column(INTEGER(11))
    hide_hot_flow = Column(INTEGER(11))
    mark = Column(String(255))
    weibo_position = Column(INTEGER(11))
    show_attitude_bar = Column(INTEGER(11))
    readtimetype = Column(String(255))
    bid = Column(String(255))
    is_del = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.attitudes_count = kw.get("attitudes_count", None)
        self.bid = kw.get("bid", None)
        self.bmiddle_pic = kw.get("bmiddle_pic", None)
        self.can_edit = kw.get("can_edit", None)
        self.cardid = kw.get("cardid", None)
        self.comments_count = kw.get("comments_count", None)
        self.content_auth = kw.get("content_auth", None)
        self.create_ts = kw.get("create_ts", None)
        self.created_at = kw.get("created_at", None)
        self.expire_time = kw.get("expire_time", None)
        self.extern_safe = kw.get("extern_safe", None)
        self.favorited = kw.get("favorited", None)
        self.hide_flag = kw.get("hide_flag", None)
        self.hide_hot_flow = kw.get("hide_hot_flow", None)
        self.id = kw.get("id", None)
        self.idstr = kw.get("idstr", None)
        self.isLongText = kw.get("isLongText", None)
        self.is_del = kw.get("is_del", None)
        self.is_paid = kw.get("is_paid", None)
        self.mark = kw.get("mark", None)
        self.mblog_vip_type = kw.get("mblog_vip_type", None)
        self.mblogtype = kw.get("mblogtype", None)
        self.metadata = kw.get("metadata", None)
        self.mid = kw.get("mid", None)
        self.more_info_type = kw.get("more_info_type", None)
        self.original_pic = kw.get("original_pic", None)
        self.pending_approval_count = kw.get("pending_approval_count", None)
        self.readtimetype = kw.get("readtimetype", None)
        self.reposts_count = kw.get("reposts_count", None)
        self.reward_exhibition_type = kw.get("reward_exhibition_type", None)
        self.show_additional_indication = kw.get("show_additional_indication", None)
        self.show_attitude_bar = kw.get("show_attitude_bar", None)
        self.source = kw.get("source", None)
        self.text = kw.get("text", None)
        self.textLength = kw.get("textLength", None)
        self.thumbnail_pic = kw.get("thumbnail_pic", None)
        self.update_ts = kw.get("update_ts", None)
        self.user_id = kw.get("user_id", None)
        self.web_id = kw.get("web_id", None)
        self.weibo_position = kw.get("weibo_position", None)


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(WeiboInfo):
        if not (str(k).startswith("_") or isinstance(getattr(WeiboInfo, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
