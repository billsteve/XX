# -*- coding:utf-8 -*-
import json

import XX.File.FileHelper as cf


class UrlInfoHelper(object):

    # json str 2 redis。把异常的url记录下来,并把缓存删了
    @staticmethod
    def add2redis(url_info, redis_key, redis_conn, del_cache=0, spider="", get_url_cache_path=None, unique_url=None):
        try:
            redis_conn.rpush(redis_key, json.dumps(url_info))
        except:
            print("==UrlInfoHelper->Add redis is wrong")
        if del_cache:
            cache_fp = get_url_cache_path(unique_url(url_info.get("url")), spider=spider)
            if cf.FileHelper.is_file_exit(cache_fp):
                print("Remove cache file + " + cache_fp + "\t url  is " + url_info.get("url"))
                cf.FileHelper.remove_file(cache_fp)
            else:
                print("=====Cache is not exists========" + cache_fp)
        else:
            print("--" * 50, flush=True)


if __name__ == '__main__':
    pass
