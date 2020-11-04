# -*- coding: utf-8 -*-
import re


# TODO：debug 其他图片 以img开头的图片的url

def get_img_urls(html):
    return re.findall('http.+\.jpg', html)


def get_url_from_html(txt):
    return re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", txt)


def get_url_from_text(txt):
    return re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", txt)


def get_ip(txt):
    return re.findall(
        r"((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))", txt)


def replace_continuous_blank_2_one(txt):
    return re.sub(' +', ' ', txt)


def get_date(txt):
    if txt and isinstance(txt, str):
        return re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", txt)


def repleaseEmoji(sourceStr, replaceStr=''):
    if isinstance(sourceStr, str):
        try:
            co = re.compile('[\U00010000-\U0010ffff]')
        except re.error:
            co = re.compile('[\uD800-\uDBFF][\uDC00-\uDFFF]')
        return co.sub(sourceStr, replaceStr)
    else:
        return sourceStr


def get_version(app):
    return re.findall(r'\d+\.(?:\d+\.)*\d+', app)


if __name__ == '__main__':
    print(get_version("drupal4"))
