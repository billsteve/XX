#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time        : 2018/7/4 16:09
# @Email       : billsteve@126.com
# @File          : BuiltinFunctions.py
# @Software  : PyCharm
# 重写内部方法
import time

import XX.Date.DatetimeHelper as Dt


def print_function(s, flush=True, *arg, **kw):
    ts = int(kw.get("ts", 0))
    if "ts" in kw:
        kw.pop("ts")
    print(s, flush=flush, *arg, **kw)
    time.sleep(ts)


def print_no_end(s, flush=True, end="", *arg, **kw):
    print_function(s, flush=flush, end=end, *arg, **kw)


def print_blank_end(s, flush=True, end=" ", *arg, **kw):
    print_no_end(s, flush=flush, end=end, *arg, **kw)


def print_from_head(s, **kw):
    print_no_end("\r" + Dt.get_now_time() + "\t" + str(s), **kw)


def print_wait(ts=1, s=""):
    for t in range(ts):
        print_from_head(f"{s} Please Wait {ts - t}" + "." * t + "        ")
        time.sleep(1)


if __name__ == '__main__':
    print_wait(4, "有延时。")
