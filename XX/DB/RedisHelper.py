# -*- encoding:utf8 -*-
import redis


class RedisHelper(object):
    pool = None
    host = None
    db = 0

    @staticmethod
    def get_redis_connect(host="127.0.0.1", port=6379, db=0, password=None, decode_responses=True):
        if RedisHelper.pool and RedisHelper.db == db and RedisHelper.host == host:
            return redis.Redis(connection_pool=RedisHelper.pool, decode_responses=decode_responses)
        else:
            RedisHelper.db = db
            RedisHelper.pool = redis.ConnectionPool(host=host, port=port, db=db, password=password, decode_responses=decode_responses)
            return redis.Redis(connection_pool=RedisHelper.pool, decode_responses=decode_responses)

    @staticmethod
    def get_redis_instance(host="127.0.0.1", port=6379, db=0, decode_responses=True):
        return redis.Redis(host=host, db=db, port=port, decode_responses=decode_responses)

    @staticmethod
    def get_redis_connect_by_cfg(cfg):
        return RedisHelper.get_redis_connect(**cfg)
