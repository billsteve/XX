#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/12/23 16:38
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : CompanyEmployeeModel.py
# @Des         : 
# @Software : PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyEmployee(Base, BaseModel):
    __tablename__ = 'company_employee'

    id = Column(INTEGER(11), primary_key=True)
    com_id = Column(INTEGER(11))
    web_key = Column(String(255, 'utf8mb4_unicode_ci'))
    Name = Column(String(255, 'utf8mb4_unicode_ci'))
    person_id = Column(INTEGER(11))
    Job = Column(String(255, 'utf8mb4_unicode_ci'))
    CerNo = Column(String(255, 'utf8mb4_unicode_ci'))
    ScertName = Column(String(255, 'utf8mb4_unicode_ci'))
    is_del = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.CerNo = kw.get("CerNo", None)
        self.Job = kw.get("Job", None)
        self.Name = kw.get("Name", None)
        self.ScertName = kw.get("ScertName", None)
        self.com_id = kw.get("com_id", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.person_id = kw.get("person_id", None)
        self.update_ts = kw.get("update_ts", None)
        self.web_key = kw.get("web_key", None)


if __name__ == '__main__':
    createInitFunction(CompanyEmployee)
