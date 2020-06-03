#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/2/18 15:03
# @File           : DMHelper
# @Des           : 
# @Email        : billsteve@126.com
import XX.Encrypt.EncryptHelper as Enc


def add_HBase(spider, url, html, project_name, conn, row=None):
    table = conn.connection.table("crawl_" + project_name)
    row = spider + "_" + Enc.Encrypt.md5(url) if not row else row
    if table.row(row):
        print("==Exists\t" + row)
        return -1
    data = {
        "source:url": str(url),
        "source:html": str(html),
        "source:type": "html",
        "source:size": str(len(html)),
    }
    conn.addRowColumn(row, data, table=table)
    return 1
