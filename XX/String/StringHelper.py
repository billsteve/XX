#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/24 13:46
# @Author   : Peter
# @Des       : 
# @File        : StringHelper
# @Software: PyCharm
import string


def bytes2str(l):
    if type(l) == bytes:
        return l.decode("utf-8")
    elif type(l) == list or type(l) == tuple:
        res = []
        for one in list(l):
            res.append(bytes2str(one))
        return res
    elif type(l) == dict:
        res = {}
        for k, v in l.items():
            res[k] = bytes2str(v)
        return res
    elif type(l) == str:
        return l
    else:
        return l


def str2int(s):
    try:
        return int(s)
    except:
        return


# 获取字符的数量
def get_letter_count(s):
    num = 0
    for c in s:
        # 英文
        if c in string.ascii_letters:
            num += 1
    return num


# 获取汉字数量
def get_zh_count(s):
    num = 0
    for c in s:
        # 英文
        if c.isalpha() and c not in string.ascii_letters:
            num += 1
    return num


if __name__ == '__main__':
    s = "我  s 是你的bbaba!"
    print(get_zh_count(s))
    pass
