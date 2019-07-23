#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/17 10:50
# @Email     : billsteve@126.com
# @Des       : 
# @File        : KafkaPipeline
# @Software: PyCharm
# 放到Kakfa队列
import json

import XX.HTML.HtmlHelper as chtml
import XX.Tools.BuiltinFunctions as bf
from pykafka import KafkaClient


class KafkaPipeline(object):
    def __init__(self):

        self.client = KafkaClient(hosts="LOCALHOST" + ":6667")

    def process_item(self, item, spider):
        topicdocu = self.client.topics[spider.name]
        producer = topicdocu.get_producer()
        # 数据处理
        item = chtml.parseDict(item)
        json_str = json.dumps(item, ensure_ascii=False)
        producer.produce(json_str)
        bf.printFromHead(spider.name + "\tAdd kafka")
        return item
