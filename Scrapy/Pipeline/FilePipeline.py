#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import time

import XX.File.FileHelper as cf
import XX.HTML.HtmlHelper as chtml


# File pipeline:放到今日文件中
class FilePipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.settings = settings
        return cls()

    def process_item(self, item, spider):
        # 数据处理
        item = chtml.parseDict(dict(item))
        today = time.strftime("%Y_%m_%d", time.localtime(int(time.time())))
        json_str = json.dumps(item, ensure_ascii=False)

        # 保存数据到文件
        file_path = FilePipeline.settings.get("ROOT_PATH_JSON") + "json" + os.sep + spider.name + os.sep + today + ".json"
        cf.FileHelper.save_file(file_path, json_str + "\n")
        return item
