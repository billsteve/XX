#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/10 22:54
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Help.py
# @Software : PyCharm



def del_redis_keys_by_prefix(prefix, conn):
    for key in conn.keys():
        if str(key).startswith(prefix):
            conn.delete(key)
            print(key)


if __name__ == '__main__':
    d = {'url': 'https://www.baidu.com/s?ie=utf8&oe=utf8&wd=%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0&tn=98010089_dg&ch=2', 'crawl_ts': 1557479433, 'create_ts': '2019-05-10 17:10:33',
         'real_url': 'http://www.tjlsty.com.cn/Home/Product/index/pid/3.html#cur_pro',
         'snapshot_url': 'http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8keayRouCCa3UvfSC4zodAur9WJD614Ui34sRpxjQjxy9ho1ZPmq7XRjQUGzcBbr02fzKbd8LXc1erKSs-uUxPUdk2D2EnY2ujHbOo4nEBUcjmoBRxYSRQ_Khmjcu8ZR_Zt-38ZyFrOvvX0CEtLzN67PBwXBhe2eLEkNwYEAhWYbeBKf-ipcQ9JgjAYoSJAa4s.Db_a9-CkYP7nZeeV2m5wKV6k3Cr55OCf3F8gYoDkEvyNvyUPOQIJyAp7BEW342d0.U1YY0ZDqEraOvnpq1260mywkXHvt3QOmkoLnJ0K9uZ7Y5Hc0TA-W5H00Ijvt3QOm1egP_sKGUHYznjf0u1dEugK1nfKdpHdBmy-bIykV0ZKGujY10APGujYYnH60UgfqnH0krNtknjDLg1nknWwxn1msnfKopHYs0ZFY5HcsP0K-pyfqnHfYn-tznH03r7tzrjRkr7tzrjTLPNtzrjTzn7tzrjbvP7tzrj61PdtzrjR3PfKBpHYznjwxnHRd0AdW5HDsnj7xrjczPjfsnjnsg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qnWbYn101PH030A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Yz0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKYIgnqnW64nHcvn1n4PHfYnjb4nWmYPsKzug7Y5HDdPHTYP1T1nWbsPWn0Tv-b5H9WuyP-rAcvnj0snhDsuhf0mLPV5Rn3PWFDPHcvPRf3wRDdfHn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tzP1fvrjf4g100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0sn0KWThnqnHmLPWT&word=%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0',
         'title': '天津联盛天远监控系统_全程一体化服务 '}
    d = {
        "albumname": "周杰伦的床边故事",
        "publishtime": "2016-06-24 00:00:00",
        "singername": "周杰伦",
        "intro": "夜深了，猫头鹰出没，数完第一千零一个尖叫声，开始听，周杰伦 的床边故事，Jay Chou’s Bedtime Stories，今年最令人激动的乐坛震撼弹，周杰伦2016年最新着魔专辑强势暗袭你的床边！超乎想象、最自由的古典灵魂摇滚嘻哈，听周杰伦说书！10个出神入化的音乐故事。",
        "songcount": 0,
        "imgurl": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20160623\/20160623233610830051.jpg",
        "albumid": 1645030,
        "collectcount": 0,
        "singerid": 3520,
        "sextype": 0,
        "privilege": 10,
        "trans_param": {
            "special_tag": "0"
        }
    }
