#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 18:20
# @Author   : Peter
# @Des       : 
# @File        : DictHelper
# @Software: PyCharm
import XX.List.ListHelper


class DictHelper():
    @staticmethod
    def sortedDictKey(d):
        return dict(sorted(d.items(), key=lambda k: k[0]))

    @staticmethod
    def sortedDictValue(d):
        return dict(sorted(d.items(), key=lambda k: k[1], reverse=True))

    # 通过v获取k
    @staticmethod
    def getKeyByValue(d, v):
        for key, val in d.items():
            if str(val).lower() == v.lower():
                return key

    @staticmethod
    def decodeV(d, coding="utf-8"):
        dd = {}
        for k, v in d.items():
            if type(v) == dict:
                dd[k] = DictHelper.decodeV(v, coding)
            elif type(v) == bytes:
                dd[k] = str(v.decode(coding))
            elif type(v) == list or type(v) == tuple:
                dd[k] = XX.List.ListHelper.decodeV((list(v), coding))
            else:
                dd[k] = v
        return dd


if __name__ == "__main__":
    pass
