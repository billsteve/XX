#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/14 16:09
import json
import os
import time

from logzero import logger
from thrift.transport import TSocket

import XX.DB.SqlAlchemyHelper as sa
import XX.Encrypt.EncryptHelper as enc
import XX.File.FileHelper as cf
import XX.HTML.HtmlHelper as chtml
import XX.Tools.BuiltinFunctions as bf


# File pipeline:放到今日文件中
class FilePipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.cacheFilePath = settings.get("FUN_CACHE_FILE_PATH")
        cls.settings = settings
        return cls()

    def process_item(self, item, spider):
        # 数据处理
        item = chtml.parseDict(item)
        today = time.strftime("%Y_%m_%d", time.localtime(int(time.time())))
        json_str = json.dumps(item, ensure_ascii=False)

        # 保存数据到文件
        file_path = FilePipeline.settings.get("ROOT_PATH_JSON") + spider.name + os.sep + today + ".json"
        cf.FileHelper.save_file(file_path, json_str + "\n")
        return item


# 放到MySQL数据库
class MysqlPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings
        cls.session = sa.SqlAlchemyHelper.get_session_by_cfg(cls.settings.get("MCFG"))
        return cls()

    def process_item(self, item, spider):
        import importlib
        module = importlib.import_module("Util.Json2Mysql", MysqlPipeline.settings.get("PROJECT_PATH"))
        if hasattr(module, spider.name):
            getattr(module, spider.name)(item, self.session)
        else:
            logger.info("No Json2Mysql function")
        return item


# 放到Mongo数据库
class MongoPipeline(object):
    def process_item(self, item, spider):
        return item


# 放到Kakfa队列
class KafkaPipeline(object):
    def __init__(self):
        from pykafka import KafkaClient
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


class HivePipeline(object):
    def process_item(self, item, spider):
        return item


class SparkPipeline(object):
    def process_item(self, item, spider):
        return item


class StormPipeline(object):
    def process_item(self, item, spider):
        return item


class HBasePipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings

    def __init__(self):
        self.transport = TSocket.TSocket(self.settings.get("HBASE_HOST", "localhost"), self.settings.get("HBASE_PORT", 9090))
        self.transport.open()
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(self.protocol)

        # 判断是否有表，没有则生成
        tables = self.client.getTableNames()
        self.table_name = "crawl_" + self.settings.get("PROJECT_NAME", self.settings.get("BOT_NAME", "crawl"))
        if self.table_name not in tables:
            source = ColumnDescriptor(name='source')
            data = ColumnDescriptor(name='data')
            self.client.createTable(self.table_name, [source, data])

    def process_item(self, item, spider):
        # 保存到crawl_project表中 spider_name+md5(url) rowkey中，data:json_str中
        # crawl_project >  spider_name+md5(url)  > data:json_str
        url = item.get("url")
        if url:
            row = spider.name + "_" + enc.Encrypt.md5(url)
            mutations = list()
            mutations.append(Mutation(column="data:json", value=str(json.dumps(item, ensure_ascii=False))))
            self.client.mutateRow(self.table_name, row, mutations)
            logger.info("Pipeline Data 2 HBase\t" + row)
        else:
            logger.info("No url from spider \t" + spider.name)
        return item

    def close_spider(self, spider):
        self.transport.close()


class TestPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.settings = crawler.settings

    def process_item(self, item, spider):
        print("===" * 44)
        print(TestPipeline.settings)
        print(dir(spider))
        print(dir(self))
        print("===" * 44)
