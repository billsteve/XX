#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/10 22:54
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Help.py
# @Software : PyCharm


# 根据json生成sql
def getSqlByDict(d, tb_name="tb_name", tb_comment="COMMENT"):
    s = "\n\nCREATE TABLE `{tb_name}` (\n`id` int(11) NOT NULL AUTO_INCREMENT,\n\n".format(tb_name=tb_name)
    for k, v in d.items():
        if type(v) in [int, float]:
            s += """\t`{key}` int(11) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
        elif type(v) == list:
            s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
        elif type(v) == dict:
            if v.get("id"):
                s += """\t`{key}_web_id`  varchar(255) DEFAULT NULL,""".format(key=k) + "\n"
                print(":WebWebWebWebWeb")
            else:
                s += """\t`{key}` longtext DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
        else:
            s += """\t`{key}` varchar(255) DEFAULT NULL,""".format(key=k if str(k) != "id" else "web_id") + "\n"
    s += """
        `is_del` int(11) DEFAULT 0,
        `update_ts` int(11) DEFAULT NULL,
        `create_ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='{tb_comment}';""".format(tb_comment=tb_comment)
    print(s)


def getCreateTableSqlBySqlDump(fp):
    for line in open(fp, "r", encoding="utf-8"):
        if line.find("INSERT") >= 0 or line.find("--") >= 0 or line.find("/*") >= 0:
            continue
        print(line.strip())


def delRedisKeysByPrefix(prefix, conn):
    for key in conn.keys():
        if str(key).startswith(prefix):
            conn.delete(key)
            print(key)

def getColumnsByDDL(ddl):
    


if __name__ == '__main__':
    d = {'url': 'https://www.baidu.com/s?ie=utf8&oe=utf8&wd=%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0&tn=98010089_dg&ch=2', 'crawl_ts': 1557479433, 'create_ts': '2019-05-10 17:10:33', 'real_url': 'http://www.tjlsty.com.cn/Home/Product/index/pid/3.html#cur_pro', 'snapshot_url': 'http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8keayRouCCa3UvfSC4zodAur9WJD614Ui34sRpxjQjxy9ho1ZPmq7XRjQUGzcBbr02fzKbd8LXc1erKSs-uUxPUdk2D2EnY2ujHbOo4nEBUcjmoBRxYSRQ_Khmjcu8ZR_Zt-38ZyFrOvvX0CEtLzN67PBwXBhe2eLEkNwYEAhWYbeBKf-ipcQ9JgjAYoSJAa4s.Db_a9-CkYP7nZeeV2m5wKV6k3Cr55OCf3F8gYoDkEvyNvyUPOQIJyAp7BEW342d0.U1YY0ZDqEraOvnpq1260mywkXHvt3QOmkoLnJ0K9uZ7Y5Hc0TA-W5H00Ijvt3QOm1egP_sKGUHYznjf0u1dEugK1nfKdpHdBmy-bIykV0ZKGujY10APGujYYnH60UgfqnH0krNtknjDLg1nknWwxn1msnfKopHYs0ZFY5HcsP0K-pyfqnHfYn-tznH03r7tzrjRkr7tzrjTLPNtzrjTzn7tzrjbvP7tzrj61PdtzrjR3PfKBpHYznjwxnHRd0AdW5HDsnj7xrjczPjfsnjnsg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qnWbYn101PH030A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Yz0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKYIgnqnW64nHcvn1n4PHfYnjb4nWmYPsKzug7Y5HDdPHTYP1T1nWbsPWn0Tv-b5H9WuyP-rAcvnj0snhDsuhf0mLPV5Rn3PWFDPHcvPRf3wRDdfHn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tzP1fvrjf4g100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0sn0KWThnqnHmLPWT&word=%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0', 'title': '天津联盛天远监控系统_全程一体化服务 '}


    getSqlByDict(d)
