#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/14 11:22
# @Author   : Peter
# @Site       : 
# @File        : CarSeries.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class CarSeriesModel(Base, BaseModel):
    __tablename__ = 'car_series'

    id = Column(Integer, primary_key=True)
    brands_id = Column(Integer)
    series_web_id = Column(Integer, unique=True)
    name = Column(String(255), index=True)
    seriesAttribute = Column(String(10))
    series_logo = Column(String(255))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __init__(self, *arg, **kw):
        self.brands_id = kw.get("brands_id", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.seriesAttribute = kw.get("seriesAttribute", None)
        self.series_logo = kw.get("series_logo", None)
        self.series_web_id = kw.get("series_web_id", None)
        self.update_ts = kw.get("update_ts", None)

    @staticmethod
    def getBySeriesWebId(web_id, session):
        return session.query(CarSeriesModel).filter(CarSeriesModel.series_web_id == web_id).all()
