#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/10/21 12:41
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : CompanyTyc.py
# @Software : PyCharm
# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, Index, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyTyc(Base, BaseModel):
    __tablename__ = 'company_tyc'
    __table_args__ = (
        Index('wy', 'no', 'creditno', unique=True),
    )

    id = Column(Integer, primary_key=True)
    web_id = Column(String(80, 'utf8mb4_unicode_ci'), index=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'))
    no = Column(String(80, 'utf8mb4_unicode_ci'), index=True)
    creditno = Column(String(80, 'utf8mb4_unicode_ci'), index=True)
    is_del = Column(Integer)
    u_ts = Column(Integer)
    c_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.c_ts = kw.get("c_ts", None)
        self.creditno = kw.get("creditno", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.no = kw.get("no", None)
        self.u_ts = kw.get("u_ts", None)
        self.web_id = kw.get("web_id", None)


if __name__ == '__main__':
    createInitFunction(CompanyTyc)
