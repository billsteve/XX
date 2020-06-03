#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/27 10:53
# @Author   : Peter
# @Des       : 
# @File        : RegExp
# @Software: PyCharm
import re

import XX.Date.DatetimeHelper as DT


class RegExpHelper():

    @staticmethod
    def get_url_from_html(txt):
        return re.findall("(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", txt)

    @staticmethod
    def get_url_from_text(txt):
        return re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", txt)

    @staticmethod
    def get_ips(txt):
        return re.findall(
            r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", txt)
        # return re.findall("((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))", txt)

    @staticmethod
    def replace_continuous_blank_2_one(txt):
        return re.sub(' +', ' ', txt)

    @staticmethod
    def get_number(txt):
        if not txt or not isinstance(txt, str):
            return
        return re.findall(r"(\d+)", txt)

    @staticmethod
    def is_url(txt):
        return re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", txt)

    @staticmethod
    def is_domain(txt):
        return re.findall("(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", txt)

    @staticmethod
    def get_date(s):
        if not s or not isinstance(s, str):
            return ""
        p = re.compile(r'\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}|\d{4}年\d{1,2}月\d{1,2}[日号]|今天|\d{1,2}月\d{1,2}[日号]')
        result = re.findall(p, s)
        try:
            print(result[0])
            result[0] = result[0].replace('年', '-').replace('月', '-').replace('日', '').replace('号', '')
            if result[0] == "今天":
                return DT.GetToday()
            if len(result[0]) == 4 or len(result[0]) == 5:
                print(result[0])
                return str(DT.GetToday().split("-")[0]) + result[0]
            return result[0]
        except Exception as e:
            print(e)

    # TODO:适应  20190202这样的情况
    @staticmethod
    def get_date_time(s):
        if not s or not isinstance(s, str):
            return ""
        r = r"(\d{2,4}[-/年]\d{1,2}[-/月]\d{1,2}日? \d{2}:\d{2}(:\d{2})?)"
        r = r"\d{2,4}[-/年]\d{1,2}[-/月]\d{1,2}日? \d{2}:\d{2}(:\d{2})?"
        p = re.compile(r)
        result = re.findall(p, s)
        try:
            result[0] = result[0].replace('年', '-').replace('月', '-').replace('日', '').replace('号', '')
            if result[0] == "今天":
                return DT.GetToday()
            if len(result[0]) == 4 or len(result[0]) == 5:
                print(result[0])
                return str(DT.GetToday().split("-")[0]) + result[0]
            return result[0]
        except Exception as e:
            print(e)

    # 是否是汉字
    @staticmethod
    def is_Chinese(w):
        for ch in w:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False

    @staticmethod
    def get_chinese(s):
        return re.sub("[A-Za-z0-9\_\{\}\$\.\:\/\"\!\%\[\]\,\。]", "", s)
