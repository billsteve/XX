#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:38
# @Author   : Peter
# @Des       : 
# @File        : Product
# @Software: PyCharm
from XX.Model.SqlAlchemy.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Product(Base, BaseModel):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    logo = Column(String(255))

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.logo = kw.get("logo", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
