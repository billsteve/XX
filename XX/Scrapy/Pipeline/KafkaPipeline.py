#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 放到Kakfa队列
import json

import XX.HTML.HtmlHelper as chtml
import XX.BuiltinFunctions as bf
from pykafka import KafkaClient


class KafkaPipeline(object):
    def __init__(self):

        self.client = KafkaClient(hosts="LOCALHOST" + ":6667")

    def process_item(self, item, spider):
        topic = self.client.topics[spider.name]
        producer = topic.get_producer()
        # 数据处理
        item = chtml.parseDict(item)
        json_str = json.dumps(item, ensure_ascii=False)
        producer.produce(json_str)
        bf.print_from_head(spider.name + "\tAdd kafka")
        return item
