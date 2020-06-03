#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/20 23:56
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Engine.py
# @Software : PyCharm
import XX.Multiprocess.Callback as cb


def apply_async_function(pro_num, fun, para=None, error_callback=cb.msg):
    from multiprocessing import Pool
    pool = Pool(pro_num)
    for i in range(pro_num):
        if para:
            if isinstance(para, tuple) or isinstance(para, list):
                ppara = list(para)
                ppara.append(i)
                pool.apply_async(fun, args=ppara, error_callback=error_callback)
            if isinstance(para, dict):
                para["pro_num"] = i
                pool.apply_async(fun, kwds=para, error_callback=error_callback)
        else:
            pool.apply_async(fun, (i,), error_callback=error_callback)
    pool.close()
    pool.join()
