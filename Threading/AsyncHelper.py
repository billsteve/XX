# -*- coding: utf-8 -*-
import time
from threading import Thread


def thread_call(fn):
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper


class Test:
    def __index__(self):
        pass

    @staticmethod
    @thread_call
    def aa():
        print(int(time.time()))
        time.sleep(2)
        print(int(time.time()))
        return {"k", "v"}


if __name__ == '__main__':
    l = []
    for url in range(10):
        r = Test.aa()
        print(r)
    print(l)
