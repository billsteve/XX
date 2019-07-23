# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Img(Base, BaseModel):
    __tablename__ = 'img'

    id = Column(INTEGER(11), primary_key=True)
    web_id = Column(INTEGER(11))
    picture_url = Column(String(255))

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.metadata = kw.get("metadata", None)
        self.picture_url = kw.get("picture_url", None)
        self.web_id = kw.get("web_id", None)


class Title(Base, BaseModel):
    __tablename__ = 'title'

    id = Column(INTEGER(11), primary_key=True)
    web_id = Column(INTEGER(11), unique=True)
    title = Column(String(255))

    def __init__(self, *arg, **kw):
        self.id = kw.get("id", None)
        self.metadata = kw.get("metadata", None)
        self.title = kw.get("title", None)
        self.web_id = kw.get("web_id", None)


if __name__ == '__main__':
    createInitFunction(Img)
    createInitFunction(Title)
