#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/3/21 17:25
# @File           : SaaS
# @Des           : 
# @Email        : billsteve@126.com
from BaseModel.BaseModel import *
from sqlalchemy import Column, String, TIMESTAMP, Text, text, DateTime
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BaiduAdvertisement(Base, BaseModel):
    __tablename__ = 'baidu_advertisement'

    id = Column(INTEGER(11), primary_key=True)
    url = Column(String(255))
    real_url = Column(String(255))
    snapshot_url = Column(String(255))
    title = Column(String(255))
    is_del = Column(INTEGER(11), server_default=text("'0'"))
    create_ts = Column(INTEGER(11))
    update_ts = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.real_url = kw.get("real_url", None)
        self.snapshot_url = kw.get("snapshot_url", None)
        self.title = kw.get("title", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)


class BaiduSearchResult(Base, BaseModel):
    __tablename__ = 'wp_saas_baidu_search_result'

    id = Column(INTEGER(11), primary_key=True)
    platform = Column(String(255))
    keyword = Column(String(255))
    crawl_time = Column(INTEGER(11))
    url = Column(String(255))
    real_url = Column(String(255), unique=True)
    source_url = Column(String(255))
    title = Column(String(255))
    spider = Column(String(60))
    skip_url = Column(Text)
    snapshot_url = Column(Text)
    show_url = Column(Text)
    is_ad = Column(TINYINT(1))
    content = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.content = kw.get("content", None)
        self.crawl_time = kw.get("crawl_time", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_ad = kw.get("is_ad", None)
        self.is_del = kw.get("is_del", None)
        self.keyword = kw.get("keyword", None)
        self.metadata = kw.get("metadata", None)
        self.platform = kw.get("platform", None)
        self.real_url = kw.get("real_url", None)
        self.show_url = kw.get("show_url", None)
        self.skip_url = kw.get("skip_url", None)
        self.snapshot_url = kw.get("snapshot_url", None)
        self.source_url = kw.get("source_url", None)
        self.spider = kw.get("spider", None)
        self.title = kw.get("title", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)


class Company(Base, BaseModel):
    __tablename__ = 'wp_saas_company'
    id = Column(INTEGER(11), primary_key=True)
    ADDR = Column(String(255, 'utf8mb4_unicode_ci'))
    ANADDR = Column(String(255, 'utf8mb4_unicode_ci'))
    ENTTYPE = Column(String(255, 'utf8mb4_unicode_ci'))
    ENTTYPENAME = Column(String(255, 'utf8mb4_unicode_ci'))
    HIGHLIGHTTITLE = Column(String(255, 'utf8mb4_unicode_ci'))
    INVOPT = Column(String(255, 'utf8mb4_unicode_ci'))
    JYFW = Column(Text(collation='utf8mb4_unicode_ci'))
    NBXH = Column(String(80, 'utf8mb4_unicode_ci'), index=True)
    PRIPID = Column(String(255, 'utf8mb4_unicode_ci'))
    QYBM = Column(String(255, 'utf8mb4_unicode_ci'))
    QYWZ = Column(String(255, 'utf8mb4_unicode_ci'))
    REGNO = Column(String(80, 'utf8mb4_unicode_ci'), index=True)
    REGSTATECODE = Column(String(255, 'utf8mb4_unicode_ci'))
    REGSTATE_CN = Column(String(255, 'utf8mb4_unicode_ci'))
    REGUNIT = Column(String(255, 'utf8mb4_unicode_ci'))
    REGUNITNAME = Column(String(255, 'utf8mb4_unicode_ci'))
    SQ = Column(String(255, 'utf8mb4_unicode_ci'))
    S_EXT_NODENUM = Column(String(255, 'utf8mb4_unicode_ci'))
    TEL = Column(String(255, 'utf8mb4_unicode_ci'))
    UBINDTYPE = Column(String(255, 'utf8mb4_unicode_ci'))
    UBINDTYPENAME = Column(String(255, 'utf8mb4_unicode_ci'))
    UNITCODE = Column(String(255, 'utf8mb4_unicode_ci'))
    UNITNAME = Column(String(255, 'utf8mb4_unicode_ci'))
    XZQHBM = Column(String(255, 'utf8mb4_unicode_ci'))
    reg_time = Column(DateTime)
    is_del = Column(INTEGER(11))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.ADDR = kw.get("ADDR", None)
        self.ANADDR = kw.get("ANADDR", None)
        self.ENTTYPE = kw.get("ENTTYPE", None)
        self.ENTTYPENAME = kw.get("ENTTYPENAME", None)
        self.HIGHLIGHTTITLE = kw.get("HIGHLIGHTTITLE", None)
        self.INVOPT = kw.get("INVOPT", None)
        self.JYFW = kw.get("JYFW", None)
        self.NBXH = kw.get("NBXH", None)
        self.PRIPID = kw.get("PRIPID", None)
        self.QYBM = kw.get("QYBM", None)
        self.QYWZ = kw.get("QYWZ", None)
        self.REGNO = kw.get("REGNO", None)
        self.REGSTATECODE = kw.get("REGSTATECODE", None)
        self.REGSTATE_CN = kw.get("REGSTATE_CN", None)
        self.REGUNIT = kw.get("REGUNIT", None)
        self.REGUNITNAME = kw.get("REGUNITNAME", None)
        self.SQ = kw.get("SQ", None)
        self.S_EXT_NODENUM = kw.get("S_EXT_NODENUM", None)
        self.TEL = kw.get("TEL", None)
        self.UBINDTYPE = kw.get("UBINDTYPE", None)
        self.UBINDTYPENAME = kw.get("UBINDTYPENAME", None)
        self.UNITCODE = kw.get("UNITCODE", None)
        self.UNITNAME = kw.get("UNITNAME", None)
        self.XZQHBM = kw.get("XZQHBM", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.reg_time = kw.get("reg_time", None)
        self.update_ts = kw.get("update_ts", None)


class ItjuziCompany(Base, BaseModel):
    __tablename__ = 'itjuzi_company'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    des = Column(String(255))
    logo = Column(String(255))
    web_id = Column(INTEGER(11))
    is_del = Column(TINYINT(255))
    create_ts = Column(INTEGER(11))
    update_ts = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.des = kw.get("des", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.logo = kw.get("logo", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.update_ts = kw.get("update_ts", None)
        self.web_id = kw.get("web_id", None)


class ItjuziNew(Base, BaseModel):
    __tablename__ = 'itjuzi_news'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255))
    url = Column(String(255))
    logo = Column(String(255))
    web_id = Column(INTEGER(11))
    is_del = Column(TINYINT(255))
    create_ts = Column(INTEGER(11))
    update_ts = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.logo = kw.get("logo", None)
        self.metadata = kw.get("metadata", None)
        self.title = kw.get("title", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)
        self.web_id = kw.get("web_id", None)


class Url(Base, BaseModel):
    __tablename__ = 'wp_saas_url'

    id = Column(INTEGER(11), primary_key=True)
    domain = Column(String(255), index=True)
    url = Column(String(255), index=True)
    name = Column(String(255), index=True)
    level = Column(INTEGER(11))
    p_id = Column(INTEGER(11))
    content = Column(Text)
    title = Column(Text)
    description = Column(Text)
    keywords = Column(Text)
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.content = kw.get("content", None)
        self.create_ts = kw.get("create_ts", None)
        self.description = kw.get("description", None)
        self.domain = kw.get("domain", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.keywords = kw.get("keywords", None)
        self.level = kw.get("level", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.p_id = kw.get("p_id", None)
        self.title = kw.get("title", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)


class Keyword(Base, BaseModel):
    __tablename__ = 'wp_saas_keywords'

    id = Column(INTEGER(11), primary_key=True)
    words = Column(String(192), nullable=False, unique=True)
    source = Column(INTEGER(1))
    flag = Column(INTEGER(1))
    update_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    create_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.flag = kw.get("flag", None)
        self.id = kw.get("id", None)
        self.metadata = kw.get("metadata", None)
        self.source = kw.get("source", None)
        self.update_ts = kw.get("update_ts", None)
        self.words = kw.get("words", None)


class NewsSearch(Base, BaseModel):
    __tablename__ = 'news_search'

    id = Column(INTEGER(11), primary_key=True)
    source_url = Column(String(255))
    url = Column(String(255))
    title = Column(String(255))
    top_image = Column(String(255))
    meta_img = Column(String(255))
    movies = Column(LONGTEXT)
    text = Column(String(255))
    keywords = Column(LONGTEXT)
    meta_keywords = Column(LONGTEXT)
    tags = Column(LONGTEXT)
    authors = Column(LONGTEXT)
    publish_date = Column(String(255))
    summary = Column(String(255))
    is_parsed = Column(String(255))
    download_state = Column(INTEGER(11))
    download_exception_msg = Column(String(255))
    meta_description = Column(String(255))
    meta_lang = Column(String(255))
    meta_favicon = Column(String(255))
    meta_data = Column(LONGTEXT)
    canonical_link = Column(String(255))
    additional_data = Column(LONGTEXT)
    link_hash = Column(String(255))
    is_del = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))
    update_ts = Column(TIMESTAMP)

    def __init__(self, *arg, **kw):
        self.additional_data = kw.get("additional_data", None)
        self.authors = kw.get("authors", None)
        self.canonical_link = kw.get("canonical_link", None)
        self.create_ts = kw.get("create_ts", None)
        self.download_exception_msg = kw.get("download_exception_msg", None)
        self.download_state = kw.get("download_state", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.is_parsed = kw.get("is_parsed", None)
        self.keywords = kw.get("keywords", None)
        self.link_hash = kw.get("link_hash", None)
        self.meta_data = kw.get("meta_data", None)
        self.meta_description = kw.get("meta_description", None)
        self.meta_favicon = kw.get("meta_favicon", None)
        self.meta_img = kw.get("meta_img", None)
        self.meta_keywords = kw.get("meta_keywords", None)
        self.meta_lang = kw.get("meta_lang", None)
        self.metadata = kw.get("metadata", None)
        self.movies = kw.get("movies", None)
        self.publish_date = kw.get("publish_date", None)
        self.source_url = kw.get("source_url", None)
        self.summary = kw.get("summary", None)
        self.tags = kw.get("tags", None)
        self.text = kw.get("text", None)
        self.title = kw.get("title", None)
        self.top_image = kw.get("top_image", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)


class Product(Base, BaseModel):
    __tablename__ = 'wp_saas_product'

    id = Column(INTEGER(11), primary_key=True)
    url_id = Column(INTEGER(11), index=True)
    name = Column(String(255), index=True)
    p_id = Column(INTEGER(11))
    logo = Column(String(255))
    intro = Column(LONGTEXT)
    company_id = Column(INTEGER(11))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.company_id = kw.get("company_id", None)
        self.id = kw.get("id", None)
        self.intro = kw.get("intro", None)
        self.is_del = kw.get("is_del", None)
        self.logo = kw.get("logo", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.p_id = kw.get("p_id", None)
        self.update_ts = kw.get("update_ts", None)
        self.url_id = kw.get("url_id", None)


class ProductSearch(Base, BaseModel):
    __tablename__ = 'product_search'

    id = Column(INTEGER(11), primary_key=True)
    source_url = Column(String(255))
    url = Column(String(255))
    title = Column(String(255))
    top_image = Column(String(255))
    meta_img = Column(String(255))
    movies = Column(LONGTEXT)
    text = Column(String(255))
    keywords = Column(LONGTEXT)
    meta_keywords = Column(LONGTEXT)
    tags = Column(LONGTEXT)
    authors = Column(LONGTEXT)
    publish_date = Column(String(255))
    summary = Column(String(255))
    is_parsed = Column(String(255))
    download_state = Column(INTEGER(11))
    download_exception_msg = Column(String(255))
    meta_description = Column(String(255))
    meta_lang = Column(String(255))
    meta_favicon = Column(String(255))
    meta_data = Column(LONGTEXT)
    canonical_link = Column(String(255))
    additional_data = Column(LONGTEXT)
    link_hash = Column(String(255))
    is_del = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))
    update_ts = Column(TIMESTAMP)

    def __init__(self, *arg, **kw):
        self.additional_data = kw.get("additional_data", None)
        self.authors = kw.get("authors", None)
        self.canonical_link = kw.get("canonical_link", None)
        self.create_ts = kw.get("create_ts", None)
        self.download_exception_msg = kw.get("download_exception_msg", None)
        self.download_state = kw.get("download_state", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.is_parsed = kw.get("is_parsed", None)
        self.keywords = kw.get("keywords", None)
        self.link_hash = kw.get("link_hash", None)
        self.meta_data = kw.get("meta_data", None)
        self.meta_description = kw.get("meta_description", None)
        self.meta_favicon = kw.get("meta_favicon", None)
        self.meta_img = kw.get("meta_img", None)
        self.meta_keywords = kw.get("meta_keywords", None)
        self.meta_lang = kw.get("meta_lang", None)
        self.metadata = kw.get("metadata", None)
        self.movies = kw.get("movies", None)
        self.publish_date = kw.get("publish_date", None)
        self.source_url = kw.get("source_url", None)
        self.summary = kw.get("summary", None)
        self.tags = kw.get("tags", None)
        self.text = kw.get("text", None)
        self.title = kw.get("title", None)
        self.top_image = kw.get("top_image", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)


class ProductType(Base, BaseModel):
    __tablename__ = 'wp_saas_product_type'

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(INTEGER(11))
    type_id = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.product_id = kw.get("product_id", None)
        self.type_id = kw.get("type_id", None)
        self.update_ts = kw.get("update_ts", None)


class Types(Base, BaseModel):
    __tablename__ = 'wp_saas_types'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    p_id = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.p_id = kw.get("p_id", None)
        self.update_ts = kw.get("update_ts", None)


class ProductFromNews(Base, BaseModel):
    __tablename__ = 'wp_saas_product_from_news'

    id = Column(INTEGER(11), primary_key=True)
    news_id = Column(INTEGER(11), index=True)
    title = Column(String(255), index=True)
    products = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(INTEGER(11))
    create_ts = Column(INTEGER(11))

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.news_id = kw.get("news_id", None)
        self.products = kw.get("products", None)
        self.title = kw.get("title", None)
        self.update_ts = kw.get("update_ts", None)


if __name__ == '__main__':
    createInitFunction(BaiduAdvertisement)
