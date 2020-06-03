#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/10/30 19:27
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : QcmNewModel.py
# @Software : PyCharm
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class QcmNewModel(Base, BaseModel):
    __tablename__ = 'qcm_new'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    crawl_ts = Column(Integer)
    url = Column(String(120))
    is_del = Column(TINYINT(1))
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.crawl_ts = kw.get("crawl_ts", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)

    @staticmethod
    def addQcm(data, session):
        name = data.get("name")
        if name:
            exists = QcmNewModel.getByName(name, session)
        else:
            return 0
        if not exists:
            qcm = QcmNewModel(**data)
            QcmNewModel.addModel(qcm, session)
            return qcm.id
        return exists[0].id


if __name__ == '__main__':
    createInitFunction(QcmNewModel)
