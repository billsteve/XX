#!/usr/bin/python3
# -*- coding:utf-8 -*-
import hashlib
import os

from logzero import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .Date.DatetimeHelper import *


def get_session(host="localhost", user="root", password="123456", port="3306", charset="utf-8", db="test", *arg, **kw):
    global session
    if session:
        return session
    else:
        driver = kw.get("driver", "pymysql")
        mysql_url = 'mysql+' + driver + '://' + user + ":" + password + "@" + host + ":" + str(port) + "/" + str(
            db) + "?charset=" + charset.replace("-", "") + "&autocommit=true"
        engine = create_engine(mysql_url, encoding="utf8", *arg, **kw)
        session = sessionmaker(bind=engine)()
        return session


def get_md5_name(hash_string):
    md5_str = hashlib.new("md5", hash_string.encode("utf-8")).hexdigest()
    return md5_str[0] + os.sep + md5_str[1] + os.sep + md5_str[2] + os.sep + md5_str


def writefile(filename, text, mode="w"):
    f = open(filename, mode, encoding="UTF-8")
    f.write(text)
    f.close()
    pass


####################################################
import pymysql

global_conn = None


def connect(host="localhost", user="root", password="123456", port=3306, charset="utf8", db="test",
            mysql_timeout=5000, use_global=False):
    global global_conn
    if global_conn:
        logger.info("使用全局连接")
        return global_conn

    try_times = 3
    conn = None
    for i in range(try_times):
        try:
            conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset,
                                   connect_timeout=mysql_timeout, autocommit=1)
            break
        except Exception as e:
            import traceback
            traceback.print_exc()
            logger.info("data connection error,%s" % e)
        finally:
            pass
    if use_global:
        global_conn = conn
        logger.info("首次连接")
    return conn


def close(conn):
    global global_conn
    if global_conn:
        return False
    else:
        pass
    try:
        conn.close()
    except Exception as e:
        logger.info("data shutdown error,%s" % e)
    finally:
        pass

    return True


def insert(conn, sql):
    global global_conn
    conn = global_conn if global_conn else conn
    try:
        conn.ping()
        cur = conn.cursor()
        cur.execute(sql)
        id = int(conn.insert_id())
        conn.commit()
    except Exception as e:
        logger.info("Mysql Insert Error: %s, %s" % (e, sql))
        logger.info("data insert error")
        conn.rollback()
        id = -1
    finally:
        cur.close()
    return id


def lastrowid(conn):
    global global_conn
    conn = global_conn if global_conn else conn
    try:
        conn.ping()
        cur = conn.cursor()
        id = int(cur.lastrowid)
    except Exception as e:
        logger.info("data last_id error,%s" % e)
        id = -1
    finally:
        cur.close()
    return id


def update(conn, sql):
    global global_conn
    conn = global_conn if global_conn else conn
    try:
        conn.ping()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        result = cur.execute(sql)
        conn.commit()
    except Exception as e:
        logger.info(" ========== Mysql Update Error: %s" % e)
        writefile("mysql-err.log", get_now_time() + sql + "\n\n\n", mode="a")
        conn.ping()
        conn.rollback()
        result = False
    finally:
        cur.close()
    return result


def fetch(conn, sql):
    global global_conn
    conn = global_conn if global_conn else conn
    try:
        conn.ping()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        rs = cur.execute(sql)
        list = cur.fetchmany(rs)
        conn.commit()
    except Exception as e:
        logger.info("Mysql Fetch Error: %s" % e)
        conn.rollback()
        conn.ping()
        list = None
    finally:
        cur.close()
    return list


def make_insert_sql(table: str, data: dict, updates: dict, replace=1) -> str:
    columns_sql = ""
    values_sql = ""
    updates_sql = ""
    for key in data.keys():
        if data[key]:
            data[key] = pymysql.escape_string(str(data[key]))
        columns_sql = columns_sql + "`" + key + "`,\t"
        if data[key] is not None:
            values_sql = values_sql + "'" + str(data[key]) + "',\t"
        else:
            values_sql = values_sql + "null,\t"

        if replace:
            # 覆盖
            if key in updates:
                if data[key] is not None:
                    updates_sql = updates_sql + "`" + key + "` = '" + str(data[key]) + "',\t"
                else:
                    updates_sql = updates_sql + "`" + key + "` = null,\t"
        else:
            # 补充
            if key in updates:
                if data[key]:
                    updates_sql = updates_sql + "`" + key + f"` =  CASE WHEN {key}  IS NOT NULL THEN {key} ELSE '" + str(
                        data[key]) + "'  END,\t"

    columns_sql = columns_sql[:-2]
    values_sql = values_sql[:-2]
    if len(updates_sql) > 2:
        updates_sql = updates_sql[:-2]
    return f"INSERT INTO `{table}`( {columns_sql} )VALUES({values_sql}) ON DUPLICATE KEY UPDATE {updates_sql} ;\t"
