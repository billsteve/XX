# -*- coding: utf-8 -*-
# 从html中提取正文, 文本密度提取算法
# update time: 20161014


import re
import traceback

from lxml import etree
from scrapy import Selector


class GetNewsArticle(object):
    def __init__(self, unicode_url='', unicode_html='', *args, **kwargs):
        self.url = unicode_url
        if type(unicode_html) == str:
            self.html = unicode_html
        else:
            self.html = unicode_html
        if self.url is '' or self.html is '':
            raise ValueError('url or html is null ')
        self.article_content = ''

    def __by_xpath(self):
        try:
            tree = etree.HTML(self.html)
        except:
            tree = etree.HTML(self.html.encode("utf-8"))
        # for 腾讯新闻
        if 'qq.com' in self.url:
            for i in tree.xpath('//div[@id="Cnt-Main-Article-QQ"]//p//text()'):
                self.article_content += i

        # for 今日头条新闻
        elif 'toutiao.com' in self.url:
            for i in tree.xpath('//div[@class="article-content"]//text()'):
                self.article_content += i

        # for 新浪新闻
        elif 'sina.com.cn' in self.url:
            for i in tree.xpath('//div[@id="artibody" or @id="articleContent" or @id="j_articleContent"]//p//text()'):
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'
            if not self.article_content:
                # ??
                for i in tree.xpath('//div[@id="artibody" or @id="articleContent" or @id="j_articleContent"]//p'):
                    self.article_content = self.article_content + cfun.clean_str_label(i.xpath("string(.)")) + '\n'

        # for 搜狐新闻
        elif 'sohu.com' in self.url:
            for i in tree.xpath('//div[@id="contentText"]//text()'):
                self.article_content += i

        # for 网易新闻
        elif '163.com' in self.url:
            for i in tree.xpath('//div[@id="endText"]//text()'):
                self.article_content += i

        # for 汽车之家新闻
        elif 'autohome.com.cn' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@id="articleContent" or @class="dealertext" or @id="newsbody"]/p').extract():
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'

        # for 车质网新闻
        elif '12365auto.com' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@class="show" or @class="sp_new_show"]/p').extract():
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'

        # for 易车网新闻
        elif 'bitauto.com' in self.url or 'yiche.com' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@class="text_box" or @id="openimg_articlecontent"]/p').extract():
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'

        # for 一点资讯
        elif 'yidianzixun.com' in self.url:
            for i in Selector(text=self.html).xpath('//div[@id="imedia-article" or @class="content-bd"]//p//text()'):
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'

        # for 太平洋汽车
        elif 'pcauto.com.cn' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@class="artText clearfix" or @class="artText"]/p').extract():
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'

        # for 爱卡汽车 newsbody
        elif 'xcar.com.cn' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@id="newsbody" or @class="artical_player_wrap"]/p').extract():
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'

        # for 车讯网
        elif 'chexun.com' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@class="news-editbox"]/p').extract():
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'

        # for 买车网
        elif 'maiche.com' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@class="content-left"]//div[@class="detail"]//p//text()'):
                if i:
                    self.article_content = self.article_content + cfun.clean_str_label(str(i)) + '\n'

        # for 凤凰网
        elif 'ifeng.com' in self.url:
            # ??
            for i in Selector(text=self.html).xpath('//div[@class="arl-c-txt"]/p').extract():
                self.article_content = self.article_content + cfun.clean_str_label(i) + '\n'
        else:
            self.article_content = ''

        self.article_content = cfun.clean_str_label(self.article_content)

        if len(self.article_content) < 2:
            return False
        else:
            return True

    def __run(self):
        if not self.__by_xpath():
            ex = htmltoarticle(html=self.html)
            self.article_content = ex.get_ariticle()

    def get_article(self):
        try:
            self.__run()
        except:
            traceback.print_exc()
            self.article_content = ''

        if len(self.article_content) < 2:
            return ""
        else:
            return self.article_content


class htmltoarticle(object):
    def __init__(self, *args, **kwargs):
        self.html = kwargs.pop('html', '')
        if self.html is '':
            raise ValueError('html is null ')
        self.lines = []
        self.block = []
        self.threshold_value = 172

    # 移除HTML标签
    def __removeLabel(self):
        re_doctype = re.compile(r'(?is)<!DOCTYPE.*?>', re.S)
        self.html = re_doctype.sub('', self.html)

        re_comment = re.compile(r'(?is)<!--.*?-->', re.S)
        self.html = re_comment.sub('', self.html)

        re_javascript = re.compile(r'(?is)<script.*?>.*?</script>', re.S)
        self.html = re_javascript.sub('', self.html)

        re_css = re.compile(r'(?is)<style.*?>.*?</style>', re.S)
        self.html = re_css.sub('', self.html)

        re_special_char = re.compile(r'&.{2,5};|&#.{2,5};', re.S)
        self.html = re_special_char.sub('', self.html)

        re_other_tag = re.compile(r'(?is)<.*?>', re.S)
        self.html = re_other_tag.sub('', self.html)

        re_empty_char = re.compile(r'\\s', re.S)
        self.html = re_empty_char.sub('', self.html)

    # 移除空格
    def __removeSpace(self, target_str):
        return "".join(target_str.split())

    # 按行分割，并移除每行首尾的空格
    def __statistic_line(self):
        for line in self.html.splitlines(False):
            line = self.__removeSpace(line)
            self.lines.append(line)

    # 获取1-blockwidth行中每行有多少字符
    def __statistic_block(self, blockwidth):
        i = 0
        while i < len(self.lines) - blockwidth:
            block_len = 0
            j = 0
            while j < blockwidth:
                block_len += len(self.lines[i + j])
                j += 1
            self.block.append(block_len)
            i += 1

    # 不知道干什么用的
    def __find_Surge(self, start, threshold):
        i = start
        while i < len(self.block):
            if self.block[i] > threshold and self.block[i + 1] > 0 and self.block[i + 2] > 0 and self.block[i + 3] > 0:
                return i
            i += 1
        return -1

    def __find_Dive(self, surgePoint):
        i = surgePoint + 1
        while i < len(self.block):
            if self.block[i] == 0 and self.block[i + 1] == 0:
                return i
            i += 1
        return len(self.block) - 1

    def __run(self):
        start = 0
        end = 0
        article_content = ''
        while True:
            start = self.__find_Surge(end, self.threshold_value)
            if start < 0:
                break
            end = self.__find_Dive(start)
            for i in range(start, end + 1):
                article_content += self.lines[i]
                article_content += '\n'
        return article_content

    def get_ariticle(self):
        self.__removeLabel()
        self.__statistic_line()
        self.__statistic_block(3)
        return self.__run()


if __name__ == '__main__':
    import XX.HTTP.RequestsHelper as creq

    url = "http://www.chexun.com/2018-04-20/105255634.html"
    r = creq.RequestHelper.SendCacheRequest(url)
    if r.status_code == 200:
        ex = GetNewsArticle(unicode_url=url, unicode_html=r.text)
        print(ex.get_article())
        # ex = htmltoarticle(html=r.text)
        # print ex.get_ariticle()
