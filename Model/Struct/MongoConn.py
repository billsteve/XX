# -*- coding: utf-8 -*-


def get_mongo_conn_cfg(**kw):
    d = dict()
    d["host"] = kw.get("host", "localhost")
    # d["username"] = kw.get("username", None)
    # d["password"] = kw.get("pwd", None)
    d["port"] = kw.get("port", 27017)
    return d

# ubuntu_cfg = get_mongo_conn_cfg(host="192.168.1.44")
# zhihan00_cfg = get_mongo_conn_cfg(host="192.168.1.50")
