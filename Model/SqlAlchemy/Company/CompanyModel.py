#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/8/17 0:29
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Company.py
# @Software : PyCharm
from sqlalchemy import Column, Integer, Index, String, Text, or_
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import *

Base = declarative_base()
metadata = Base.metadata


class CompanyModel(Base, BaseModel):
    __tablename__ = 'company'
    __table_args__ = (
        Index('wy', 'NBXH', 'REGNO', unique=True),
    )

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    ADDR = Column(String(255))
    ANADDR = Column(String(255))
    ENTTYPE = Column(String(255))
    ENTTYPENAME = Column(String(255))
    HIGHLIGHTTITLE = Column(String(255))
    INVOPT = Column(String(255))
    JYFW = Column(Text(collation='utf8mb4_unicode_ci'))
    NBXH = Column(String(80), index=True)
    PRIPID = Column(String(255))
    QYBM = Column(String(255))
    QYWZ = Column(String(255))
    REGNO = Column(String(80), index=True)
    REGSTATECODE = Column(String(255))
    REGSTATE_CN = Column(String(255))
    REGUNIT = Column(String(255))
    REGUNITNAME = Column(String(255))
    SQ = Column(String(255))
    S_EXT_NODENUM = Column(String(255))
    TEL = Column(String(255))
    UBINDTYPE = Column(String(255))
    UBINDTYPENAME = Column(String(255))
    UNITCODE = Column(String(255))
    UNITNAME = Column(String(255))
    XZQHBM = Column(String(255))
    reg_time = Column(Integer)
    is_del = Column(Integer)
    u_ts = Column(Integer)
    c_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.ADDR = kw.get("ADDR", None)
        self.ANADDR = kw.get("ANADDR", None)
        self.company_id = kw.get("company_id", None)
        self.ENTTYPE = kw.get("ENTTYPE", None)
        self.ENTTYPENAME = kw.get("ENTTYPENAME", None)
        self.HIGHLIGHTTITLE = kw.get("HIGHLIGHTTITLE", None)
        self.INVOPT = kw.get("INVOPT", None)
        self.JYFW = kw.get("JYFW", None)
        self.NBXH = kw.get("NBXH", None)
        self.PRIPID = kw.get("PRIPID", None)
        self.QYBM = kw.get("QYBM", None)
        self.QYWZ = kw.get("QYWZ", None)
        self.REGNO = kw.get("REGNO", None)
        self.REGSTATECODE = kw.get("REGSTATECODE", None)
        self.REGSTATE_CN = kw.get("REGSTATE_CN", None)
        self.REGUNIT = kw.get("REGUNIT", None)
        self.REGUNITNAME = kw.get("REGUNITNAME", None)
        self.SQ = kw.get("SQ", None)
        self.S_EXT_NODENUM = kw.get("S_EXT_NODENUM", None)
        self.TEL = kw.get("TEL", None)
        self.UBINDTYPE = kw.get("UBINDTYPE", None)
        self.UBINDTYPENAME = kw.get("UBINDTYPENAME", None)
        self.UNITCODE = kw.get("UNITCODE", None)
        self.UNITNAME = kw.get("UNITNAME", None)
        self.XZQHBM = kw.get("XZQHBM", None)
        self.c_ts = kw.get("c_ts", None)
        self.reg_time = kw.get("reg_time", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.u_ts = kw.get("u_ts", None)

    @staticmethod
    def getByINVOPT(name, session):
        return session.query(CompanyModel).filter(CompanyModel.INVOPT == name).limit(1).all()

    @staticmethod
    def getByRegnoOrNbxh(regno, nbxh, session):
        return session.query(CompanyModel).filter(or_(CompanyModel.REGNO == regno, CompanyModel.NBXH == nbxh)).limit(1).all()

    @staticmethod
    def getByRegno(regno, session):
        return session.query(CompanyModel).filter(CompanyModel.REGNO == regno).all()

    @staticmethod
    def getByNBXH(nbxh, session):
        return session.query(CompanyModel).filter(CompanyModel.NBXH == nbxh).all()


if __name__ == '__main__':
    createInitFunction(CompanyModel)
