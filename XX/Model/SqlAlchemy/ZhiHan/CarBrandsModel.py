#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/14 11:21
# @Author   : Peter
# @Site       : 
# @File        : CarBrands.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class CarBrandsModel(Base, BaseModel):
    __tablename__ = 'car_brands'

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer)
    brands_web_id = Column(Integer, unique=True)
    name = Column(String(255), index=True)
    brandsIsInlet = Column(String(10))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __init__(self, *arg, **kw):
        self.brand_id = kw.get("brand_id", None)
        self.brandsIsInlet = kw.get("brandsIsInlet", None)
        self.brands_web_id = kw.get("brands_web_id", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getBrandsByWebId(web_id, session):
        return session.query(CarBrandsModel).filter(CarBrandsModel.brands_web_id == web_id).all()
