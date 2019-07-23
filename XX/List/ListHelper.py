#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/24 14:24
# @Author   : Peter
# @Des       : 
# @File        : ListHelper
# @Software: PyCharm
import XX.Dict.DictHelper


class ListHelper:
    @staticmethod
    def decodeV(d, coding="utf-8"):
        ll = []
        for v in d:
            if type(v) == list or type(v) == tuple:
                ll.append(ListHelper.decodeV(list(v), coding))
            elif type(v) == bytes:
                ll.append(v.decode(coding))
            elif type(v) == dict:
                ll.append(Utils.Dict.DictHelper.DictHelper.decodeV(v, coding))
            else:
                ll.append(v)
        return ll


if __name__ == '__main__':
    s = [{'web_id': b'a', 'id': 4}, {'web_id': b'a0', 'id': 3}, {'web_id': b'a00', 'id': 2}, {'web_id': b'b', 'id': 5}, {'web_id': b'c', 'id': 6}, {'web_id': b'd', 'id': 7}, {'web_id': b'mb', 'id': 12}, {'web_id': b'mpv', 'id': 9},
         {'web_id': b'p', 'id': 11}, {'web_id': b'qk', 'id': 13}, {'web_id': b's', 'id': 10}, {'web_id': b'suva', 'id': 16}, {'web_id': b'suva0', 'id': 15}, {'web_id': b'suvb', 'id': 17}, {'web_id': b'suvc', 'id': 18},
         {'web_id': b'suvd', 'id': 19}]
    t = ListHelper.decodeV(s)
    print(t)

    pass
