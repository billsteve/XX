#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:53
# @Author   : Peter
# @Des       : 
# @File        : SqlAlchemyHelper
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SqlAlchemyHelper():

    @staticmethod
    def get_session(host="localhost", user="root", pwd="root", port=3306, charset="utf-8", db="test", *arg, **kw):
        driver = kw.get("driver", "pymysql")
        mysql_url = 'mysql+' + driver + '://' + user + ":" + pwd + "@" + host + ":" + str(port) + "/" + str(db) + "?charset=" + charset.replace("-", "")
        engine = create_engine(mysql_url, encoding=charset, pool_size=10, max_overflow=20, *arg, **kw)
        return sessionmaker(bind=engine)()

    @staticmethod
    def get_session_by_cfg(cfg):
        return SqlAlchemyHelper.get_session(**cfg)


if __name__ == "__main__":
    import XX.Model.Struct.MysqlConn as cfg

    sa = SqlAlchemyHelper()
    mcfg = cfg.ubuntu_cfg
    mcfg["db"] = "weibo"
    print(mcfg)
    session = sa.get_session_by_cfg(mcfg)
    print(session)
