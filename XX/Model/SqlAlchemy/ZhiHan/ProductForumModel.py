#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:39
# @Author   : Peter
# @Des       : 
# @File        : ProductForum
# @Software: PyCharm
from sqlalchemy import Column, Integer, Index, String, Text
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class ProductForum(Base, BaseModel):
    __tablename__ = 'product_forum'
    __table_args__ = (
        Index('wy', 'product_id', 'forum_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    forum_id = Column(Integer, nullable=False)
    url = Column(String(512), nullable=False)
    forum_name = Column(String(512), nullable=False)
    product_name = Column(String(512), nullable=False)
    forum_car_name = Column(String(512), nullable=False)
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.forum_id = kw.get("forum_id", None)
        self.id = kw.get("id", None)
        self.meta_data = kw.get("meta_data", None)
        self.product_id = kw.get("product_id", None)
        self.product_name = kw.get("product_name", None)
        self.forum_name = kw.get("forum_name", None)
        self.forum_car_name = kw.get("forum_car_name", None)
        self.url = kw.get("url", None)
        self.update_ts = kw.get("update_ts", None)
        self.is_del = kw.get("is_del", None)
        self.create_ts = kw.get("create_ts", None)

    @staticmethod
    def getForumUrlsByForumId(forum_id, session):
        return session.query(ProductForum).filter(ProductForum.forum_id == forum_id).all()

    @staticmethod
    def getForumUrlByProductId(product_id, session):
        return session.query(ProductForum).filter(ProductForum.product_id == product_id).all()

    @staticmethod
    def getForumUrlByProductAndForum(product_id, forum_id, session):
        return session.query(ProductForum).filter(ProductForum.product_id == product_id, ProductForum.forum_id == forum_id).all()
