# -*- coding: utf-8 -*-
from hashlib import md5


class SimpleHash(object):
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return (self.cap - 1) & ret


class BloomFilter(object):

    def __init__(self, conn=None, block_num=1, key='bf'):
        """
        :param block_num: one block_num for about 90,000,000; if you have more strings for filtering, increase it.
        :param key: the key's name in Redis
        """
        self.redis_conn = conn
        # <<表示二进制向左移动位数，比如2<<2,2的二进制表示000010，向左移2位，就是001000，就是十进制的8
        self.bit_size = 1 << 31  # Redis的String类型最大容量为512M，现使用256M
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.key = "B_" + key + "_"
        self.block_num = block_num
        self.hash_func = []
        for seed in self.seeds:
            self.hash_func.append(SimpleHash(self.bit_size, seed))

    def is_exists(self, str_input):
        if not str_input:
            return False
        m5 = md5()
        m5.update(str_input.encode("utf-8"))
        str_input = m5.hexdigest()
        ret = True
        name = self.key + str(int(str_input[0:2], 16) % self.block_num)
        for f in self.hash_func:
            loc = f.hash(str_input)
            ret = ret & self.redis_conn.getbit(name, loc)
        return ret

    def add(self, str_input):
        if BloomFilter.is_exists(self, str_input):
            return 0
        m5 = md5()
        m5.update(str_input.encode("utf-8"))
        str_input = m5.hexdigest()
        name = self.key + str(int(str_input[0:2], 16) % self.block_num)
        for f in self.hash_func:
            loc = f.hash(str_input)
            self.redis_conn.setbit(name, loc, 1)
        return 1


if __name__ == '__main__':
    """ 第一次运行时会显示 not exists!，之后再运行会显示 exists! """
    from .DB.RedisHelper import *

    conn_redis = RedisHelper.get_redis_connect("localhost", password=None, db=0)
    bf = BloomFilter(conn_redis)
    if bf.is_exists('http://www.baidu.com'):  # 判断字符串是否存在
        print('exists!')
    else:
        print('not exists!')
        bf.add('http://www.baidu.com')
