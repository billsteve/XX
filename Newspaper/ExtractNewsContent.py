#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/1/6 13:30
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : ExtractNewsContent.py
# @Des         : 
# @Software : PyCharm
from newspaper import Article


class ExtractNewsContent:

    def __init__(self, *args, **kwargs):
        self.article = Article(kwargs.get("url", ""), keep_article_html=True, language=kwargs.get("language", "zh"))
        if kwargs.get("input_html"):
            self.article.download(input_html=kwargs.get("input_html"))
        self.article.parse()
