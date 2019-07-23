#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/14 11:19
# @Author   : Peter
# @Site       : 
# @File        : CarBrand.py
# @Software: PyCharm
from sqlalchemy import Column, String
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class CarBrandModel(Base, BaseModel):
    __tablename__ = 'car_brand'

    id = Column(Integer, primary_key=True)
    brand_web_id = Column(Integer, unique=True)
    name = Column(String(255), index=True)
    initials = Column(String(10))
    brand_logo = Column(String(255))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __init__(self, *arg, **kw):
        self.brand_logo = kw.get("brand_logo", None)
        self.brand_web_id = kw.get("brand_web_id", None)
        self.id = kw.get("id", None)
        self.initials = kw.get("initials", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.update_ts = kw.get("update_ts", None)
        self.is_del = kw.get("is_del", None)
        self.create_ts = kw.get("create_ts", None)

    @staticmethod
    def getByBrandWebId(web_id, session):
        infos = session.query(CarBrandModel).filter(CarBrandModel.brand_web_id == web_id).all()
        return infos[0] if infos else None
