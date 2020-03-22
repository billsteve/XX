# -*- coding: utf-8 -*-
import XX.Dict.DictHelper


class ListHelper:
    @staticmethod
    def decode_v(d, coding="utf-8"):
        ll = []
        for v in d:
            if type(v) == list or type(v) == tuple:
                ll.append(ListHelper.decodeV(list(v), coding))
            elif type(v) == bytes:
                ll.append(v.decode(coding))
            elif type(v) == dict:
                ll.append(XX.Dict.DictHelper.DictHelper.decodeV(v, coding))
            else:
                ll.append(v)
        return ll


def count_dict_list_by_k_v(dict_list, unique_key="k", count_key="s"):
    word_count = {}
    for one in dict_list:
        word_count[one[unique_key]] = 1 + word_count.get(one[unique_key], 0)
    r = []
    for one in dict_list:
        if word_count.get(one[unique_key]):
            one[count_key] = word_count[one[unique_key]]
            del word_count[one[unique_key]]
            r.append(one)
    return r


if __name__ == '__main__':
    s = [{'web_id': b'a', 'id': 4}, {'web_id': b'a0', 'id': 3}, {'web_id': b'a00', 'id': 2}, {'web_id': b'b', 'id': 5},
         {'web_id': b'c', 'id': 6}, {'web_id': b'd', 'id': 7}, {'web_id': b'mb', 'id': 12}, {'web_id': b'mpv', 'id': 9},
         {'web_id': b'p', 'id': 11}, {'web_id': b'qk', 'id': 13}, {'web_id': b's', 'id': 10},
         {'web_id': b'suva', 'id': 16}, {'web_id': b'suva0', 'id': 15}, {'web_id': b'suvb', 'id': 17},
         {'web_id': b'suvc', 'id': 18},
         {'web_id': b'suvd', 'id': 19}]
    t = ListHelper.decode_v(s)
    print(t)

    pass
