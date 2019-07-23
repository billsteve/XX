#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/12/2 15:24
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Json2File.py
# @Des         : 
# @Software : PyCharm
import os
import XX.Date.DatetimeHelper as dt
import XX.File.FileHelper as uf
import json


def JsonCheckDecorator(func):
    def inner(*args, **kwargs):
        if kwargs.get("json_data") or args[0]:
            func(*args, **kwargs)
        else:
            print("No Json 2 DB " + "===" * 30)

    return inner


# json数据保存到对应文件夹
def Json2File(fp=None, *dargs, **dkargs):
    def dec_func(func):
        def inner(*args, **kwargs):
            if len(args) < 2:
                json_data = kwargs.get("json_data", None)
                spider = kwargs.get("spider", None)
                fp = kwargs.get("fp", None)
            else:
                json_data = args[0]
                spider = args[1]
                fp = args[3]
            if json_data:
                today = dt.GetToday().replace("-", "_")
                uf.FileHelper.mkdir(fp + spider)
                json.dump(json_data, open(fp + spider + os.sep + today + ".json", "a", encoding="utf-8"), ensure_ascii=False)
            return func(*args, **kwargs)  # 2

        return inner

    return dec_func


@JsonCheckDecorator
def test(json_data, mcfg):
    print("Ok" * 22)
    pass
