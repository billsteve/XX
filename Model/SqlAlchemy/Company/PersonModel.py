#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/23 14:42
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : PersonModel.py
# @Software : PyCharm

from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PersonModel(Base, BaseModel):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    web_id = Column(Integer)
    web_key = Column(String(50))
    name = Column(String(50))
    image = Column(String(200))
    is_del = Column(Integer)
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.get = kw.get("get", None)
        self.getAll = kw.get("getAll", None)
        self.getAllIds = kw.get("getAllIds", None)
        self.getByFromId = kw.get("getByFromId", None)
        self.getByFromIdAndMod = kw.get("getByFromIdAndMod", None)
        self.getByName = kw.get("getByName", None)
        self.id = kw.get("id", None)
        self.image = kw.get("image", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.web_key = kw.get("web_key", None)
        self.update_ts = kw.get("update_ts", None)
        self.web_id = kw.get("web_id", None)

    @staticmethod
    def savePerson(data, session):
        web_id = data.get("web_id")
        web_key = data.get("web_key")
        if web_id:
            exists = PersonModel.getByKV("web_id", web_id, session)
        elif web_key:
            exists = PersonModel.getByWebKey(web_key, session)
        else:
            return
        if not exists:
            person = PersonModel(**data)
            PersonModel.addModel(person, session)
            return person.id
        return exists[0].id


if __name__ == '__main__':
    createInitFunction(PersonModel)
