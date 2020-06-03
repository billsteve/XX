#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/25 16:53
# @File           : UserItemModel
# @Des           : 
# @Email        : billsteve@126.com
import XX.Model.SqlAlchemy.BaseModel as BM
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserItem(Base, BM.BaseModel):
    __tablename__ = 'user_items'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11))
    item_name = Column(String(60))
    item_content = Column(String(255))
    is_del = Column(TINYINT(1))
    create_ts = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.item_content = kw.get("item_content", None)
        self.item_name = kw.get("item_name", None)
        self.metadata = kw.get("metadata", None)
        self.uid = kw.get("uid", None)
        self.update_ts = kw.get("update_ts", None)


if __name__ == '__main__':
    BM.createInitFunction(UserItem)
