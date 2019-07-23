#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/29 15:06
# @Author   : Peter
# @Des       : 
# @File        : CompanyChangeModel
# @Software: PyCharm

from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyChange(Base, BaseModel):
    __tablename__ = 'company_change'

    id = Column(Integer, primary_key=True)
    com_id = Column(Integer)
    web_key = Column(String(255, 'utf8mb4_unicode_ci'))
    ProjectName = Column(Text(collation='utf8mb4_unicode_ci'))
    ChangeDate = Column(String(255, 'utf8mb4_unicode_ci'))
    BeforeContent = Column(Text(collation='utf8mb4_unicode_ci'))
    AfterContent = Column(Text(collation='utf8mb4_unicode_ci'))
    is_del = Column(String(255, 'utf8mb4_unicode_ci'))
    create_ts = Column(String(255, 'utf8mb4_unicode_ci'))
    update_ts = Column(String(255, 'utf8mb4_unicode_ci'))

    def __init__(self, *arg, **kw):
        self.AfterContent = kw.get("AfterContent", None)
        self.BeforeContent = kw.get("BeforeContent", None)
        self.ChangeDate = kw.get("ChangeDate", None)
        self.ProjectName = kw.get("ProjectName", None)
        self.com_id = kw.get("com_id", None)
        self.web_key = kw.get("web_key", None)
        self.create_ts = kw.get("create_ts", None)
        self.get = kw.get("get", None)
        self.getAll = kw.get("getAll", None)
        self.getAllIds = kw.get("getAllIds", None)
        self.getByFromId = kw.get("getByFromId", None)
        self.getByFromIdAndMod = kw.get("getByFromIdAndMod", None)
        self.getByName = kw.get("getByName", None)
        self.getColumsByFromIdAndMod = kw.get("getColumsByFromIdAndMod", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.updateId = kw.get("updateId", None)
        self.update_ts = kw.get("update_ts", None)


if __name__ == '__main__':
    createInitFunction(CompanyChange)
