# -*- encoding:utf8 -*-
import json
import random
import traceback

import redis

import XX.Date.DatetimeHelper as Dt
import XX.HTTP.RequestsHelper as Rh
from XX.Debug import *


# 阿布云
def get_proxy(un="H76Z3LKO67NRN5QD", pwd="272305BABB9380E1", profession=False) -> dict:
    # 代理隧道验证信息
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": "http-dyn.abuyun.com",
        "port": "9010" if profession else "9020",
        "user": un,
        "pass": pwd,
    }
    return {"http": proxyMeta, "https": proxyMeta}


def get_random_proxy(r):
    ips = r.keys()
    while 1:
        if ips:
            ip = random.choice(ips)
            proxies = {
                "http": ip,
                "https": ip,
            }
            return proxies
        else:
            print("No more ip redis")
            time.sleep(1)
            continue


def add_tai_yang(redis_host="127.0.0.1", db=11):
    r = redis.Redis(redis_host, db=db)
    url = "http://http-api.taiyangruanjian.com/getip?num=1&type" \
          "=2&pro=&city=0&yys=0&port=11&pack=13604&ts=1&ys=0&cs=0&lb=1&sb=0&pb=4&mr=0&regions="
    while True:
        time.sleep(1)
        if r.dbsize() < 3:
            resp = Rh.RequestHelper.send_cache_request(url)
            if resp.status == 200:
                try:
                    json_data = json.loads(resp.text)
                    if json_data["code"] == 0:
                        ip = str(json_data["data"][0]["ip"]) + ":" + str(json_data["data"][0]["port"])
                        ets = int(Dt.str_to_ts(json_data["data"][0]["expire_time"]) - time.time() + 1)
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


def add_mivip_proxy(conn_redis, api=None, size=20):
    while 1:
        if conn_redis.dbsize() < size:
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


def get_zhima_proxy(r):
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


def add_zhima(r):
    url = "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=15624&ts=1&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    while True:
        time.sleep(1)
        if r.dbsize() < 2:
            resp = Rh.RequestHelper.send_cache_request(url)
            if resp.status == 200:
                try:
                    json_data = json.loads(resp.text)
                    if json_data["code"] == 0:
                        ip = str(json_data["data"][0]["ip"]) + ":" + str(json_data["data"][0]["port"])
                        ets = int(Dt.str_to_ts(json_data["data"][0]["expire_time"]) - time.time() + 1)
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


def test_ip():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5005.400 QQBrowser/10.0.923.400"
    }
    while 1:
        proxy = get_random_proxy()
        if proxy:
            urls = list()
            urls.append("https://www.baidu.com")
            urls.append("https://www.qq.com")
            for url in urls:
                try:
                    req = requests.get(url, proxies=proxy, timeout=5, headers=headers)
                    if req.status_code != 200:
                        # TODO：删除代理
                        pass
                    time.sleep(1)
                except:
                    print("time out" + url)
        else:
            p(" wrong proxy", line="-----")


def get_proxy_by_ip(ip, port):
    proxies = {
        "http": f"{ip}:{port}",
        "https": f"{ip}:{port}",
    }
    return proxies


get_abuyun_proxy = get_proxy

if __name__ == '__main__':
    proxy = get_abuyun_proxy("H98KW9664832F56D", "22E8C0DE197A4C7E")
    import requests

    r = requests.get("https://www.jd.com/", proxies=proxy)
    print(r.status_code)
