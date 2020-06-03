# -*- coding: utf-8 -*-
import re


class RegExpHelper():

    # TODO：debug 其他图片 以img开头的图片的url
    @staticmethod
    def get_img_urls(html):
        return re.findall('http.+\.jpg', html)

    @staticmethod
    def get_url_from_html(txt):
        return re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", txt)

    @staticmethod
    def get_url_from_text(txt):
        return re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", txt)

    @staticmethod
    def get_ip(txt):
        return re.findall(r"((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))", txt)

    @staticmethod
    def replace_continuous_blank_2_one(txt):
        return re.sub(' +', ' ', txt)

    @staticmethod
    def get_date(txt):
        if not txt or isinstance(txt, str):
            return
        return re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", txt)

    @staticmethod
    def repleaseEmoji(sourceStr, replaceStr=''):
        if isinstance(sourceStr, str):
            try:
                co = re.compile('[\U00010000-\U0010ffff]')
            except re.error:
                import traceback
                co = re.compile('[\uD800-\uDBFF][\uDC00-\uDFFF]')
            return co.sub(sourceStr, replaceStr)
        else:
            return sourceStr


if __name__ == "__main__":
    print(RegExpHelper.repleaseEmoji("加油， 我们与你同在！[抱抱]🌹", "??111"))
    exit()
    content = "<td class='info_d'><div class='info'><a href='//car.autohome.com.cn/pic/series-s17694/49.html?pvareaid=101281'>图片</a><a href='spec/17694/config.html?pvareaid=101282'>参数配置</a>"
    content = "https://www.jb51.net/article/98054.htm"
    for l in RegExpHelper.get_url_from_text(content):
        print(l)
