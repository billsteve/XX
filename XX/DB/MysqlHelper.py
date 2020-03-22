#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/17 11:09
# @File           : Mysql2Redis
# @Des           :
# @Email        : billsteve@126.com
import pymysql

from XX.List.ListHelper import ListHelper


class MysqlHelper:
    pool = None
    db = None
    host = None

    def __init__(self, host="127.0.0.1", user="root", password="root", db="test", port=3306, charset="utf8", **kw):
        self._conn = pymysql.connect(host, user, password, db, port=port, charset=charset.replace("-", ""))
        if kw.get("kv"):
            self.cur = self._conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            self.cur = self._conn.cursor()

    def query(self, sql, vals=None, cursor=None):
        self.cur.execute(sql, vals)
        res = ListHelper.decodeV(self.cur.fetchall())
        return res

    def execute(self, sql, vals=None, cursor=None, commit=True):
        res = self.cur.execute(sql, vals)
        if commit:
            self._conn.commit()
        return res

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def lastrowid(self):
        return self.cur.lastrowid

    def close(self):
        self._conn.close()

    def dispose(self, method="commit"):
        if method == "commit":
            self._conn.commit()
        else:
            self._conn.rollback()
        self.cur.close()
        self._conn.close()


class SqlHelper:

    # 根据字段和ddl语句查看哪个字段没有
    @staticmethod
    def get_less_columns(jd, ddl):
        t = set()
        for line in ddl.split("\n"):
            if line and line.find("`") >= 0:
                t.add(line.split("`")[1])
        return set(jd.keys()) - t

    # 根据ddl获取所有字段
    @staticmethod
    def get_columns_list(ddl):
        t = []
        for line in ddl.split("\n"):
            if line and line.find("`") >= 0:
                t.append(line.split("`")[1])
        return t

    # 根据字典获取建表语句
    @staticmethod
    def get_table_sql_by_dict(d, tb_name="tb_name", tb_comment="COMMENT"):
        s = "\n\nCREATE TABLE `{tb_name}` (\n`id` int(11) NOT NULL AUTO_INCREMENT,\n\n".format(tb_name=tb_name)
        for k, v in d.items():
            if type(v) in [int, float]:
                s += """\t`{key}` int(11) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            elif type(v) == list:
                s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            elif type(v) == dict:
                if v.get("id"):
                    s += """\t`{key}_web_id`  varchar(255) DEFAULT NULL,""".format(key=k) + "\n"
                    print(":WebWebWebWebWeb")
                else:
                    s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            else:
                s += """\t`{key}` varchar(255) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
        s += """
            `is_del` int(11) DEFAULT 0,
            `update_ts` int(11) DEFAULT NULL,
            `create_ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='{tb_comment}';""".format(tb_comment=tb_comment)
        print(s)

    # 根据dump文件获取所有表建表语句
    @staticmethod
    def get_tables_sql_by_sql_dump(fp):
        for line in open(fp, "r", encoding="utf-8"):
            if line.find("INSERT") >= 0 or line.find("--") >= 0 or line.find("/*") >= 0:
                continue
            print(line.strip())

    # 根据json生成sql
    @staticmethod
    def get_sql_by_dict(d, tb_name="tb_name", tb_comment="COMMENT"):
        s = "\n\nCREATE TABLE `{tb_name}` (\n`id` int(11) NOT NULL AUTO_INCREMENT,\n\n".format(tb_name=tb_name)
        for k, v in d.items():
            if type(v) in [int, float]:
                s += """\t`{key}` int(11) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            elif type(v) == list:
                s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            elif type(v) == dict:
                if v.get("id"):
                    s += """\t`{key}_web_id`  varchar(255) DEFAULT NULL,""".format(key=k) + "\n"
                    print(":WebWebWebWebWeb")
                else:
                    s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            else:
                s += """\t`{key}` varchar(255) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
        s += """
            `is_del` int(11) DEFAULT 0,
            `update_ts` int(11) DEFAULT NULL,
            `create_ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='{tb_comment}';""".format(tb_comment=tb_comment)
        print(s)

    @staticmethod
    def get_create_table_sql_by_sql_dump(fp):
        for line in open(fp, "r", encoding="utf-8"):
            if line.find("INSERT") >= 0 or line.find("--") >= 0 or line.find("/*") >= 0:
                continue
            print(line.strip())


class DDLHelper:
    # 根据json生成sql
    @staticmethod
    def get_sql_by_dict(d, tb_name="tb_name", tb_comment="COMMENT"):
        s = "\n\nCREATE TABLE `{tb_name}` (\n`id` int(11) NOT NULL AUTO_INCREMENT,\n\n".format(tb_name=tb_name)
        for k, v in d.items():
            if type(v) in [int, float]:
                s += """\t`{key}` int(11) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            elif type(v) == list:
                s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            elif type(v) == dict:
                if v.get("id"):
                    s += """\t`{key}_web_id`  varchar(255) DEFAULT NULL,""".format(key=k) + "\n"
                    print(":WebWebWebWebWeb")
                else:
                    s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
            else:
                s += """\t`{key}` varchar(255) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
        s += """
            `is_del` int(11) DEFAULT 0,
            `update_ts` int(11) DEFAULT NULL,
            `create_ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='{tb_comment}';""".format(tb_comment=tb_comment)
        print(s)

    @staticmethod
    def get_create_table_sql_by_sql_dump(fp):
        for line in open(fp, "r", encoding="utf-8"):
            if line.find("INSERT") >= 0 or line.find("--") >= 0 or line.find("/*") >= 0:
                continue
            print(line.strip())

    @staticmethod
    def del_redis_keys_by_prefix(prefix, conn):
        for key in conn.keys():
            if str(key).startswith(prefix):
                conn.delete(key)
                print(key)
