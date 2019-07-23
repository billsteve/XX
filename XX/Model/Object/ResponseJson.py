# -*- coding:utf-8 -*-
import json


# 服务端生成的response json结构封装
class ResponseJson(object):
    data = None
    code = 0
    msg = ""

    def __init__(self, data=None, code=0, msg="", status="ok", *arg, **kw):
        self.data = data
        self.code = code
        self.msg = msg

    @staticmethod
    def getResponseJson(data=None, code=0, msg="", resformat="dict", status="ok", *arg, **kw):
        if not msg:
            if code == 0:
                msg = "ok"
            else:
                msg = "err"

        responseJson = {"data": data, "code": code, "msg": msg}
        if resformat == "dict":
            return responseJson
        elif resformat == "str":
            return json.dumps(responseJson, ensure_ascii=False)
        else:
            return responseJson


if __name__ == "__main__":
    res = ResponseJson()
    print(res.__dict__)
    pass
