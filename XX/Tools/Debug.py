# -  *  - coding:utf-8 -  *  -
import time


def pline(line="===", num=50):
    print(line * num)


def p(msg="", ts=0, line=""):
    try:
        if line:
            print(str(msg) + line * 30)
        else:
            print(str(msg))
    except:
        print(" \n === Can't print msg" + str(type(msg)) + " ========== ===")
    time.sleep(ts)


def d(msg="", ts=0, line1="", line2="", MsgAction=None, *arg, **kw):
    if line1:
        if not line2:
            line2 = line1
        pline(line1, 30)
    try:
        if MsgAction:
            print(MsgAction(msg, *arg, **kw))
        else:
            print(msg)
    except:
        print(" \n === Can't print msg" + str(type(msg)) + " ========== ===")
        return
    if line2:
        pline(line2, 30)
    time.sleep(ts)


def pe(*arg, **kwg):
    p(*arg, **kwg)
    exit()


def de(*arg, **kwg):
    d(*arg, **kwg)
    exit()


def dict_print(obj, indent=' '):
    def _pretty(obj, indent):
        for i, tup in enumerate(obj.items()):
            k, v = tup
            # 如果是字符串则拼上""
            if isinstance(k, str):
                k = '"%s"' % k
            if isinstance(v, str):
                v = '"%s"' % v
            # 如果是字典则递归
            if isinstance(v, dict):
                # 计算下一层的indent
                v = ''.join(_pretty(v, indent + ' ' * len(str(k) + ': {')))
            # case,根据(k,v)对在哪个位置确定拼接什么
            if i == 0:  # 开头,拼左花括号
                if len(obj) == 1:
                    yield '{%s: %s}' % (k, v)
                else:
                    yield '{%s: %s,\n' % (k, v)
            elif i == len(obj) - 1:  # 结尾,拼右花括号
                yield '%s%s: %s}' % (indent, k, v)
            else:  # 中间
                yield '%s%s: %s,\n' % (indent, k, v)

    return ''.join(_pretty(obj, indent))


if __name__ == "__main__":
    d("测试 信息    ", line1="-v-", line2="-^-")
