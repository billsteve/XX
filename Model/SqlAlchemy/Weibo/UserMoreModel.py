#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/25 17:56
# @File           : UserMoreModel
# @Des           : 
# @Email        : billsteve@126.com
import XX.Model.SqlAlchemy.BaseModel as BM
from sqlalchemy import Column, Float, String, Text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserMore(Base, BM.BaseModel):
    __tablename__ = 'user_more'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), unique=True)
    user_web_id = Column(INTEGER(11))
    wb_comment_avg = Column(Float(11, True))
    wb_like_avg = Column(Float(11, True))
    wb_share_avg = Column(Float(11, True))
    wb_count_avg_per_month = Column(Float(11, True))
    car_offical = Column(TINYINT(1))
    types = Column(String(255))
    actionlog_ext = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.actionlog_ext = kw.get("actionlog_ext", None)
        self.car_offical = kw.get("car_offical", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.types = kw.get("types", None)
        self.uid = kw.get("uid", None)
        self.user_web_id = kw.get("user_web_id", None)
        self.update_ts = kw.get("update_ts", None)
        self.wb_comment_avg = kw.get("wb_comment_avg", None)
        self.wb_count_avg_per_month = kw.get("wb_count_avg_per_month", None)
        self.wb_like_avg = kw.get("wb_like_avg", None)
        self.wb_share_avg = kw.get("wb_share_avg", None)

    @staticmethod
    def setAbout(uid, session):
        import time
        exists = UserMore.getIdByKV("uid", uid, session)
        if exists:
            res = UserMore.updateKV(uid, "car_offical", 1, session)
        else:
            ts = int(time.time())
            umm = UserMore(car_offical=1, uid=uid, create_ts=ts)
            UserMore.addModel(umm, session)
            res = id
        return res


if __name__ == '__main__':
    BM.createInitFunction(UserMore)
