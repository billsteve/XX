# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Growing(Base, BaseModel):
    __tablename__ = 'growing'

    id = Column(INTEGER(11), primary_key=True)
    kw = Column(String(30))
    name = Column(String(180), unique=True)

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.kw = kw.get("kw", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)


if __name__ == '__main__':
    createInitFunction(Growing)
