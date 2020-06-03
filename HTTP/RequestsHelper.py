# -*- coding: utf-8 -*-
import json
import pickle

import requests
from logzero import logger
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import XX.Encrypt.EncryptHelper as Enc
import XX.String.StringHelper as String
from XX.File.FileHelper import *
from XX.Model.Object.ResponseObj import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestHelper(object):
    @staticmethod
    def send_request(url, **kw):
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
        json_ = kw["json"] if "json" in kw.keys() else None
        allow_redirects = kw["allow_redirects"] if "allow_redirects" in kw.keys() else True
        try:
            if method.lower() in ["get", "post", "head", "delete", "put", "options", 'patch']:
                func = getattr(requests, method.lower())
            else:
                logger.debug(f" == Unsupported  method : {method}")
                response.msg = f"unsupported method : {method}."
                response.method = method
                return response
            request = func(url, data=data, headers=headers, cookies=cookies, proxies=proxies,
                           timeout=timeout, verify=verify, allow_redirects=allow_redirects, json=json_)
            response.status = response.status_code = request.status_code
            response.text = request.text
            if kw.get("serialization_type") == "json":
                try:
                    response.text = request.json()
                except Exception as e:
                    response.msg = f"Response is not json! Exception : {e}"
                    pass
            if request.cookies:
                response.cookies = requests.utils.dict_from_cookiejar(request.cookies)
            response.RequestHeaders = headers
            response.encoding = request.encoding
            response.data = data
            response.json = json_
            if request.headers:
                response.ResponseHeaders = dict(request.headers)
            response.headers = response.ResponseHeaders
            if 500 <= request.status_code < 600:
                response.msg = "500-600"
            elif 400 >= request.status_code >= 200:
                response.msg = "successful" + response.msg if response.msg else ""
            else:
                response.msg = "Not normal status"
        except Exception as e:
            traceback.print_exc()
            response.status = response.status_code = 0
            response.msg = f"Time out!  Exception : {e}"
        return response

    # 删除缓存，重新请求
    @staticmethod
    def send_refresh_cache_request(url, *arg, **kw):
        # 写缓存
        if kw.get("save_path"):
            FileHelper.remove_file(kw.get("save_path"))
            # logger.info("Delete old cache file ")
        resp = RequestHelper.send_request(url, *arg, **kw)
        if resp.status_code <= 300:
            try:
                FileHelper.mkdir(FileHelper.get_file_path_and_name(kw.get("save_path"))[0])
                # 保存HTML
                if kw.get("save_html"):
                    open(kw.get("save_path") + ".xhtml", "w", encoding="utf-8").write(resp.text)
                    if kw.get("serialization_type") == "json":
                        _ = open(kw.get("save_path"), "w", encoding="utf-8")
                        json.dump(String.bytes2str(resp.__dict__), _, ensure_ascii=False)
                else:
                    resp.cache = 1
                    resp.cache_file = kw.get("save_path")
                    if kw.get("save_path") and resp.text:
                        pickle.dump(resp, open(kw.get("save_path"), "wb"))
                    else:
                        # logger.debug(f"Don't save. No HTML or no cache_path .Code is {resp.status_code}")
                        pass
                return resp
            except Exception as e:
                traceback.print_exc()
                logger.debug("===Can't dump html file to >> " + str(kw.get("save_path")) + f"    {e}")
        else:
            # logger.debug(f"Not 200:{resp.status_code}.  {url}")
            return resp

    # 缓存文件请求
    @staticmethod
    def send_cache_request(url, *arg, **kw):
        resp = ResponseObj()
        del_cache_out_ts = kw["del_cache_out_ts"] if "del_cache_out_ts" in kw.keys() else None

        def out_time(fp=kw.get("save_path"), ts=del_cache_out_ts) -> bool:
            # 没设置过期时间
            if not ts:
                return False
            # 文件不存在
            if not FileHelper.is_file_exit(fp):
                return True
            if time.time() - FileHelper.get_create_ts(fp) > ts:
                return True
            return False

        # 存在，且不过期
        if kw.get("save_path") and os.path.isfile(kw.get("save_path")) and os.path.getsize(
                kw.get("save_path")) and not out_time():
            try:
                if kw.get("serialization_type") == "json":
                    resp.__dict__ = dict(json.load(open(kw.get("save_path"), encoding="utf-8")))
                    resp.__dict__["cache"] = 2
                    resp.__dict__["cache_file"] = kw.get("save_path")
                else:
                    try:
                        resp = pickle.load(open(kw.get("save_path"), "rb"))
                        resp.cache = 2
                        resp.cache_file = kw.get("save_path")
                        if not resp.text:
                            return RequestHelper.send_refresh_cache_request(url, *arg, **kw)
                    except Exception as e:
                        traceback.print_exc()
                        resp.msg = f"Failed to unpickle cached content: {e}!"
            except Exception as e:
                traceback.print_exc()
                resp.msg = f"Failed to read cached content: {e}!"
        else:
            resp = RequestHelper.send_refresh_cache_request(url, *arg, **kw)
        return resp

    @staticmethod
    # 检测缓存文件是否存在
    def send_check_request(url, *arg, **kw):
        if kw.get("save_path") and os.path.isfile(kw.get("save_path")) and os.path.getsize(kw.get("save_path")):
            return 1

    @staticmethod
    def async_request(urls, err_callback=None, pool_size=5, *args, **kw):
        import grequests
        tasks = [grequests.get(u, **kw) for u in urls]
        return grequests.map(tasks, size=pool_size, exception_handler=err_callback)

    @staticmethod
    def try_request_url(url, *arg, **kw):
        try_time_level = kw["try_time_level"] if "try_time_level" in kw.keys() else 5
        try_times = kw["try_times"] if "try_times" in kw.keys() else 0
        try_ts = kw["try_ts"] if "try_ts" in kw.keys() else 0.01
        kw["try_times"] = try_times
        time.sleep(try_times * try_ts)
        response = RequestHelper.send_cache_request(url, *arg, **kw)
        if response:
            if 400 <= response.status_code <= 600:
                kw["try_times"] += 1
                logger.debug(" =" + str(response.status_code) + "= ")
                if try_time_level and kw["try_times"] >= try_time_level:
                    return response
                RequestHelper.try_request_url(url, *arg, **kw)
            else:
                return response
        else:
            logger.debug("No response")
            return None
        return response

    @staticmethod
    def pick_2_html(pick_path, html_path=""):
        import pickle
        try:
            resp = pickle.load(open(pick_path, "rb"))
            if not html_path:
                html_path = pick_path.split(".")[0] + ".html"
            open(html_path, "w", encoding="utf-8").write(resp.text)
        except Exception as e:
            return


def cache_response(response, roo_path=None):
    if hasattr(response, "cache_file") and response.cache_file:
        pickle.dump(response, open(response.cache_file, "wb"))
    else:
        fp = roo_path + FileHelper.get_md5_name(response.url + Enc.Encrypt.md5(str(response.headers))) + ".pickle"
        FileHelper.mkdir(FileHelper.get_file_path_and_name(fp)[0])
        pickle.dump(response, open(fp, "wb"))
    return 1


if __name__ == "__main__":
    # url = "https://www.baidu.com/?tn=98010089_dg"
    # save_path = "E:\\baidu.pick"
    # req = RequestHelper.try_request_url(url, save_path=save_path, refresh=1, verify=False, method="get")
    # response = ResponseObj(status_code=0, url="1.com", headers={"kl": "v2"})
    # r = cache_response(response, roo_path="./")
    pass
