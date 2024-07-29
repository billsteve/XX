# -*- coding: utf-8 -*-
import functools


def get_redis_conn_cfg(**kw):
    d = dict()
    d["host"] = kw.get("host", "localhost")
    d["password"] = kw.get("password", None)
    d["port"] = kw.get("port", 6379)
    d["db"] = kw.get("db", 0)
    d["decode_responses"] = kw.get("decode_responses", True)
    return d


local = functools.partial(get_redis_conn_cfg, host="localhost", password="DRsXT5ZJ6Oi55LPQ", db=0)
