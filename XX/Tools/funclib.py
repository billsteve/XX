#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/24 13:44
# @Author   : Peter
# @Des       : 
# @File        : funclib
# @Software: PyCharm
import datetime
import json
import re
import traceback


# !!!废弃的函数,兼容以前的spider，保留此函数
def unicode_to_str(text, encoding=None, errors='strict'):
    """Return the str representation of text in the given encoding. Unlike
    .encode(encoding) this function can be applied directly to a str
    object without the risk of double-decoding problems (which can happen if
    you don't use the default 'ascii' encoding)
    """
    if encoding is None:
        encoding = 'utf-8'
    if isinstance(text, bytes):
        return text.encode(encoding, errors)
    elif isinstance(text, str):
        return text
    else:
        raise TypeError('unicode_to_str must receive a unicode or str object, got %s' % type(text).__name__)


# 内置数据类型转换成 str
def to_str(data):
    if isinstance(data, (int, float, bool)) or data is None:
        return str(data)
    elif isinstance(data, bytes):
        return data.encode('utf-8')
    elif isinstance(data, str):
        return data
    elif isinstance(data, list):
        return __list_to_str(data)
    elif isinstance(data, dict):
        return __dict_to_str(data)
    elif isinstance(data, tuple):
        return __tuple_to_str(data)
    elif isinstance(data, set):
        return __set_to_str(data)
    elif isinstance(data, (datetime.datetime, datetime.date)):
        return __datetime_to_str(data)
    else:
        print('Dont know how to change %s to str!' % str(type(data)))
        return ''


# 字典转换成字符串, 其中的unicode自动转换成str
def __dict_to_str(data_dict):
    line = '{'
    # print data_dict.items()
    for k, v in data_dict.items():
        line += '%s: %s, ' % (k, to_str(v))
    return line.strip(', ') + '}'


# 列表转换成字符串, 其中的unicode自动转换成str
def __list_to_str(data_list):
    line = '['
    for var in data_list:
        line += '%s, ' % to_str(var)
    return line.strip(', ') + ']'


# tuple转换成str, 其中的unicode自动转换成str
def __tuple_to_str(data_tuple):
    return '(' + __list_to_str(list(data_tuple)).strip('[]') + ')'


# set转换成str, 其中的unicode自动转换成str
def __set_to_str(data_set):
    return 'set(' + __list_to_str(list(data_set)) + ')'


def __datetime_to_str(date_time):
    if isinstance(date_time, datetime.date):
        return str(date_time)
    return date_time.strftime('%Y-%m-%d %H:%M:%S %f')


# !!!废弃的函数,兼容以前的spider，保留此函数
def json_to_dict(target_unicode_str):
    try:
        target = target_unicode_str[target_unicode_str.index("{"):]
        return json.loads(target)
    except:
        pass


# json转字典(gbk)
def json_to_dict_gbk(target_gbk_str):
    try:
        return json.loads(__json_to_standard(target_gbk_str), encoding="gbk")
    except:
        pass


# json转字典(utf8)
def json_to_dict_utf8(target_utf8_str):
    try:
        return json.loads(__json_to_standard(target_utf8_str), encoding="utf-8")
    except:
        pass


# 内置函数
def __json_to_standard(target_str):
    target = target_str[target_str.index("{"):]
    target = target[:target.rindex("}") + 1]
    return target


# 取列表中最大数值, 一般页数是从1开始的
def list_max_number(target_list):
    new_list = []
    for i in target_list:
        i_buffer = ''
        for j in i:
            if j.isdigit() == True:
                i_buffer += j
        if i_buffer.isdigit() == True:
            new_list.append(int(i_buffer))
    if new_list:
        return int(max(new_list))
    else:
        return 1


# 清洗字符串中的换行空格和回车
def clean_str_space(target_str):
    return "".join(target_str.split())


# 清洗字符串中的html标签
def clean_str_label(target_str):
    re_flag = re.compile(r'<[^>]*>', re.S)
    result = re_flag.sub('', target_str)
    return result


# 字符串转list
def str_to_list(target_str):
    if isinstance(target_str, str):
        if target_str == '':
            return []
        elif target_str[0] == '[' and target_str[-1] == ']':
            xlist = []
            for i in target_str[1:-1].split(','):
                if i == '' or i == ' ':
                    continue
                xlist.append(i)
            return xlist
        else:
            raise TypeError(
                'String must be have [ and ], got %s' % type(target_str).__name__)
    else:
        raise TypeError('Type must be string, got %s' %
                        type(target_str).__name__)


# 字符串转字典
def str_to_dict(target_str):
    dict = {}
    for i in target_str.split(';'):
        if '=' in i:
            dict[i.split('=')[0]] = i.split('=')[1]
        else:
            continue
    return dict


# 从字符串提取数字
def str_to_digit(target_str):
    try:
        if isinstance(target_str, bytes):
            target_str = to_str(target_str)
        if len(target_str) > 0:
            return int(re.sub("\D", "", target_str))
        else:
            print("no str")
            return None
    except:
        traceback.print_exc()
        return None


# 从字符串中提取时间
def str_to_time(target_timestr):
    try:
        if isinstance(target_timestr, bytes):
            target_timestr = to_str(target_timestr)
        r = re.search(
            u'\d{4}(:|-|\\|/|年)\d{1,2}(:|-|\\|/|月)\d{1,2}(|日) \d{1,2}(:|-|\\|/|时|点)\d{1,2}', target_timestr)
        if r:
            return r.group(0)
        else:
            return None
    except:
        return None


# 日期计算，通过XX小时，分，天，周来计算时间
def str_to_standardtime(target_cntimestr):
    now = datetime.datetime.now()
    standtime = ''
    # calc计算方式,False 减, True 加
    calc = False

    if isinstance(target_cntimestr, bytes):
        target_cntimestr = to_str(target_cntimestr)

    if '前' in target_cntimestr:
        calc = False
    elif '后' in target_cntimestr:
        calc = True
    else:
        return target_cntimestr

    if '秒' in target_cntimestr:
        if calc:
            standtime = now + datetime.timedelta(seconds=str_to_digit(target_cntimestr))
        else:
            standtime = now - datetime.timedelta(seconds=str_to_digit(target_cntimestr))
    elif '分' in target_cntimestr:
        if calc:
            standtime = now + datetime.timedelta(minutes=str_to_digit(target_cntimestr))
        else:
            standtime = now - datetime.timedelta(minutes=str_to_digit(target_cntimestr))
    elif '时' in target_cntimestr:
        if calc:
            standtime = now + datetime.timedelta(hours=str_to_digit(target_cntimestr))
        else:
            standtime = now - datetime.timedelta(hours=str_to_digit(target_cntimestr))
    elif '天' in target_cntimestr:
        if calc:
            standtime = now + datetime.timedelta(days=str_to_digit(target_cntimestr))
        else:
            standtime = now - datetime.timedelta(days=str_to_digit(target_cntimestr))
    elif '周' in target_cntimestr:
        if calc:
            standtime = now + datetime.timedelta(weeks=str_to_digit(target_cntimestr))
        else:
            standtime = now - datetime.timedelta(weeks=str_to_digit(target_cntimestr))
    else:
        raise ValueError('target_cntimestr must include 时分秒天周, and so on ')
    return standtime.strftime('%Y-%m-%d %H:%M:%S')


# 清空字典中空数据
def clean_dict(data_dict):
    if isinstance(data_dict, dict):
        for k, v in data_dict.items():
            if not v == 0 and not v:
                data_dict.pop(k)
            else:
                if '.' in k:
                    data_dict[re.sub('\.', '~', k)] = data_dict.pop(k)
                clean_dict(v)
    elif isinstance(data_dict, list):
        for var in data_dict:
            clean_dict(var)
    return data_dict


if __name__ == "__main__":
    print(str_to_standardtime("2天前"))
