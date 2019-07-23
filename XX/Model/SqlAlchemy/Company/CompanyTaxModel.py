#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/29 15:11
# @Author   : Peter
# @Des       : 
# @File        : CompanyTaxModel
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, String, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyTaxModel(Base, BaseModel):
    __tablename__ = 'company_tax'

    id = Column(Integer, primary_key=True)
    com_id = Column(Integer)
    web_key = Column(String(50))
    Name = Column(String(255))
    CreditCode = Column(String(255))
    Address = Column(String(255))
    PhoneNumber = Column(String(255))
    Bank = Column(String(255))
    Bankaccount = Column(String(255))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.Address = kw.get("Address", None)
        self.Bank = kw.get("Bank", None)
        self.Bankaccount = kw.get("Bankaccount", None)
        self.CreditCode = kw.get("CreditCode", None)
        self.Name = kw.get("Name", None)
        self.PhoneNumber = kw.get("PhoneNumber", None)
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
    createInitFunction(CompanyTaxModel)
