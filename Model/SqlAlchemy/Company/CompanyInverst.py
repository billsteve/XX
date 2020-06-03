#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/12 17:10
# @Email     : billsteve@126.com
# @Des       : 
# @File        : CompanyInverst
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyInvest(Base, BaseModel):
    __tablename__ = 'company_invest'

    id = Column(INTEGER(11), primary_key=True)
    invest_id = Column(INTEGER(11))
    invest_to_id = Column(INTEGER(11))
    CompanyCode = Column(String(255))
    Percent = Column(String(255))
    PercentTotal = Column(String(255))
    Level = Column(INTEGER(11))
    Org = Column(INTEGER(11))
    ShouldCapi = Column(String(255))
    StockRightNum = Column(String(255))
    DetailCount = Column(INTEGER(11))
    DetailList = Column(String(255))
    ShortStatus = Column(String(255))
    is_del = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.CompanyCode = kw.get("CompanyCode", None)
        self.DetailCount = kw.get("DetailCount", None)
        self.DetailList = kw.get("DetailList", None)
        self.Level = kw.get("Level", None)
        self.Org = kw.get("Org", None)
        self.Percent = kw.get("Percent", None)
        self.PercentTotal = kw.get("PercentTotal", None)
        self.ShortStatus = kw.get("ShortStatus", None)
        self.ShouldCapi = kw.get("ShouldCapi", None)
        self.StockRightNum = kw.get("StockRightNum", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.invest_id = kw.get("invest_id", None)
        self.invest_to_id = kw.get("invest_to_id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)

    def getInvestRelation(self, invest_id, invest_to_id, session):
        return session.query(CompanyInvest.id).filter(CompanyInvest.invest_id == invest_id, CompanyInvest.invest_to_id == invest_to_id).limit(1).all()


if __name__ == '__main__':
    createInitFunction(CompanyInvest)
