# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class GpInfo(Base, BaseModel):
    __tablename__ = 'gp_info'

    id = Column(INTEGER(11), primary_key=True)
    url = Column(String(255, 'utf8mb4_unicode_ci'))
    encrypt_url = Column(String(255, 'utf8mb4_unicode_ci'))
    title = Column(String(255, 'utf8mb4_unicode_ci'))
    source_url = Column(String(255, 'utf8mb4_unicode_ci'))
    html = Column(Text(collation='utf8mb4_unicode_ci'))
    context = Column(Text(collation='utf8mb4_unicode_ci'))
    is_del = Column(TINYINT(1))
    create_ts = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.html = kw.get("html", None)
        self.context = kw.get("context", None)
        self.create_ts = kw.get("create_ts", None)
        self.encrypt_url = kw.get("encrypt_url", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.source_url = kw.get("source_url", None)
        self.title = kw.get("title", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)


if __name__ == '__main__':
    createInitFunction(GpInfo)
