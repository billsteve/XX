#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/21 23:07
# 重新解析缓存文件，生成Item
import os
import pickle

import XX.File.FileHelper as uf


def reload_cache(cache_rp):
    for fp, fn in uf.FileHelper.get_file_list(cache_rp):
        yield pickle.load(open(fp + os.sep + fn, "rb"))
