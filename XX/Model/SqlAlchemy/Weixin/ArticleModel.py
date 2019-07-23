#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/1/5 23:37
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Article.py
# @Des         : 
# @Software : PyCharm
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base
import XX.Model.SqlAlchemy.BaseModel as BM

Base = declarative_base()
metadata = Base.metadata


class ArticleModel(Base, BM.BaseModel):
    __tablename__ = 'article'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(300), server_default=text("''"))
    article_url = Column(String(300), server_default=text("''"))
    cover_url = Column(String(200), server_default=text("''"))
    description = Column(String(200), server_default=text("''"))
    publish_time = Column(DateTime)
    wx_id = Column(INTEGER(11), server_default=text("'0'"))
    read_count = Column(INTEGER(11), server_default=text("'0'"))
    like_count = Column(INTEGER(11), server_default=text("'0'"))
    comment_count = Column(INTEGER(11), server_default=text("'0'"))
    weixin_url = Column(String(300), server_default=text("''"))
    read_more_url = Column(String(300), server_default=text("''"))
    msg_index = Column(INTEGER(11), server_default=text("'0'"))
    copyright_stat = Column(INTEGER(1), server_default=text("'0'"))
    qunfa_id = Column(INTEGER(30), server_default=text("'0'"))
    type = Column(INTEGER(11), server_default=text("'0'"))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.article_url = kw.get("article_url", None)
        self.comment_count = kw.get("comment_count", None)
        self.copyright_stat = kw.get("copyright_stat", None)
        self.cover_url = kw.get("cover_url", None)
        self.create_ts = kw.get("create_ts", None)
        self.description = kw.get("description", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.like_count = kw.get("like_count", None)
        self.metadata = kw.get("metadata", None)
        self.msg_index = kw.get("msg_index", None)
        self.publish_time = kw.get("publish_time", None)
        self.qunfa_id = kw.get("qunfa_id", None)
        self.read_count = kw.get("read_count", None)
        self.read_more_url = kw.get("read_more_url", None)
        self.title = kw.get("title", None)
        self.type = kw.get("type", None)
        self.update_ts = kw.get("update_ts", None)
        self.weixin_url = kw.get("weixin_url", None)
        self.wx_id = kw.get("wx_id", None)


if __name__ == '__main__':
    BM.createInitFunction(ArticleModel)
