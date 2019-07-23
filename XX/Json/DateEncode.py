#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/5/13 13:56
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : DateEncode.py
# @Des         : 
# @Software : PyCharm
import datetime
import json
from datetime import date


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
