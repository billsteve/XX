# coding:utf8

import re
from urllib.parse import unquote
import requests
import sys


def get_char(js):
    all_var = {}
    # 判断混淆 无参数 返回常量 函数
    if_else_no_args_return_constant_function_functions = []
    """
    function zX_() {
            function _z() {
                return '09';
            };
            if (_z() == '09,') {
                return 'zX_';
            } else {
                return _z();
            }
        }
    """
    constant_function_regex4 = re.compile("""
        function\s+\w+\(\)\s*\{\s*
            function\s+\w+\(\)\s*\{\s*
                return\s+[\'\"][^\'\"]+[\'\"];\s*
            \};\s*
            if\s*\(\w+\(\)\s*==\s*[\'\"][^\'\"]+[\'\"]\)\s*\{\s*
                return\s*[\'\"][^\'\"]+[\'\"];\s*
            \}\s*else\s*\{\s*
                return\s*\w+\(\);\s*
            \}\s*
        \}
        """,
                                          re.X)
    l = constant_function_regex4.findall(js)
    for i in l:
        function_name = re.search("""
        function\s+(\w+)\(\)\s*\{\s*
            function\s+\w+\(\)\s*\{\s*
                return\s+[\'\"]([^\'\"]+)[\'\"];\s*
            \};\s*
            if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
            \}\s*else\s*\{\s*
                return\s*\w+\(\);\s*
            \}\s*
        \}
        """, i,
                                  re.X)
        if_else_no_args_return_constant_function_functions.append(
            function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b, c, d = function_name.groups()
        all_var["%s()" % a] = d if b == c else b

    # 判断混淆 无参数 返回函数 常量
    if_else_no_args_return_function_constant_functions = []
    """
    function wu_() {
            function _w() {
                return 'wu_';
            };
            if (_w() == 'wu__') {
                return _w();
            } else {
                return '5%';
            }
        }
    """
    constant_function_regex5 = re.compile("""
        function\s+\w+\(\)\s*\{\s*
            function\s+\w+\(\)\s*\{\s*
                return\s+[\'\"][^\'\"]+[\'\"];\s*
            \};\s*
            if\s*\(\w+\(\)\s*==\s*[\'\"][^\'\"]+[\'\"]\)\s*\{\s*
                return\s*\w+\(\);\s*
            \}\s*else\s*\{\s*
                return\s*[\'\"][^\'\"]+[\'\"];\s*
            \}\s*
        \}
        """,
                                          re.X)
    l = constant_function_regex5.findall(js)
    for i in l:
        function_name = re.search("""
        function\s+(\w+)\(\)\s*\{\s*
            function\s+\w+\(\)\s*\{\s*
                return\s+[\'\"]([^\'\"]+)[\'\"];\s*
            \};\s*
            if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
                return\s*\w+\(\);\s*
            \}\s*else\s*\{\s*
                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
            \}\s*
        \}
        """, i,
                                  re.X)
        if_else_no_args_return_function_constant_functions.append(
            function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b, c, d = function_name.groups()
        all_var["%s()" % a] = b if b == c else d

    # var 参数等于返回值函数
    var_args_equal_value_functions = []
    """
    var ZA_ = function(ZA__) {
            'return ZA_';
            return ZA__;
        };
    """
    constant_function_regex1 = re.compile(
        "var\s+[^=]+=\s*function\(\w+\)\{\s*[\'\"]return\s*\w+\s*[\'\"];\s*return\s+\w+;\s*\};")
    l = constant_function_regex1.findall(js)
    for i in l:
        function_name = re.search("var\s+([^=]+)", i).group(1)
        var_args_equal_value_functions.append(function_name)
        js = js.replace(i, "")
        # 替换全文
        a = function_name
        js = re.sub("%s\(([^\)]+)\)" % a, r"\1", js)

    # var 无参数 返回常量 函数
    var_no_args_return_constant_functions = []
    """
    var Qh_ = function() {
            'return Qh_';
            return ';';
        };
    """
    constant_function_regex2 = re.compile("""
            var\s+[^=]+=\s*function\(\)\{\s*
                [\'\"]return\s*\w+\s*[\'\"];\s*
                return\s+[\'\"][^\'\"]+[\'\"];\s*
                \};
            """,
                                          re.X)
    l = constant_function_regex2.findall(js)
    for i in l:
        function_name = re.search("""
            var\s+([^=]+)=\s*function\(\)\{\s*
                [\'\"]return\s*\w+\s*[\'\"];\s*
                return\s+[\'\"]([^\'\"]+)[\'\"];\s*
                \};
            """,
                                  i,
                                  re.X)
        var_no_args_return_constant_functions.append(function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b = function_name.groups()
        all_var["%s()" % a] = b

    # 无参数 返回常量 函数
    no_args_return_constant_functions = []
    """
    function ZP_() {
            'return ZP_';
            return 'E';
        }
    """
    constant_function_regex3 = re.compile("""
            function\s*\w+\(\)\s*\{\s*
                [\'\"]return\s*[^\'\"]+[\'\"];\s*
                return\s*[\'\"][^\'\"]+[\'\"];\s*
            \}\s*
        """,
                                          re.X)
    l = constant_function_regex3.findall(js)
    for i in l:
        function_name = re.search("""
            function\s*(\w+)\(\)\s*\{\s*
                [\'\"]return\s*[^\'\"]+[\'\"];\s*
                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
            \}\s*
        """,
                                  i,
                                  re.X)
        no_args_return_constant_functions.append(function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b = function_name.groups()
        all_var["%s()" % a] = b

    # 无参数 返回常量 函数 中间无混淆代码
    no_args_return_constant_sample_functions = []
    """
    function do_() {
            return '';
        }
    """
    constant_function_regex3 = re.compile("""
            function\s*\w+\(\)\s*\{\s*
                return\s*[\'\"][^\'\"]*[\'\"];\s*
            \}\s*
        """,
                                          re.X)
    l = constant_function_regex3.findall(js)
    for i in l:
        function_name = re.search("""
            function\s*(\w+)\(\)\s*\{\s*
                return\s*[\'\"]([^\'\"]*)[\'\"];\s*
            \}\s*
        """,
                                  i,
                                  re.X)
        no_args_return_constant_sample_functions.append(function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b = function_name.groups()
        all_var["%s()" % a] = b

    # 字符串拼接时使无参常量函数
    """
    (function() {
                'return sZ_';
                return '1'
            })()
    """
    constant_function_regex6 = re.compile("""
            \(function\(\)\s*\{\s*
                [\'\"]return[^\'\"]+[\'\"];\s*
                return\s*[\'\"][^\'\"]*[\'\"];?
            \}\)\(\)
        """,
                                          re.X)
    l = constant_function_regex6.findall(js)
    for i in l:
        function_name = re.search("""
            \(function\(\)\s*\{\s*
                [\'\"]return[^\'\"]+[\'\"];\s*
                return\s*([\'\"][^\'\"]*[\'\"]);?
            \}\)\(\)
        """,
                                  i,
                                  re.X)
        js = js.replace(i, function_name.group(1))

    # 字符串拼接时使用返回参数的函数
    """
    (function(iU__) {
                'return iU_';
                return iU__;
            })('9F')
    """
    constant_function_regex6 = re.compile("""
            \(function\(\w+\)\s*\{\s*
                [\'\"]return[^\'\"]+[\'\"];\s*
                return\s*\w+;
            \}\)\([\'\"][^\'\"]*[\'\"]\)
        """,
                                          re.X)

    l = constant_function_regex6.findall(js)
    for i in l:
        function_name = re.search("""
            \(function\(\w+\)\s*\{\s*
                [\'\"]return[^\'\"]+[\'\"];\s*
                return\s*\w+;
            \}\)\(([\'\"][^\'\"]*[\'\"])\)
        """,
                                  i,
                                  re.X)
        js = js.replace(i, function_name.group(1))

    # 获取所有变量
    var_regex = "var\s+(\w+)=(.*?);\s"

    for var_name, var_value in re.findall(var_regex, js):
        var_value = var_value.strip("\'\"").strip()
        if "(" in var_value:
            var_value = ";"
        all_var[var_name] = var_value

    # 注释掉 此正则可能会把关键js语句删除掉
    # js = re.sub(var_regex, "", js)

    for var_name, var_value in all_var.items():
        js = js.replace(var_name, var_value)

    js = re.sub("[\s+']", "", js)

    # 寻找%E4%B8%AD%E5%80%92%E 密集区域
    string_region = re.findall("((?:%\w\w)+)", js)
    string_str = ""
    for string_ in string_region:
        if len(string_) > len(string_str):
            string_str = string_

    string = unquote(string_str)

    # 从 字符串密集区域后面开始寻找索引区域
    index_m = re.search("([\d,]+(;[\d,]+)+)", js[js.find(string_str) + len(string_str):])
    string_list = list(string)
    index_list = index_m.group(1).split(";")

    _word_list = []
    for word_index_list in index_list:
        _word = ""
        if "," in word_index_list:
            word_index_list = word_index_list.split(",")
            word_index_list = [int(x) for x in word_index_list]
        else:
            word_index_list = [int(word_index_list)]
        for word_index in word_index_list:
            _word += string_list[word_index]
        _word_list.append(_word)
    return _word_list


def get_complete_text_autohome(text):
    types = re.findall('hs_kw\d+_([^\'\"]+)', text)
    types = set(types)
    # js_list = re.findall("<script>(\(function[\s\S]+?)\(document\);</script>", text.encode("utf8"))
    js_list = re.findall("<script>(\(function[\s\S]+?)\(document\);</script>", text)
    type_charlist = {}
    for js in js_list:
        for _type in types:
            if _type in js:
                break
        # else:
        #     continue
        if not js:
            continue
        try:
            char_list = get_char(js)
        except Exception as e:
            continue
        type_charlist.update({_type: char_list})

    def char_replace(m):
        index = int(m.group(1))
        typ = m.group(2)
        char_list = type_charlist.get(typ, [])
        if not char_list:
            return m.group()
        char = char_list[index]
        return char

    text = re.sub("<span\s*class=[\'\"]hs_kw(\d+)_([^\'\"]+)[\'\"]></span>", char_replace, text)
    return text


# get html
def getRealHtml(html):
    if html:
        # html = get_complete_text_autohome(html.encode('utf-8'))
        html = get_complete_text_autohome(html)
        try:
            text = re.search("<div\s*class=[\'\"]tz-paragraph[^\'\"]*?[\'\"]>([\s\S]+?)</div>", html).group(1)
        except:
            try:
                text = re.search("<div\s*class=[\'\"]conttxt content[^\'\"]*?[\'\"]>([\s\S]+?)</div>", html).group(1)
            except:
                try:
                    text = re.search("<div\s*class=[\'\"]content conttxt[^\'\"]*?[\'\"]>([\s\S]+?)</div>", html).group(1)
                except:
                    try:
                        text = re.search("<div\s*class=[\'\"]conttxt[^\'\"]*?[\'\"]>([\s\S]+?)</div>", html).group(1)
                    except:
                        try:
                            text = re.search("<div\s*class=[\'\"]content[^\'\"]*?[\'\"]>([\s\S]+?)</div>", html).group(1)
                        except:
                            text = ""
        return text


if __name__ == "__main__":
    import sys

    html = open("D:\\1.html", "r").read().encode("utf-8")
    print(len(html))
    html = getRealHtml(html)
    open("D:\\res.log", "w").write(html)
    print("===")
