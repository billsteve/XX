#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/1/3 10:25
# @Email     : billsteve@126.com
# @Des       : 
# @File        : WeixinModel
# @Software: PyCharm
from sqlalchemy import Column, Date, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base
import XX.Model.SqlAlchemy.BaseModel as BaseModel

Base = declarative_base()
metadata = Base.metadata


class WeixinModel(Base, BaseModel.BaseModel):
    __tablename__ = 'weixin'

    id = Column(INTEGER(11), primary_key=True)
    wx_id = Column(INTEGER(11))
    biz = Column(String(32), unique=True)
    name = Column(String(255))
    gh_id = Column(INTEGER(11))
    weixin_id = Column(INTEGER(11))
    head_img = Column(String(255))
    head_img_circle = Column(String(255))
    intro = Column(String(255))
    no1 = Column(INTEGER(11))
    no2 = Column(String(255))
    no3 = Column(INTEGER(11))
    no4 = Column(INTEGER(11))
    no5 = Column(INTEGER(11))
    is_del = Column(TINYINT(1))
    update_Ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.biz = kw.get("biz", None)
        self.create_ts = kw.get("create_ts", None)
        self.gh_id = kw.get("gh_id", None)
        self.head_img = kw.get("head_img", None)
        self.head_img_circle = kw.get("head_img_circle", None)
        self.id = kw.get("id", None)
        self.intro = kw.get("intro", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.no1 = kw.get("no1", None)
        self.no2 = kw.get("no2", None)
        self.no3 = kw.get("no3", None)
        self.no4 = kw.get("no4", None)
        self.no5 = kw.get("no5", None)
        self.update_Ts = kw.get("update_Ts", None)
        self.weixin_id = kw.get("weixin_id", None)
        self.wx_id = kw.get("wx_id", None)


if __name__ == '__main__':
    BaseModel.createInitFunction(WeixinModel)
