# -*- encoding:utf8 -*-
import requests
import json
import multiprocessing
import random
import traceback

import XX.Date.DatetimeHelper as tsh
import XX.HTTP.RequestsHelper as reqh
import XX.DB.RedisHelper as RH
import redis
import requests
from XX.Tools.Debug import *


# 阿布云大代理
def getProxy(un="H76Z3LKO67NRN5QD", pwd="272305BABB9380E1"):
    # # 代理服务器------------------------------
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = un
    proxyPass = pwd

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    # # -----------------------------------------
    return proxies


def changeProxy():
    pass


def getTaiYangProxy(redis_host="127.0.0.1", db=11):
    r = redis.Redis(redis_host, db=db)
    p = multiprocessing.Process(target=addTaiYang, args=(None,))
    p.daemon = True
    p.start()
    p.join()
    ips = r.keys()
    if ips:
        ip = random.choice(ips)
        proxies = {
            "http": ip,
            "https": ip,
        }
        return proxies
    else:
        print("No more ip in taiyang proxy(db11)")
        return None


def addTaiYang(redis_host="127.0.0.1", db=11):
    r = redis.Redis(redis_host, db=db)
    url = "http://http-api.taiyangruanjian.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&pack=13604&ts=1&ys=0&cs=0&lb=1&sb=0&pb=4&mr=0&regions="
    while True:
        time.sleep(1)
        if r.dbsize() < 3:
            resp = reqh.RequestsHelper.RequestUrl(url)
            if resp.status == 200:
                try:
                    json_data = json.loads(resp.text)
                    if json_data["code"] == 0:
                        ip = str(json_data["data"][0]["ip"]) + ":" + str(json_data["data"][0]["port"])
                        ets = int(tsh.strToTs(json_data["data"][0]["expire_time"]) - time.time() + 1)
                        d("OK " + json_data["data"][0]["expire_time"] + " ====== now + " + str(ets // 60), line1="===")
                        r.set(ip, 0, ex=ets)
                        time.sleep(1)
                except:
                    print("not json data" + resp.text)
                    traceback.print_exc()
            else:
                print("proxy return error" + str(resp.text))
        else:
            break
    return 1


def addMivipProxy(r_cfg, api=None):
    conn_redis = RH.RedisHelper.getRedisConnectByCfg(r_cfg)
    while 1:
        if conn_redis.dbsize() < 50:
            try:
                req = requests.get(api, timeout=5)
                if req.status_code == 200:
                    json_data = json.loads(req.text)
                    ips = json_data.get("result")
                    if ips:
                        for ip in ips:
                            conn_redis.set(ip["ip:port"], 0, ip["time_avail"])
                            print("Add proxy" + str(ip["ip:port"]))
                    else:
                        print("No ip" + req.text)
                else:
                    print(req.status_code)
            except:
                traceback.print_exc()
        else:
            print("Too Much proxy")
        time.sleep(10)


def getZhimaProxy(redis_host="127.0.0.1", db=11):
    r = redis.Redis(redis_host, db=db)
    # p = multiprocessing.Process(target=addZhima, args=(None,))
    # p.daemon = True
    # p.start()
    # p.join()
    ips = r.keys()
    if ips:
        ip = random.choice(ips)
        proxies = {
            "http": ip,
            "https": ip,
        }
        return proxies
    else:
        print("No more ip in taiyang proxy(db11)")
        return None


def addZhima(redis_host="127.0.0.1", db=11):
    r = redis.Redis(redis_host, db=db)
    url = "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=15624&ts=1&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    while True:
        time.sleep(1)
        if r.dbsize() < 2:
            resp = reqh.RequestsHelper.RequestUrl(url)
            if resp.status == 200:
                try:
                    json_data = json.loads(resp.text)
                    if json_data["code"] == 0:
                        ip = str(json_data["data"][0]["ip"]) + ":" + str(json_data["data"][0]["port"])
                        ets = int(tsh.strToTs(json_data["data"][0]["expire_time"]) - time.time() + 1)
                        d("OK " + json_data["data"][0]["expire_time"] + " ====== now + " + str(ets // 60), line1="===")
                        r.set(ip, 0, ex=ets)
                        time.sleep(1)
                    else:
                        print(json_data)
                except:
                    print("not json data" + resp.text)
                    traceback.print_exc()
            else:
                print("proxy return error" + str(resp.text))
        else:
            print("Enough")
            time.sleep(10)


def getDB11Proxy(redis_host="127.0.0.1", db=11):
    r = redis.Redis(redis_host, db=db)
    ips = r.keys()
    if ips:
        ip = random.choice(ips)
        proxies = {
            "http": ip,
            "https": ip,
        }
        return proxies
    else:
        print("No more ip in taiyang proxy(db11)")
        return None


def testIP():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5005.400 QQBrowser/10.0.923.400"
    }
    while 1:
        PROXIES = getZhimaProxy()
        if PROXIES:
            urls = []
            urls.append("https://www.baidu.com/?tn=98010089_dg")
            urls.append("http://www.qichacha.com/")
            urls.append("http://www.gsxt.gov.cn/index.html")
            urls.append("https: // www.csdn.net /")
            for url in urls:
                try:
                    req = requests.get(url, proxies=PROXIES, timeout=5, headers=headers)
                    print(req.status_code)
                    time.sleep(1)
                except:
                    print("time out" + url)
        else:
            p(" wrong proxy", line="-----")


def getProxyByIP(ip):
    proxies = {
        "http": ip,
        "https": ip,
    }
    return proxies


if __name__ == "__main__":
    import random
    from XX.Model.Struct.RedisConn import ali_cfg

    ali_cfg["db"] = 9
    api = "https://proxyapi.mimvp.com/api/fetchsecret.php?orderid=867050512125280583&num=50&http_type=3&result_fields=1,3&result_sort_field=2&result_format=json"
    addMivipProxy(ali_cfg, api=api)
    exit()
