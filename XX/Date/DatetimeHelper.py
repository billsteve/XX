# -*- encoding:utf8 -*-
import datetime
import time

import pandas as pd

import XX.funclib as cfun


# 获取距离今天的某段时间的时间戳
def get_add_date_ts(month=0, day=1, start_ts=None):
    if start_ts:
        x = time.localtime(start_ts)
    else:
        x = time.localtime(time.time())
    Y = int(time.strftime('%Y', x))
    M = int(time.strftime('%m', x))
    D = int(time.strftime('%d', x))
    z = datetime.datetime(Y, M, D)
    starts = str(z + pd.tseries.offsets.DateOffset(months=month, days=day))
    ts = int(time.mktime(time.strptime(starts, '%Y-%m-%d %H:%M:%S')))
    return ts


# 字符串转时间戳
def str_to_ts(str1):
    return int(time.mktime(time.strptime(str1, '%Y-%m-%d %H:%M:%S')))


# 时间戳转换为日期
def ts_to_date(ts=time.time()):
    return time.strftime('%Y-%m-%d', time.localtime(ts))


# 时间戳转换为日期
def ts_to_datetime(ts=time.time()):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


# 时间戳转换为时间
def ts_to_time(ts=time.time()):
    return time.strftime('%H:%M:%S', time.localtime(ts))


# 获取现在的时间
def get_now_time(ts=time.time()):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


# 获取今天的日期
def get_today(ts=time.time()):
    return time.strftime('%Y-%m-%d', time.localtime(ts))


# 获取今天的月份
def get_this_month(ts=time.time()):
    return time.strftime('%Y-%m', time.localtime(ts))


# 获取当前小时
def get_hours(ts=time.time()):
    return time.strftime('%H', time.localtime(ts))


# 获取计算时间
def get_calc_date(s):
    return cfun.str_to_standard_time(s)


def is_date(date):
    try:
        date = date.strip()
        if len(date) == 0:
            return False
        if ":" in date:
            if date.count(":") == 1:
                time.strptime(date, "%Y-%m-%d %H:%M")
            elif date.count(":") == 2:
                time.strptime(date, "%Y-%m-%d %H:%M:%S")
        elif "-" in date:
            time.strptime(date, "%Y-%m-%d")
        elif "/" in date:
            time.strptime(date, "%Y/%m/%d")
        elif "." in date:
            time.strptime(date, "%Y.%m.%d")
        elif len(date) == 8:
            time.strptime(date, "%Y%m%d")
        return True
    except Exception as e:
        return False


def get_date(date):
    date = date.replace("年", "-").replace("月", "-").replace("日", "").replace("号", "").replace("点", ":").replace("时",
                                                                                                                ":").replace(
        "分", ":").replace("秒", "")
    date = cfun.str_to_standard_time(date)
    try:
        date = date.strip()
        if len(date) == 0:
            return False
        date = cfun.str_to_standard_time(date)
        if ":" in date:
            if date.count(":") == 1:
                date = time.strptime(date, "%Y-%m-%d %H:%M")
            elif date.count(":") == 2:
                date = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        elif "-" in date:
            if len(date.split("-")[0]) == 4:
                # "2018-01-01"
                date = time.strptime(date, "%Y-%m-%d")
            elif len(date.split("-")[0]) == 2 and date.count("-") == 2:
                date = time.strptime("20" + date, "%Y-%m-%d")
            elif len(date.split("-")[0]) == 2 and date.count("-") == 1:
                date = time.strptime(get_today()[:4] + "-" + date, "%Y-%m-%d")
        elif "/" in date:
            date = time.strptime(date, "%Y/%m/%d")
        elif "." in date:
            date = time.strptime(date, "%Y.%m.%d")
        elif len(date) == 8:
            date = time.strptime(date, "%Y%m%d")
        else:
            date = ""
        return time.strftime('%Y-%m-%d', date)
    except Exception as e:
        print(e)
        return ""


# 时间戳转为iso8601时间
def ts_to_iso8601(ts=time.time(), format_='%Y-%m-%dT%H:%M:%S.%fZ'):
    format_ = format_.replace('%f', '{-FF-}')  # 订单处理微秒数据 %f
    length = min(16, len(str(ts)))  # 最多去到微秒级

    # 获取毫秒/微秒 数据
    sec = '0'
    if length != 10:  # 非秒级
        sec = str(ts)[:16][-(length - 10):]  # 最长截取16位长度 再取最后毫秒/微秒数据
    sec = '{:0<6}'.format(sec)  # 长度位6，靠左剩下的用0补齐
    timestamp = float(str(ts)[:10])  # 转换为秒级时间戳
    return datetime.datetime.utcfromtimestamp(timestamp).strftime(format_).replace('{-FF-}', sec)


if __name__ == '__main__':
    print(ts_to_iso8601())
