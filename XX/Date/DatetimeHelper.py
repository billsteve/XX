# -*- encoding:utf8 -*-
import datetime
import time

import XX.Tools.funclib as cfun
import pandas as pd


# 获取距离今天的某段时间的时间戳
def getAddDateTs(month=0, day=1, start_ts=None):
    if start_ts:
        x = time.localtime(start_ts)
    else:
        x = time.localtime(time.time())
    now = time.strftime('%Y-%m-%d', x)
    Y = int(time.strftime('%Y', x))
    M = int(time.strftime('%m', x))
    D = int(time.strftime('%d', x))
    z = datetime.datetime(Y, M, D)
    strts = str(z + pd.tseries.offsets.DateOffset(months=month, days=day))
    ts = int(time.mktime(time.strptime(strts, '%Y-%m-%d %H:%M:%S')))
    return ts


# 字符串转时间戳
def strToTs(str1):
    return int(time.mktime(time.strptime(str1, '%Y-%m-%d %H:%M:%S')))


# 时间戳转换为日期
def tsToDate(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))


# 时间戳转换为日期
def tsToDatetime(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


# 时间戳转换为时间
def tsToTime(ts):
    return time.strftime('%H:%M:%S', time.localtime(ts))


# 获取现在的时间
def GetNowTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))


# 获取今天的日期
def GetToday():
    return time.strftime('%Y-%m-%d', time.localtime(int(time.time())))


# 获取今天的月份
def GetThisMonth():
    return time.strftime('%Y-%m', time.localtime(int(time.time())))


# 获取当前小时
def GetHours():
    return time.strftime('%H', time.localtime(int(time.time())))


# 获取计算时间
def getCalcDate(s):
    return cfun.str_to_standardtime(s)


def isDate(date):
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
    except:
        return False


def getDate(date):
    date = date.replace("年", "-").replace("月", "-").replace("日", "").replace("号", "").replace("点", ":").replace("时", ":").replace("分", ":").replace("秒", "")
    date = cfun.str_to_standardtime(date)
    try:
        date = date.strip()
        if len(date) == 0:
            return False
        date = cfun.str_to_standardtime(date)
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
                date = time.strptime(GetToday()[:4] + "-" + date, "%Y-%m-%d")
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


if __name__ == "__main__":
    print(getDate("03月15日"))
