#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/22 13:25
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Tax.py
# @Software : PyCharm
from mongoengine import *


class Tax(Document):
    success = BooleanField(required=True)
    data = DictField(max_length=50)
    url = StringField(max_length=250)
    meta = {'collection': 'tax'}


if __name__ == '__main__':
    pass
