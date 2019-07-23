#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/21 23:07
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : LoadCache.py
# @Software : PyCharm
# 重新解析缓存文件，生成Item
import os
import pickle

import XX.File.FileHelper as uf


def ReloadCache(cache_rp):
    for fp, fn in uf.FileHelper.getFileList(cache_rp):
        yield pickle.load(open(fp + os.sep + fn, "rb"))
