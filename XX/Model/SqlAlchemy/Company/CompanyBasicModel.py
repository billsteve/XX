#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/25 14:29
# @Author   : Peter
# @Des       : 
# @File        : CompanyBasicModel
# @Software: PyCharm
# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, Index, VARCHAR, or_
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyBasicModel(Base, BaseModel):
    __tablename__ = 'company_basic'
    __table_args__ = (
        Index('wy', 'no', 'creditno', unique=True),
    )

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    no = Column(VARCHAR(80), index=True)
    web_key = Column(VARCHAR(80), index=True)
    creditno = Column(VARCHAR(80), index=True)
    is_del = Column(Integer)
    u_ts = Column(Integer)
    c_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.c_ts = kw.get("c_ts", None)
        self.creditno = kw.get("creditno", None)
        self.get = kw.get("get", None)
        self.getAll = kw.get("getAll", None)
        self.getAllIds = kw.get("getAllIds", None)
        self.getByFromId = kw.get("getByFromId", None)
        self.getByFromIdAndMod = kw.get("getByFromIdAndMod", None)
        self.getByName = kw.get("getByName", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.web_key = kw.get("web_key", None)
        self.no = kw.get("no", None)
        self.u_ts = kw.get("u_ts", None)

    @staticmethod
    def getByNoOrCreditNo(no="", creditno="", session=None):
        return session.query(CompanyBasicModel).filter(or_(CompanyBasicModel.no == no, CompanyBasicModel.creditno == creditno)).limit(1).all()

    @staticmethod
    def updateComKey(id_, web_key, session):
        infos = session.query(CompanyBasicModel).filter(CompanyBasicModel.id == id_).update({CompanyBasicModel.web_key: web_key})
        session.commit()
        return infos

    @staticmethod
    def addBasic(data, session):
        if data.get("no"):
            exists = CompanyBasicModel.getByNo(data.get("no"), session)
        elif data.get("web_key"):
            exists = CompanyBasicModel.getByCreditNo(data.get("web_key"), session)
        elif data.get("creditno"):
            exists = CompanyBasicModel.getByCreditNo(data.get("creditno"), session)
        elif data.get("name"):
            exists = CompanyBasicModel.getByName(data.get("name"), session)
        else:
            return None
        if not exists:
            basic = CompanyBasicModel(**data)
            CompanyBasicModel.addModel(basic, session)
            return basic.id
        return exists[0].id


class TestModel(Base, BaseModel):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))


if __name__ == '__main__':
    createInitFunction(TestModel)
