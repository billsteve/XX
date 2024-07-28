# -*- coding: utf-8 -*-
import decimal
import re
import urllib.parse
from datetime import datetime, date


def url_parse(k):
    return urllib.parse.unquote(str(k))


def url_encode(k):
    return urllib.parse.quote(str(k))


# 给不能dump的字段，改为能dump
def parse_dict(item):
    if isinstance(item, str):
        return item
    if isinstance(item, list):
        l = []
        for i in item:
            l.append(parse_dict(i))
        return l
    for k in item:
        print(item)
        print(k)
        if isinstance(item[k], str):
            pass
        elif isinstance(item[k], dict):
            item[k] = parse_dict(item[k])
        elif isinstance(item[k], list):
            item[k] = parse_dict(item[k])
        elif isinstance(item[k], decimal.Decimal):
            item[k] = float(item[k])
        elif isinstance(item[k], datetime):
            item[k] = item[k].strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(item[k], date):
            item[k] = item[k].strftime('%Y-%m-%d')
    return item


# 从url中获取参数列表
def format_url_to_dict(url):
    res = {}
    try:
        values = url.split('?')[-1]
        if values:
            for key_value in values.split('&'):
                if key_value.find("=") >= 0:
                    try:
                        res[key_value.split('=')[0]] = key_value.split('=')[1]
                    except Exception as e:
                        print(e)
                        raise
    except Exception as e:
        print(e)
        raise
    return res


def delHtml(str1):
    str1 = str1.replace("<br />", "\n").replace("<br/>", "\n").replace("<br>", "\n").replace("<hr />", "\n")
    return re.compile(r"<[^>]+>", re.S).sub('', str(str1)) if str1 else ""


def decode_url(url):
    import urllib.parse
    return urllib.parse.unquote(url)


# 删除字符串
def delStr(from_str, start_str, end_str):
    s_index = from_str.find(start_str)
    if s_index > 0:
        s_index = len(start_str) + s_index
        e_index = from_str.find(end_str, s_index)
        if s_index < e_index:
            from_str1 = from_str[:s_index - 1]
            from_str2 = from_str[e_index + 1:]
            from_str = from_str1 + from_str2
            return cut_str(from_str, start_str, end_str)
        else:
            return from_str
    else:
        return from_str


# 切割字符串
def cut_str(from_str, start_str, end_str):
    s_index = from_str.find(start_str)
    if s_index > 0:
        s_index = len(start_str) + s_index
        e_index = from_str.find(end_str, s_index)
        if e_index >= s_index:
            return from_str[s_index:e_index]
        else:
            return from_str[s_index:]
    return ""


def get_cookies_from_list(l):
    # l = ['BDORZ=27315; max-age=86400; domain=.baidu.com; path=/','BDORZ2=27315; max-age=86400; domain=.baidu.com; path=/']
    cookies = {}
    for cookie in l:
        k_v = cookie.split(";")[0]
        k_v = k_v.split("=")
        cookies[k_v[0]] = k_v[1]
    return cookies


def get_cookie_from_str(cookie):
    lines = cookie.split(";")
    cookies = {}
    for line in lines:
        if line.find("=") >= 0:
            name, value = line.strip().split('=', 1)
            cookies[name] = value
    return cookies


def get_header_from_line_str(headers):
    return {each.split(':', 1)[0].strip(): each.split(':', 1)[1].strip() for each in headers.split('\n') if
            each.split()}


# 获取字符串中的数字
def get_num_from_str(msg):
    if isinstance(msg, str):
        return re.findall(r"\d+", str(msg))
    elif isinstance(msg, bytes):
        return re.findall(r"\d+", str(msg.decode("utf-8")))
    else:
        return msg


#  获取文本中的电话
def get_tel(text):
    tel = re.findall(r"\(?0\d{2,3}[) -]?\d{7,9}-\d{0,8}", text)
    if tel:
        return tel[0]
    else:
        tel = re.findall(r"1\d{10}$", text)
        if tel:
            return tel[0]
        return


def tff2_unicode():  # 将字体映射为unicode列表
    filename = '/home/jason/workspace/1.ttf'
    fnt = fontforge.open(filename)
    for i in fnt.glyphs():
        print(i.unicode)


if __name__ == '__main__':
    d = {'url': 'https://tool.chinaz.com:443/subdomain?domain=tencent.com&page=1',
         'sub_urls': ['tencent.com', 'cloud.tencent.com', 'meeting.tencent.com', 'www.tencent.com', 'intl.cloud.tencent.com']}
    r = parse_dict(d)
    print(r)
