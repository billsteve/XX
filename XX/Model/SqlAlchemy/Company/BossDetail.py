#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/12 16:15
# @Email     : billsteve@126.com
# @Des       : BossDetail
# @File        : BossDetail
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BossDetail(Base, BaseModel):
    __tablename__ = 'boss_detail'

    id = Column(INTEGER(11), primary_key=True)
    boss_web_id = Column(INTEGER(11))
    name = Column(String(255))
    personid = Column(String(255))
    companyname = Column(String(255))
    companykey = Column(String(255))
    face_oss = Column(String(255))
    face = Column(String(255))
    link = Column(String(255))
    job = Column(String(255))
    weibo = Column(String(255))
    des = Column(String(255))
    country = Column(String(255))
    city = Column(String(255))
    county = Column(String(255))
    role = Column(String(255))
    edu = Column(String(255))
    everjob = Column(String(255))
    weixin = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))
    birth = Column(String(255))
    jiguan = Column(String(255))
    sex = Column(String(255))
    hangye = Column(String(255))
    biye = Column(String(255))
    xueli = Column(String(255))
    zhuanye = Column(String(255))
    minzu = Column(String(255))
    hobby = Column(String(255))
    milestone = Column(String(255))
    sayings = Column(String(255))
    type = Column(String(255))
    cleaning_type = Column(String(255))
    click_count = Column(String(255))
    status = Column(String(255))
    is_delete = Column(String(255))
    oper_name = Column(String(255))
    relativeInfoCount = Column(INTEGER(11))
    is_del = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.birth = kw.get("birth", None)
        self.biye = kw.get("biye", None)
        self.boss_web_id = kw.get("boss_web_id", None)
        self.city = kw.get("city", None)
        self.cleaning_type = kw.get("cleaning_type", None)
        self.click_count = kw.get("click_count", None)
        self.companykey = kw.get("companykey", None)
        self.companyname = kw.get("companyname", None)
        self.country = kw.get("country", None)
        self.county = kw.get("county", None)
        self.create_ts = kw.get("create_ts", None)
        self.des = kw.get("des", None)
        self.edu = kw.get("edu", None)
        self.email = kw.get("email", None)
        self.everjob = kw.get("everjob", None)
        self.face = kw.get("face", None)
        self.face_oss = kw.get("face_oss", None)
        self.hangye = kw.get("hangye", None)
        self.hobby = kw.get("hobby", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.is_delete = kw.get("is_delete", None)
        self.jiguan = kw.get("jiguan", None)
        self.job = kw.get("job", None)
        self.link = kw.get("link", None)
        self.metadata = kw.get("metadata", None)
        self.milestone = kw.get("milestone", None)
        self.minzu = kw.get("minzu", None)
        self.name = kw.get("name", None)
        self.oper_name = kw.get("oper_name", None)
        self.personid = kw.get("personid", None)
        self.phone = kw.get("phone", None)
        self.relativeInfoCount = kw.get("relativeInfoCount", None)
        self.role = kw.get("role", None)
        self.sayings = kw.get("sayings", None)
        self.sex = kw.get("sex", None)
        self.status = kw.get("status", None)
        self.type = kw.get("type", None)
        self.update_ts = kw.get("update_ts", None)
        self.weibo = kw.get("weibo", None)
        self.weixin = kw.get("weixin", None)
        self.xueli = kw.get("xueli", None)
        self.zhuanye = kw.get("zhuanye", None)


if __name__ == '__main__':
    createInitFunction(BossDetail)
