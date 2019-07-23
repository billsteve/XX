# -*- coding: utf-8 -*-
import re
import traceback
import urllib.parse


def urlParse(k):
    return urllib.parse.unquote(str(k))


def urlEncode(k):
    return urllib.parse.quote(str(k))


def parseDict(item):
    # if isinstance(item, Item):
    #     item = parseDict(item.__dict__)
    for k in item:
        if isinstance(item[k], str):
            item[k] = urlParse(item[k])
        elif isinstance(item[k], dict):
            item[k] = parseDict(item[k])
    return item


# 从url中获取参数列表
def formatUrlToDict(url):
    res = {}
    try:
        values = url.split('?')[-1]
        for key_value in values.split('&'):
            try:
                res[key_value.split('=')[0]] = key_value.split('=')[1]
            except:
                pass
        return res
    except:
        traceback.print_exc()
        print(" === URL: " + str(url))
        return {}


def delHtml(str1):
    str1 = str1.replace("<br />", "\n").replace("<br/>", "\n").replace("<br>", "\n").replace("<hr />", "\n")
    return re.compile(r'<[^>]+>', re.S).sub('', str(str1)) if str1 else ""


def decodeUrl(url):
    import urllib.parse
    return urllib.parse.unquote(url)


# 删除字符串
def delStr(from_str, start_str, end_str):
    s_index = from_str.find(start_str)
    if s_index > 0:
        s_index = len(start_str) + s_index
        e_index = from_str.find(end_str, s_index)
        if s_index > 0 and e_index > s_index:
            from_str1 = from_str[:s_index - 1]
            from_str2 = from_str[e_index + 1:]
            from_str = from_str1 + from_str2
            return cutStr(from_str, start_str, end_str)
        else:
            return from_str
    else:
        return from_str


# 切割字符串
def cutStr(from_str, start_str, end_str):
    s_index = from_str.find(start_str)
    if s_index > 0:
        s_index = len(start_str) + s_index
        e_index = from_str.find(end_str, s_index)
        if e_index >= s_index:
            return from_str[s_index:e_index]
        else:
            return from_str[s_index:]
    return ""


def getCookiesFromList(l):
    # l = ['BDORZ=27315; max-age=86400; domain=.baidu.com; path=/','BDORZ2=27315; max-age=86400; domain=.baidu.com; path=/']
    cookies = {}
    for cookie in l:
        k_v = cookie.split(";")[0]
        k_v = k_v.split("=")
        cookies[k_v[0]] = k_v[1]
    return cookies


def getCookieFromStr(cookie):
    lines = cookie.split(";")
    cookies = {}
    for line in lines:
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    return cookies


def getHeaderFromLineStr(headers):
    return {each.split(':', 1)[0].strip(): each.split(':', 1)[1].strip() for each in headers.split('\n') if each.split()}


# 获取字符串中的数字
def getNumFromStr(msg):
    if isinstance(msg, str):
        return re.findall("\d+", str(msg))
    elif isinstance(msg, bytes):
        return re.findall("\d+", str(msg.encode("utf-8")))
    else:
        return msg


#  获取文本中的电话
def getTel(text):
    tel = re.findall(r"\(?0\d{2,3}[) -]?\d{7,9}-\d{0,8}", text)
    if tel:
        return tel[0]
    else:
        tel = re.findall(r"1\d{10}$", text)
        if tel:
            return tel[0]
        return


def getCSSHTML1():
    font_path = "e:\\1.ttf"
    try:
        font = ttLib.TTFont(font_path)
        font.saveXML("E:\\1.xml")
        for one in font.getGlyphOrder():
            print(one)
        return
        num = -1
        for one in font.getGlyphNames():
            print(one)
            continue
            num += 1
            _from = "xe" + one[4:].lower() + ";"
            _to = words[num]
            content = str(content).replace(_from, _to)
        return content
    except:
        print("can't wire font file")
        traceback.print_exc()
        return ""


def modify_data():
    data = "<span style='font-family: myfont;'>&#xedfa;</span>弟目前年入35万左右"
    font_path = "e:\\1.ttf"
    font = ttLib.TTFont(font_path)
    uniList = font['cmap'].tables[0].ttFont.getGlyphOrder()
    print(uniList)

    # 返回替换后的字符串
    return data


def tff2Unicode():  # 将字体映射为unicode列表
    filename = '/home/jason/workspace/1.ttf'
    fnt = fontforge.open(filename)
    for i in fnt.glyphs():
        print(i.unicode)


if __name__ == '__main__':
    pass
