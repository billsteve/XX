#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/1/4 9:38
# @Email     : billsteve@126.com
# @Des       : SogouCookieModel
# @File        : SogouCookieModel
# @Software: PyCharm
import XX.Model.SqlAlchemy.BaseModel as BM
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SogouCookieModel(Base, BM.BaseModel):
    __tablename__ = 'sogou_cookie'

    id = Column(INTEGER(11), primary_key=True)
    cookie = Column(String(64))
    create_ts = Column(INTEGER(11))
    times = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.cookie = kw.get("cookie", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.metadata = kw.get("metadata", None)
        self.times = kw.get("times", None)


if __name__ == '__main__':
    BM.createInitFunction(SogouCookieModel)
