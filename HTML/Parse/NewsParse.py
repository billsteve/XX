#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/1/15 14:25
# @File           : NewsParse
# @Des           : 新闻解析
# @Email        : billsteve@126.com
from newspaper import Article


class NewsParse:
    def __init__(self, **kw):
        self.html = kw.get("html")
        self.url = kw.get("url")

    def getNewsItem(self, **kw):
        data = dict()

        html = self.html if self.html else kw.get("html")
        doc = Article(kw.get("url", "-"), language="zh")
        doc.download(input_html=html)
        doc.parse()
        data["url"] = doc.url
        data["title"] = doc.title
        data["content"] = doc.text
        data["date"] = str(doc.publish_date)
        return data


if __name__ == '__main__':
    from pprint import pprint

    # html = """</div>2018-09-18 13:35:03 &nbsp;<a href='http://look.huanqiu.com/article/2018-09/13041797.html' target='_blank'>环球网</a> &nbsp; &nbsp;<span class="chan_newsInfo_comment"><a href="#comment">参与评论(<em id="top_comment_number"></em>)人</a></span>"""
    html = open("a.html", encoding="utf-8").read()

    pprint(NewsParse.getNewsItem(NewsParse(), html=html))
