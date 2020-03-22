#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/30 14:53
# @File           : CacheHelper
# @Des           : 
# @Email        : billsteve@126.com
import os
import pickle

import XX.Encrypt.EncryptHelper as Enc
import XX.File.FileHelper as FH
import XX.Tools.BuiltinFunctions as BF
import XX.configs as cc
import happybase
from logzero import logger


# TODO:Rebuild(太不耦合)
def cache_file_2_hbase(root_path, hb_cfg, table_name, pro_num=0):
    conn_hbase = happybase.Connection(**hb_cfg)
    table = conn_hbase.table("crawl_" + table_name)
    for fp, fn in FH.FileHelper.getFileList(root_path):
        if not fn.startswith(cc.WORDS16[pro_num]):
            continue
        spider = fp.split(os.sep)[-4]
        response = pickle.load(open(fp + os.sep + fn, "rb"))
        row = spider + "_" + Enc.Encrypt.md5(response.url)
        if table.row(row):
            BF.print_from_head("Exists\t" + row)
            continue
        data = {
            "source:url": str(response.url),
            "source:status_code": str(response.status),
            "source:html": str(response.text),
            "source:type": "html",
            "source:size": str(len(response.text)),
            "source:encoding": response.encoding
        }
        table.put(row, data)
        logger.info(row)
