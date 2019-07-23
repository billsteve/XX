#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time        : 2018/7/4 16:09
# @Email       : billsteve@126.com
# @File          : BuiltinFunctions.py
# @Software  : PyCharm
# 重写内部方法
import copy
import time

import XX.Date.DatetimeHelper as dt


def print_function(s, flush=True, *arg, **kw):
    ts = int(kw.get("ts", 0))
    if "ts" in kw:
        kw.pop("ts")
    print(s, flush=flush, *arg, **kw)
    time.sleep(ts)


def printNoEnd(s, flush=True, end="", *arg, **kw):
    print_function(s, flush=flush, end=end, *arg, **kw)


def printBlankEnd(s, flush=True, end=" ", *arg, **kw):
    printNoEnd(s, flush=flush, end=end, *arg, **kw)


def printFromHead(s, **kw):
    printNoEnd("\r" + dt.GetNowTime() + "\t" + str(s), **kw)


if __name__ == '__main__':
    print()