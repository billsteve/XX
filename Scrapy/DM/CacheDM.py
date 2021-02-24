# -*- coding: utf-8 -*-
import os
import pickle
import time
import traceback
from typing import Union

import happybase
from logzero import logger
from scrapy.http import Request
from scrapy.http import TextResponse, Response

import XX.Encrypt.EncryptHelper as Enc
from XX.Date.DatetimeHelper import get_today, get_this_month
from XX.File.FileHelper import FileHelper as Fh
from XX.HTML.UrlHelper import UrlHelper as Uh

process_request_type = Union[None, Response, Request]
process_response_type = Union[Response, Request]


# 文件缓存中间件
class CacheFileRequest(object):
    @staticmethod
    def get_cache_file(*args, **kwargs):
        spider = kwargs.get("spider")
        url = kwargs.get("url")
        request = kwargs.get("request", {})
        method = "get"
        if request:
            method = request.method
            body = request.body.decode("utf-8")
            # print("POST 缓存")
        else:
            # print("----No request")
            pass
        root_path_cache = kwargs.get("root_path_cache", "./")
        spider = spider if spider else Uh.get_domain(url).replace(".", "_")
        if method.lower() == "post":
            return root_path_cache + spider + os.sep + Fh.get_md5_name(url + "_" + body) + ".cache"
        else:
            return root_path_cache + spider + os.sep + Fh.get_md5_name(url) + ".cache"

    @classmethod
    def from_crawler(cls, crawler):

        settings = crawler.settings
        cls.cache_file_path_func = settings.get("FUN_CACHE_FILE_PATH", cls.get_cache_file)
        cls.cache_file_exclude = settings.get("CACHE_FILE_EXCLUDE")
        cls.cache_file_ts = settings.get("CACHE_FILE_TS", None)
        cls.cache_file_exclude_ts = settings.get("CACHE_FILE_EXCLUDE_TS", cls.cache_file_ts)
        cls.settings = settings
        return cls()

    def process_request(self, request, spider) -> process_request_type:
        cache_file_path = self.cache_file_path_func(
            url=str(request.url), spider=str(spider.name),
            root_path_cache=self.settings.get("ROOT_PATH_CACHE"),
            request=request)

        # 是否应该读缓存
        def should_read_cache(request, spider) -> bool:
            # 存在缓存文件
            exists_file = Fh.is_file_exit(cache_file_path)
            # 是排除URL
            exclude = 1 if self.cache_file_exclude and request.url.find(self.cache_file_exclude) >= 0 else 0
            if exists_file:
                if exclude:
                    if self.cache_file_exclude_ts >= 0:

                        if time.time() - Fh.get_update_ts(cache_file_path) < self.cache_file_exclude_ts:
                            return True
                        else:
                            logger.debug(
                                f"缓存文件过期。不读取。{cache_file_path}{Fh.get_update_ts(cache_file_path)}  {request.url}")
                            return False
                    # 排除URL无过期时间,就是排除URL都不读缓存
                    else:
                        logger.debug(f"排除的，没设置过期时间，全不读缓存。{request.url}")
                        return False
                else:
                    # 全部时间
                    if self.cache_file_ts:
                        # 全部URL 没有过期
                        if time.time() - Fh.get_update_ts(cache_file_path) < self.cache_file_ts:
                            return True
                        else:
                            logger.debug(f"== OUT TIME，不读缓存。{request.url}")
                            return False
                    else:
                        return True
            else:
                # logger.debug(f"缓存文件不存在。 {request.url}")
                return False

        if should_read_cache(request, spider):
            try:
                logger.info(f"===Read cache===  {cache_file_path.split(os.sep)[-1]}   {request.url}")
                return pickle.load(open(cache_file_path, "rb"))
            except Exception as e:
                logger.info(f"== Can't Read cache ===  Reason is {e}")
                Fh.remove_file(cache_file_path)
                traceback.print_exc()
        else:
            # 不读缓存
            # logger.info("===Should Not Read Cache===   " + request.url)
            pass

    # 写文件缓存
    def process_response(self, request, response, spider) -> process_response_type:
        cache_file_path = self.cache_file_path_func(
            url=str(request.url), spider=str(spider.name),
            root_path_cache=self.settings.get("ROOT_PATH_CACHE"),
            request=request)

        # 是否应该重写缓存
        def should_write_cache(request, spider) -> bool:
            exists_file = Fh.is_file_exit(cache_file_path)
            exclude = 1 if self.cache_file_exclude and request.url.find(self.cache_file_exclude) >= 0 else 0
            if exists_file:
                if exclude:
                    if self.cache_file_exclude_ts:
                        if time.time() - Fh.get_update_ts(cache_file_path) > self.cache_file_exclude_ts:
                            logger.debug(
                                f"排除缓存文件过期。需要重写。{cache_file_path}{Fh.get_update_ts(cache_file_path)}  {request.url}")
                            return True
                        else:
                            logger.debug(
                                f"排除的URL没过期，不重写。过了{int(time.time() - Fh.get_update_ts(cache_file_path))} 秒？ {cache_file_path}")
                            return False
                    else:
                        logger.debug(f"排除URL没设置过期时间 都要重写。 {cache_file_path}")
                        return True
                else:
                    # logger.debug(f"不是排除的URL不重写缓存。 {cache_file_path}")
                    return False
            else:
                logger.debug(f"缓存文件不存在。写缓存。 {request.url}")
                return True

        if response.status < 300:
            Fh.mkdir(Fh.get_file_path_and_name(cache_file_path)[0])
            try:
                if should_write_cache(request, spider):
                    if hasattr(response, "certificate"):
                        del response.certificate
                    res = Fh.remove_file(cache_file_path)
                    pickle.dump(response, open(cache_file_path, "wb"))
                    logger.info(f"===Write cache===      {cache_file_path}   {request.url}")
                # else:
                #     logger.info(f"===Cache Exists===      {cache_file_path}   {request.url}")
            except Exception as e:
                logger.info(f"== Can't Write cache 2 file==   Reason is {e}")
                Fh.remove_file(cache_file_path)
                # traceback.print_exc()
        else:
            logger.info(f"===Status Code ERROR ===   Code is {response.status} " + response.url)
        return response


# 文件按天缓存中间件
class CacheFilePerDayRequest(object):
    @staticmethod
    def get_cache_file(*args, **kwargs):
        spider = kwargs.get("spider")
        url = kwargs.get("url")
        request = kwargs.get("request", {})
        method = "get"
        if request:
            method = request.method
            body = request.body.decode("utf-8")
            # print("POST 缓存")
        else:
            # print("----No request")
            pass
        root_path_cache = kwargs.get("root_path_cache", "./")
        spider = spider if spider else Uh.get_domain(url).replace(".", "_")
        if method.lower() == "post":
            return root_path_cache + spider + os.sep + get_today().replace("-", '_') + os.sep + Fh.get_md5_name(url + "_" + body) + ".cache"
        else:
            return root_path_cache + spider + os.sep + get_today().replace("-", '_') + os.sep + Fh.get_md5_name(url) + ".cache"

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.cache_file_path_func = settings.get("FUN_CACHE_FILE_PATH", cls.get_cache_file)
        cls.cache_file_exclude = settings.get("CACHE_FILE_EXCLUDE")
        cls.cache_file_ts = settings.get("CACHE_FILE_TS", None)
        cls.cache_file_exclude_ts = settings.get("CACHE_FILE_EXCLUDE_TS", cls.cache_file_ts)
        cls.settings = settings
        return cls()

    def process_request(self, request, spider) -> process_request_type:
        cache_file_path = self.cache_file_path_func(
            url=str(request.url), spider=str(spider.name),
            root_path_cache=self.settings.get("ROOT_PATH_CACHE"),
            request=request)

        # 是否应该读缓存
        def should_read_cache(request, spider) -> bool:
            # 存在缓存文件
            exists_file = Fh.is_file_exit(cache_file_path)
            # 是排除URL
            exclude = 1 if self.cache_file_exclude and request.url.find(self.cache_file_exclude) >= 0 else 0
            if exists_file:
                if exclude:
                    if self.cache_file_exclude_ts >= 0:
                        if time.time() - Fh.get_update_ts(cache_file_path) < self.cache_file_exclude_ts:
                            return True
                        else:
                            logger.debug(
                                f"缓存文件过期。不读取。{cache_file_path}{Fh.get_update_ts(cache_file_path)}  {request.url}")
                            return False
                    # 排除URL无过期时间,就是排除URL都不读缓存
                    else:
                        logger.debug(f"排除的，没设置过期时间，全不读缓存。{request.url}")
                        return False
                else:
                    # 全部时间
                    if self.cache_file_ts:
                        # 全部URL 没有过期
                        if time.time() - Fh.get_update_ts(cache_file_path) < self.cache_file_ts:
                            return True
                        else:
                            logger.debug(f"== OUT TIME，不读缓存。{request.url}")
                            return False
                    else:
                        return True
            else:
                # logger.debug(f"缓存文件不存在。 {request.url}")
                return False

        if should_read_cache(request, spider):
            try:
                logger.info(f"===Read cache===  {cache_file_path.split(os.sep)[-1]}   {request.url}")
                return pickle.load(open(cache_file_path, "rb"))
            except Exception as e:
                logger.info(f"== Can't Read cache ===  Reason is {e}")
                Fh.remove_file(cache_file_path)
                traceback.print_exc()
        else:
            # 不读缓存
            logger.info("===Shouldn't Read Cache===   " + request.url)
            pass

    # 写文件缓存
    def process_response(self, request, response, spider) -> process_response_type:
        cache_file_path = self.cache_file_path_func(
            url=str(request.url), spider=str(spider.name),
            root_path_cache=self.settings.get("ROOT_PATH_CACHE"),
            request=request)

        # 是否应该重写缓存
        def should_write_cache(request, spider) -> bool:
            exists_file = Fh.is_file_exit(cache_file_path)
            exclude = 1 if self.cache_file_exclude and request.url.find(self.cache_file_exclude) >= 0 else 0
            if exists_file:
                if exclude:
                    if self.cache_file_exclude_ts:
                        if time.time() - Fh.get_update_ts(cache_file_path) > self.cache_file_exclude_ts:
                            logger.debug(
                                f"排除缓存文件过期。需要重写。{cache_file_path}{Fh.get_update_ts(cache_file_path)}  {request.url}")
                            return True
                        else:
                            logger.debug(
                                f"排除的URL没过期，不重写。过了{int(time.time() - Fh.get_update_ts(cache_file_path))} 秒？ {cache_file_path}")
                            return False
                    else:
                        logger.debug(f"排除URL没设置过期时间 都要重写。 {cache_file_path}")
                        return True
                else:
                    # logger.debug(f"不是排除的URL不重写缓存。 {cache_file_path}")
                    return False
            else:
                logger.debug(f"缓存文件不存在。写缓存。 {request.url}")
                return True

        if response.status < 300:
            Fh.mkdir(Fh.get_file_path_and_name(cache_file_path)[0])
            try:
                if should_write_cache(request, spider):
                    if hasattr(response, "certificate"):
                        del response.certificate
                    Fh.remove_file(cache_file_path)
                    pickle.dump(response, open(cache_file_path, "wb"))
                    logger.info(f"===Write cache===      {cache_file_path}   {request.url}")
                # else:
                #     logger.info(f"===Cache Exists===      {cache_file_path}   {request.url}")
            except Exception as e:
                logger.info(f"== Can't Write cache 2 file==   Reason is {e}")
                Fh.remove_file(cache_file_path)
                # traceback.print_exc()
        else:
            logger.info(f"===Status Code ERROR ===   Code is {response.status} " + response.url)
        return response


# 文件按月缓存中间件
class CacheFilePerMonthRequest(object):
    @staticmethod
    def get_cache_file(*args, **kwargs):
        spider = kwargs.get("spider")
        url = kwargs.get("url")
        request = kwargs.get("request", {})
        method = "get"
        body = ''
        if request:
            method = request.method
            body = request.body.decode("utf-8")
            # print("POST 缓存")
        else:
            # print("----No request")
            pass
        root_path_cache = kwargs.get("root_path_cache", "./")
        spider = spider if spider else Uh.get_domain(url).replace(".", "_")
        if method.lower() == "post":
            return root_path_cache + spider + os.sep + get_this_month().replace("-", '_') + os.sep + Fh.get_md5_name(url + "_" + body) + ".cache"
        else:
            return root_path_cache + spider + os.sep + get_this_month().replace("-", '_') + os.sep + Fh.get_md5_name(url) + ".cache"

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.cache_file_path_func = settings.get("FUN_CACHE_FILE_PATH", cls.get_cache_file)
        cls.cache_file_exclude = settings.get("CACHE_FILE_EXCLUDE")
        cls.cache_file_ts = settings.get("CACHE_FILE_TS", None)
        cls.cache_file_exclude_ts = settings.get("CACHE_FILE_EXCLUDE_TS", cls.cache_file_ts)
        cls.settings = settings
        return cls()

    def process_request(self, request, spider) -> process_request_type:
        cache_file_path = self.cache_file_path_func(
            url=str(request.url), spider=str(spider.name),
            root_path_cache=self.settings.get("ROOT_PATH_CACHE"),
            request=request)

        # 是否应该读缓存
        def should_read_cache(request, spider) -> bool:
            # 存在缓存文件
            exists_file = Fh.is_file_exit(cache_file_path)
            # 是排除URL
            exclude = 1 if self.cache_file_exclude and request.url.find(self.cache_file_exclude) >= 0 else 0
            if exists_file:
                if exclude:
                    if self.cache_file_exclude_ts >= 0:
                        if time.time() - Fh.get_update_ts(cache_file_path) < self.cache_file_exclude_ts:
                            return True
                        else:
                            logger.debug(
                                f"缓存文件过期。不读取。{cache_file_path}{Fh.get_update_ts(cache_file_path)}  {request.url}")
                            return False
                    # 排除URL无过期时间,就是排除URL都不读缓存
                    else:
                        logger.debug(f"排除的，没设置过期时间，全不读缓存。{request.url}")
                        return False
                else:
                    # 全部时间
                    if self.cache_file_ts:
                        # 全部URL 没有过期
                        if time.time() - Fh.get_update_ts(cache_file_path) < self.cache_file_ts:
                            return True
                        else:
                            logger.debug(f"== OUT TIME，不读缓存。{request.url}")
                            return False
                    else:
                        return True
            else:
                # logger.debug(f"缓存文件不存在。 {request.url}")
                return False

        if should_read_cache(request, spider):
            try:
                logger.info(f"===Read cache===  {cache_file_path.split(os.sep)[-1]}   {request.url}")
                return pickle.load(open(cache_file_path, "rb"))
            except Exception as e:
                logger.info(f"== Can't Read cache ===  Reason is {e}")
                Fh.remove_file(cache_file_path)
                traceback.print_exc()
        else:
            # 不读缓存
            # logger.info("===Shouldn't Read Cache===   " + request.url)
            pass

    # 写文件缓存
    def process_response(self, request, response, spider) -> process_response_type:
        cache_file_path = self.cache_file_path_func(
            url=str(request.url), spider=str(spider.name),
            root_path_cache=self.settings.get("ROOT_PATH_CACHE"),
            request=request)

        # 是否应该重写缓存
        def should_write_cache(request, spider) -> bool:
            exists_file = Fh.is_file_exit(cache_file_path)
            exclude = 1 if self.cache_file_exclude and request.url.find(self.cache_file_exclude) >= 0 else 0
            if exists_file:
                if exclude:
                    if self.cache_file_exclude_ts:
                        if time.time() - Fh.get_update_ts(cache_file_path) > self.cache_file_exclude_ts:
                            logger.debug(
                                f"排除缓存文件过期。需要重写。{cache_file_path}{Fh.get_update_ts(cache_file_path)}  {request.url}")
                            return True
                        else:
                            logger.debug(
                                f"排除的URL没过期，不重写。过了{int(time.time() - Fh.get_update_ts(cache_file_path))} 秒？ {cache_file_path}")
                            return False
                    else:
                        logger.debug(f"排除URL没设置过期时间 都要重写。 {cache_file_path}")
                        return True
                else:
                    # logger.debug(f"不是排除的URL不重写缓存。 {cache_file_path}")
                    return False
            else:
                # logger.debug(f"缓存文件不存在。写缓存。 {request.url}")
                return True

        if response.status < 300:
            Fh.mkdir(Fh.get_file_path_and_name(cache_file_path)[0])
            try:
                if should_write_cache(request, spider):
                    if hasattr(response, "certificate"):
                        del response.certificate
                    Fh.remove_file(cache_file_path)
                    pickle.dump(response, open(cache_file_path, "wb"))
                    logger.info(f"===Write cache===      {cache_file_path}   {request.url}")
                # else:
                #     logger.info(f"===Cache Exists===      {cache_file_path}   {request.url}")
            except Exception as e:
                logger.info(f"== Can't Write cache 2 file==   Reason is {e}")
                Fh.remove_file(cache_file_path)
                # traceback.print_exc()
        else:
            logger.info(f"===Status Code ERROR ===   Code is {response.status} " + response.url)
        return response


# Redis Hash缓存中间件
class CacheRedisHashRequest(object):

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.settings = settings
        return cls()

    def __init__(self):
        import XX.DB.RedisHelper as RH
        self.conn_redis7 = RH.RedisHelper.get_redis_connect(self.settings.get("REDIS_HOST"),
                                                            port=self.settings.get("REDIS_PORT"),
                                                            password=self.settings.get("REDIS_PWD"), db=7)

    # 读redis缓存
    def process_request(self, request, spider) -> process_request_type:
        if self.conn_redis7.exists(request.url):
            print("==Read cache 2 redis==")
            url = self.conn_redis7.hget(request.url, "url")
            html = self.conn_redis7.hget(request.url, "html")
            status_code = self.conn_redis7.hget(request.url, "status_code")
            encoding = self.conn_redis7.hget(request.url, "encoding")
            return TextResponse(url=url, body=html, status=status_code, encoding=encoding)

    # 写redis缓存
    def process_response(self, request, response, spider) -> process_response_type:
        if response.status == 200:
            try:
                if not self.conn_redis7.exists(response.url):
                    self.conn_redis7.hset(response.url, "url", response.url)
                    self.conn_redis7.hset(response.url, "html", response.text)
                    self.conn_redis7.hset(response.url, "status_code", response.status)
                    self.conn_redis7.hset(response.url, "encoding", response.encoding)
                    self.conn_redis7.hset(response.url, "spider", spider.name)
                    self.conn_redis7.hset(response.url, "project_name", self.settings.get("PROJECT_NAME", "crawl"))
                    print("==Write cache 2 redis==")
            except:
                print("==Can't Write cache 2 redis==")
                traceback.print_exc()
        return response


# Redis缓存中间件
class CacheRedisRequest(object):
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.settings = settings
        return cls()

    def __init__(self):
        import XX.DB.RedisHelper as RH
        self.conn_redis14 = RH.RedisHelper.get_redis_instance()

    # 读redis缓存
    def process_request(self, request, spider) -> process_request_type:
        try:
            content = self.conn_redis14.get(request.url)
            if content:
                try:
                    return pickle.loads(content)
                except Exception as e:
                    self.conn_redis14.delete(request.url)
                    logger.info(e)
        except:
            print("==Can't Read cache from redis==")
            traceback.print_exc()

    # 写redis缓存
    def process_response(self, request, response, spider) -> process_response_type:
        if response.status == 200:
            try:
                if not self.conn_redis14.exists(response.url):
                    pickinfo = pickle.dumps(response)
                    self.conn_redis14.set(response.url, pickinfo)
            except:
                print("==Can't Write cache 2 redis==")
                traceback.print_exc()
        return response


# HBase缓存下载中间件
class CacheHappyBaseRequest(object):
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.settings = settings
        return cls()

    def __init__(self):
        pool = happybase.ConnectionPool(size=3, host=self.settings.get("HBASE_HOST", "localhost"),
                                        port=self.settings.get("HBASE_PORT", 9090), protocol='binary',
                                        transport='buffered')
        self.connection = pool._acquire_connection()
        self.table_name = "crawl_" + self.settings.get("PROJECT_NAME", "crawl")
        self.table = self.connection.table(self.table_name)

        # 判断是否有表，没有则生成
        tables = self.connection.tables()
        if self.table_name.encode("utf-8") not in tables:
            self.connection.create_table(self.table_name, {'source': {}, 'data': {}})

    # 读取缓存
    def getCacheResult(self, request, spider, row_key=None):
        if not row_key:
            row_key = spider.name + "_" + Enc.Encrypt.md5(request.url)
        try:
            row = self.table.row(row_key, include_timestamp=True)
            if row:
                # 默认HTML是永久存储的
                if (request.url.endswith("html") or request.url.endswith("htm")) and not self.settings.get(
                        "HBASE_HTML_EXPIRE", 0):
                    return row
                expire = int(self.settings.get("HBASE_EXPIRE_TS", 0))
                if expire > 0:
                    if time.time() - row.get(b'source:url')[1] // 1000 <= expire:
                        return row
                    else:
                        logger.info(str(row.get(b'source:url')[1]) + "\tis out time\t" + str(expire))
                else:
                    return row
        except:
            self.__init__()
            logger.info("Reconnect 2 HBase" + "===" * 33)
        return None

    # 读缓存，生成response
    def process_request(self, request, spider) -> process_request_type:
        row_key = spider.name + "_" + Enc.Encrypt.md5(request.url)
        result = self.getCacheResult(request, spider, row_key=row_key)
        if result:
            logger.info("R>>>>\trow_key\t" + str(row_key) + "\t" + request.url)
            encoding = result.get(b"source:encoding", [b"utf-8"])[0].decode("utf-8")
            return TextResponse(url=result.get(b"source:url")[0].decode("utf-8"),
                                body=result.get(b"source:html")[0].decode("utf-8"),
                                status=result.get(b"source:status_code")[0].decode("utf-8"), encoding=encoding)
        else:
            pass

    # 写缓存到HBASE
    def process_response(self, request, response, spider) -> process_response_type:
        if not self.getCacheResult(request, spider):
            if response.status == 200:
                data = {
                    "source:url": str(response.url),
                    "source:status_code": str(response.status),
                    "source:html": str(response.text),
                    "source:type": "html",
                    "source:size": str(len(response.text)),
                    "source:encoding": response.encoding
                }
                row_key = spider.name + "_" + Enc.Encrypt.md5(request.url)
                try:
                    self.table.put(row_key, data)
                except:
                    self.__init__()
                    logger.info("Reconnect 2 HBase" + "===" * 33)
                logger.info("W<<<<\trow_key\t" + str(row_key) + "\t" + response.url)
            else:
                logger.info("Not 200 ---\t" + str(response.status) + "\t" + response.url)
        return response

    def close_spider(self):
        pass


# HBase缓存下载中间件
class CacheHBaseRK(object):
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        cls.settings = settings
        return cls()

    def __init__(self):
        pool = happybase.ConnectionPool(size=3, host=self.settings.get("HBASE_HOST", "localhost"),
                                        port=self.settings.get("HBASE_PORT", 9090), protocol='binary',
                                        transport='buffered')
        self.connection = pool._acquire_connection()
        self.table_name = "crawl_" + self.settings.get("PROJECT_NAME", "crawl")
        self.table = self.connection.table(self.table_name)

        # 判断是否有表，没有则生成
        tables = self.connection.tables()
        if self.table_name.encode("utf-8") not in tables:
            self.connection.create_table(self.table_name, {'source': {}, 'data': {}})

    # 读取缓存
    def getCacheResult(self, request, spider, row_key=None):
        if not row_key:
            row_key = self.settings.get("HBASE_ROW_KEY_FUN")(request=request)
            print("RRRRRRRRRRKKKKKKKK", row_key)
        try:
            row = self.table.row(row_key, include_timestamp=True)
            if row:
                # 默认HTML是永久存储的
                if (request.url.endswith("html") or request.url.endswith("htm")) and not self.settings.get(
                        "HBASE_HTML_EXPIRE", 0):
                    return row
                expire = int(self.settings.get("HBASE_EXPIRE_TS", 0))
                if expire > 0:
                    if time.time() - row.get(b'source:url')[1] // 1000 <= expire:
                        return row
                    else:
                        logger.info(str(row.get(b'source:url')[1]) + "\tis out time")
                else:
                    return row
        except:
            self.__init__()
            logger.info("Reconnect 2 HBase" + "===" * 33)
        return None

    # 读缓存，生成response
    def process_request(self, request, spider) -> process_request_type:
        row_key = self.settings.get("HBASE_ROW_KEY_FUN")(request=request)
        result = self.getCacheResult(request, spider, row_key=row_key)
        if result:
            logger.info("R>>>>\trow_key\t" + str(row_key) + "\t" + request.url)
            encoding = result.get(b"source:encoding", [b"utf-8"])[0].decode("utf-8")
            return TextResponse(url=result.get(b"source:url")[0].decode("utf-8"),
                                body=result.get(b"source:html")[0].decode("utf-8"),
                                status=result.get(b"source:status_code")[0].decode("utf-8"), encoding=encoding)

    # 写缓存到HBASE
    def process_response(self, request, response, spider) -> process_response_type:
        if not self.getCacheResult(request, spider):
            if response.status == 200:
                data = {
                    "source:url": str(response.url),
                    "source:status_code": str(response.status),
                    "source:html": str(response.text),
                    "source:type": "html",
                    "source:size": str(len(response.text)),
                    "source:encoding": response.encoding
                }
                row_key = self.settings.get("HBASE_ROW_KEY_FUN")(request=request)
                try:
                    self.table.put(row_key, data)
                except:
                    self.__init__()
                    logger.info("Reconnect 2 HBase" + "===" * 33)
                logger.info("W<<<<\trow_key\t" + str(row_key) + "\t" + response.url)
            else:
                logger.info("Not 200 --- " + "\t" + response.url)
        return response
