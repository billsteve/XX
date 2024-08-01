# -*- coding: utf-8 -*-

def get_hbase_conn_cfg(**kw):
    d = dict()
    d["host"] = kw.get("host", "localhost")
    # d["username"] = kw.get("username", None)
    # d["password"] = kw.get("pwd", None)
    d["port"] = kw.get("port", 9090)
    d["table"] = kw.get("table", "default")
    return d
