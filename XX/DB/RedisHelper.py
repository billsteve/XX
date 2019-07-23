# -*- encoding:utf8 -*-
import redis


class RedisHelper(object):
    pool = None
    host = None
    db = 0

    @staticmethod
    def getRedisConnect(host="127.0.0.1", port=6379, db=0, pwd=None, decode_responses=True):
        if RedisHelper.pool and RedisHelper.db == db and RedisHelper.host == host:
            return redis.Redis(connection_pool=RedisHelper.pool, decode_responses=decode_responses)
        else:
            RedisHelper.db = db
            try:
                RedisHelper.pool = redis.ConnectionPool(host=host, port=port, db=db, password=pwd, decode_responses=decode_responses)
                return redis.Redis(connection_pool=RedisHelper.pool, decode_responses=decode_responses)
            except:
                pass

    @staticmethod
    def getRedisInstance(host="127.0.0.1", port=6379, db=0, decode_responses=True):
        try:
            return redis.Redis(host=host, db=db, port=port, decode_responses=decode_responses)
        except:
            pass

    @staticmethod
    def getRedisConnectByCfg(cfg):
        return RedisHelper.getRedisConnect(**cfg)


if __name__ == "__main__":
    for i in range(5):
        r = RedisHelper.getRedisConnect(db=0, pwd="123")
        print(id(RedisHelper.pool))
    print("---" * 10)
    for i in range(5):
        r = RedisHelper.getRedisConnect(db=1)
        print(id(RedisHelper.pool))
    print("---" * 10)
    for i in range(5):
        r = RedisHelper.getRedisConnect(db=2)
        print(id(RedisHelper.pool))
    print("---" * 10)
    for i in range(5):
        r = RedisHelper.getRedisConnect(db=3)
        print(id(RedisHelper.pool))
