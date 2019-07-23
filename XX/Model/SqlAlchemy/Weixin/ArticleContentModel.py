#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/1/7 0:05
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : ArticleContent.py
# @Des         : 
# @Software : PyCharm
import XX.Model.SqlAlchemy.BaseModel as BM
from sqlalchemy import CHAR, Column, Text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ArticleContentModel(Base, BM.BaseModel):
    __tablename__ = 'article_content'

    id = Column(INTEGER(11), primary_key=True)
    article_id = Column(INTEGER(11))
    content = Column(Text)
    hash_key = Column(CHAR(32))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.article_id = kw.get("article_id", None)
        self.content = kw.get("content", None)
        self.create_ts = kw.get("create_ts", None)
        self.hash_key = kw.get("hash_key", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)


if __name__ == '__main__':
    BM.createInitFunction(ArticleContentModel)
