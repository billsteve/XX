#!/usr/bin/python3
# -*- coding:utf-8 -*-
import hashlib
import os

from logzero import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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


def connect(host="localhost", user="root", password="123456", port="3306", charset="utf8", db="test",
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
        logger.info("Mysql Update Error: %s" % e)
        writefile("mysql-err.txt", sql + "\n", mode="a")
        logger.info("data update error")
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
        logger.info("data fetch error")
        conn.rollback()
        conn.ping()
        list = None
    finally:
        cur.close()
    return list


def make_insert_sql(table, data, updates, replace=1):
    columnssql = ""
    valuessql = ""
    updatessql = ""
    for key in data.keys():
        if data[key]:
            data[key] = pymysql.escape_string(str(data[key]))
        columnssql = columnssql + "`" + key + "`,\t"
        if data[key] is not None:
            valuessql = valuessql + "'" + str(data[key]) + "',\t"
        else:
            valuessql = valuessql + "null,\t"

        if replace:
            # 覆盖
            if key in updates:
                if data[key] is not None:
                    updatessql = updatessql + "`" + key + "` = '" + str(data[key]) + "',\t"
                else:
                    updatessql = updatessql + "`" + key + "` = null,\t"
        else:
            # 补充
            if key in updates:
                if data[key]:
                    updatessql = updatessql + "`" + key + f"` =  CASE WHEN {key}  IS NOT NULL THEN {key} ELSE '" + str(
                        data[key]) + "'  END,\t"

    sql = "INSERT INTO `#tablename#`( #columns# )VALUES( #values# ) ON DUPLICATE KEY UPDATE #updates# ;\t"
    columnssql = columnssql[:-2]
    valuessql = valuessql[:-2]
    if len(updatessql) > 2:
        updatessql = updatessql[:-2]
    sql = sql.replace("#tablename#", table)
    sql = sql.replace("#columns#", columnssql)
    sql = sql.replace("#values#", valuessql)
    sql = sql.replace("#updates#", updatessql)
    return sql


if __name__ == "__main__":
    data = {
        "a": 1,
        "b": None,
        "c": "hha"
    }
    sql = make_insert_sql("t", data, data, 0)
    print(sql)
