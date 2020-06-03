#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/19 17:30
# @Author   : Peter
# @Des       : 
# @File        : InfoForumCarUrl
# @Software: PyCharm
# coding: utf-8
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from XX.Model.SqlAlchemy.BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class InfoForumCarUrlModel(Base, BaseModel):
    __tablename__ = 'info_forum_car_url'

    id = Column(Integer, primary_key=True)
    forum_id = Column(Integer)
    car_name = Column(String(255))
    url = Column(String(255))
    is_del = Column(Integer)
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.car_name = kw.get("car_name", None)
        self.create_ts = kw.get("create_ts", None)
        self.forum_id = kw.get("forum_id", None)
        self.getByFromId = kw.get("getByFromId", None)
        self.getByFromIdAndMod = kw.get("getByFromIdAndMod", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)

    @staticmethod
    def getByForumidAndName(forum_id, car_name, session):
        return session.query(InfoForumCarUrlModel).filter(InfoForumCarUrlModel.forum_id == forum_id, InfoForumCarUrlModel.car_name == car_name).all()

    @staticmethod
    def searchByForumidAndName(forum_id, car_name, session):
        infos = InfoForumCarUrlModel.getByForumidAndName(forum_id, car_name, session)
        if not infos:
            return session.query(InfoForumCarUrlModel) \
                .filter(InfoForumCarUrlModel.forum_id == forum_id, InfoForumCarUrlModel.car_name.like("%" + str(car_name) + "%")) \
                .all()


if __name__ == '__main__':
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(InfoForumCarUrlModel):
        if not (str(k).startswith("_") or isinstance(getattr(InfoForumCarUrlModel, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}", None)""".format(attr=k))
