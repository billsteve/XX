#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/11 9:44
# @Email     : billsteve@126.com
# @Des       : 
# @File        : AsyncHelper
# @Software: PyCharm
from threading import Thread
import time


def async_call(fn):
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper


class Test:
    def __index__(self):
        pass

    @staticmethod
    @async_call
    def aa():
        print(int(time.time()))
        time.sleep(2)
        print(int(time.time()))


if __name__ == '__main__':
    Test.aa()
    Test.aa()
