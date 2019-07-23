# -*- coding: utf-8 -*-
import json
import pickle

import XX.String.StringHelper as String
import requests
from XX.File.FileHelper import *
from XX.Model.Object.ResponseObj import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestHelper(object):
    @staticmethod
    def SendRequest(url, *arg, **kw):
        response = ResponseObj()
        response.status_code = 0
        response.status = 0
        method = str(kw["method"]).lower() if "method" in kw.keys() else "get"
        kw = dict(kw)
        response.url = url
        data = kw["data"] if "data" in kw.keys() else None
        headers = kw["headers"] if "headers" in kw.keys() else None
        cookies = kw["cookies"] if "cookies" in kw.keys() else None
        proxies = kw["proxies"] if "proxies" in kw.keys() else None
        timeout = kw["timeout"] if "timeout" in kw.keys() else None
        verify = kw["verify"] if "verify" in kw.keys() else True
        allow_redirects = kw["allow_redirects"] if "allow_redirects" in kw.keys() else True
        try:
            if method.lower() == "get":
                req = requests.get(url, data=data, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=verify, allow_redirects=allow_redirects)
            elif method.lower() == "post":
                req = requests.post(url, data=data, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=verify, allow_redirects=allow_redirects)
            elif method.lower() == "head":
                req = requests.head(url, data=data, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=verify, allow_redirects=allow_redirects)
            elif method.lower() == "delete":
                req = requests.delete(url, data=data, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=verify, allow_redirects=allow_redirects)
            elif method.lower() == "put":
                req = requests.put(url, data=data, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=verify, allow_redirects=allow_redirects)
            elif method.lower() == "options":
                req = requests.options(url, data=data, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=verify, allow_redirects=allow_redirects)
            elif method.lower() == "patch":
                req = requests.patch(url, data=data, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=verify, allow_redirects=allow_redirects)
            else:
                print(" == Unsupport method : " + str(method))
                response.msg = "unsupport method."
                response.method = method
                return response
            response.status = response.status_code = req.status_code
            response.text = req.text
            if kw.get("serialization_type") == "json":
                try:
                    response.text = req.json()
                except:
                    response.msg = "Response is not json!"
                    pass
            response.cookies = requests.utils.dict_from_cookiejar(req.cookies)
            response.RequestHeaders = headers
            response.encoding = req.encoding
            response.ResponseHeaders = dict(req.headers)
            response.headers = response.ResponseHeaders
            if 500 <= req.status_code < 600:
                response.msg = "500-600"
            elif 400 >= req.status_code >= 200:
                response.msg = "successful" + response.msg if response.msg else ""
            else:
                response.msg = "Not normal status"
        except Exception as e:
            traceback.print_exc()
            response.status = response.status_code = 0
            response.msg = "Time out!"
        return response

    # 删除缓存，重新请求
    @staticmethod
    def SendRefreshCacheRequest(url, *arg, **kw):
        # 写缓存
        resp = RequestHelper.SendRequest(url, *arg, **kw)
        if resp.status_code <= 300:
            try:
                FileHelper.mkdir(FileHelper.getFilePathAndName(kw.get("save_path"))[0])
                if kw.get("save_html"):
                    open(kw.get("save_path") + ".xhtml", "w", encoding="utf-8").write(resp.text)
                    if kw.get("serialization_type") == "json":
                        json.dump(String.bytes2str(resp.__dict__), open(kw.get("save_path"), "w", encoding="utf-8"), ensure_ascii=False)
                else:
                    resp.cache = 1
                    pickle.dump(resp, open(kw.get("save_path"), "wb"))
                return resp
            except:
                traceback.print_exc()
                print("===Can't dump html file to >> " + str(kw.get("save_path")))
        else:
            return resp

    @staticmethod
    # 缓存文件请求
    def SendCacheRequest(url, *arg, **kw):
        # 要缓存，没文件，或者文件为空
        resp = ResponseObj()
        if kw.get("save_path") and os.path.isfile(kw.get("save_path")) and os.path.getsize(kw.get("save_path")):
            try:
                if kw.get("serialization_type") == "json":
                    resp.__dict__ = dict(json.load(open(kw.get("save_path"), encoding="utf-8")))
                    resp.__dict__["cache"] = 1
                else:
                    resp = pickle.load(open(kw.get("save_path"), "rb"))
                    resp.cache = 2
            except:
                traceback.print_exc()
                resp.msg = "Failed to read cached content!"
        else:
            resp = RequestHelper.SendRefreshCacheRequest(url, *arg, **kw)
        return resp

    @staticmethod
    # 检测缓存文件是否存在
    def SendCheckRequest(url, *arg, **kw):
        if kw.get("save_path") and os.path.isfile(kw.get("save_path")) and os.path.getsize(kw.get("save_path")):
            return 1

    @staticmethod
    def AsyncRequest(urls, err_callback=None, pool_size=5, *args, **kw):
        import grequests
        tasks = [grequests.get(u, **kw) for u in urls]
        return grequests.map(tasks, size=pool_size, exception_handler=err_callback)

    @staticmethod
    def TryRequestUrl(url, *arg, **kw):
        try_time_level = kw["try_time_level"] if "try_time_level" in kw.keys() else 5
        try_times = kw["try_times"] if "try_times" in kw.keys() else 0
        try_ts = kw["try_ts"] if "try_ts" in kw.keys() else 0.01
        kw["try_times"] = try_times
        time.sleep(try_times * try_ts)
        response = RequestHelper.SendCacheRequest(url, *arg, **kw)
        if response:
            if 400 <= response.status <= 600:
                kw["try_times"] += 1
                print(" =" + str(response.status) + "= ", end="")
                if try_time_level and kw["try_times"] >= try_time_level:
                    return response
                RequestHelper.TryRequestUrl(url, *arg, **kw)
            else:
                return response
        else:
            print("No response")
            return None
        return response

    @staticmethod
    def Pick2Html(pick_path, html_path=""):
        import pickle
        try:
            resp = pickle.load(open(pick_path, "rb"))
            if not html_path:
                html_path = pick_path.split(".")[0] + ".html"
            open(html_path, "w", encoding="utf-8").write(resp.text)
        except:
            return


if __name__ == "__main__":
    url = "https://www.baidu.com/?tn=98010089_dg"
    save_path = "E:\\baidu.pick"
    req = RequestHelper.TryRequestUrl(url, save_path=save_path, refresh=1, verify=False, method="get")
