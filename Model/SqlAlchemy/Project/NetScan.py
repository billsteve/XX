# coding: utf-8
from XX.Model.SqlAlchemy.BaseModel import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, TEXT, text
from sqlalchemy.dialects.mysql.types import TINYINT


class Beian(Base, BaseModel):
    __tablename__ = 'beian'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer)
    name = Column(String(255))
    url = Column(String(255))
    license = Column(String(255))
    icp_license = Column(String(255))
    entity = Column(String(255))
    web_type = Column(String(255))
    owner = Column(String(255))
    owner_city = Column(String(60))
    owner_id = Column(Integer)
    no = Column(String(255))
    org = Column(String(255))
    reg_time = Column(DateTime)
    art_licence = Column(String(55))
    is_del = Column(TINYINT(1))
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.art_licence = kw.get("art_licence", None)
        self.create_ts = kw.get("create_ts", None)
        self.entity = kw.get("entity", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.license = kw.get("license", None)
        self.icp_license = kw.get("icp_license", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.no = kw.get("no", None)
        self.org = kw.get("org", None)
        self.owner = kw.get("owner", None)
        self.owner_city = kw.get("owner_city", None)
        self.owner_id = kw.get("owner_id", None)
        self.reg_time = kw.get("reg_time", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)
        self.url_id = kw.get("url_id", None)
        self.web_type = kw.get("web_type", None)


class Ip(Base, BaseModel):
    __tablename__ = 'ip'

    id = Column(Integer, primary_key=True)
    ip = Column(String(15), index=True)
    addr = Column(String(255))
    is_del = Column(TINYINT(1))
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.addr = kw.get("addr", None)
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.ip = kw.get("ip", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.update_ts = kw.get("update_ts", None)


class IpSegment(Base, BaseModel):
    __tablename__ = 'ip_segment'

    id = Column(Integer, primary_key=True)
    ip_start = Column(String(255))
    ip_stop = Column(String(255))
    is_del = Column(TINYINT(1))
    create_ts = Column(Integer)
    update_ts = Column(Integer)


class Org(Base, BaseModel):
    __tablename__ = 'org'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.update_ts = kw.get("update_ts", None)


class QueryType(Base, BaseModel):
    __tablename__ = 'query_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_del = Column(TINYINT(1))
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.update_ts = kw.get("update_ts", None)


class Tag(Base, BaseModel):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    is_del = Column(TINYINT(1))
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.update_ts = kw.get("update_ts", None)


class Url(Base, BaseModel):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    domain = Column(String(100))
    url = Column(String(255))
    name = Column(String(255))
    level = Column(Integer)
    p_id = Column(Integer)
    query_types = Column(String(255))
    is_del = Column(TINYINT(1))
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.domain = kw.get("domain", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.level = kw.get("level", None)
        self.metadata = kw.get("metadata", None)
        self.name = kw.get("name", None)
        self.p_id = kw.get("p_id", None)
        self.query_types = kw.get("query_types", None)
        self.update_ts = kw.get("update_ts", None)
        self.url = kw.get("url", None)

    @staticmethod
    def geIdByDomainAndPid(domain, pid, sessoin):
        return sessoin.query(Url.id).filter(Url.domain == domain, Url.p_id == pid).order_by("id").all()


class UrlIp(Base, BaseModel):
    __tablename__ = 'url_ip'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer)
    ip_id = Column(Integer)
    ts = Column(DateTime)
    is_del = Column(TINYINT(1))
    update_ts = Column(Integer)
    create_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.ip_id = kw.get("ip_id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.ts = kw.get("ts", None)
        self.update_ts = kw.get("update_ts", None)
        self.url_id = kw.get("url_id", None)

    @staticmethod
    def getIdByUrlIdIpId(url_id, ip_id, session):
        return session.query(UrlIp.id).filter(UrlIp.url_id == url_id, UrlIp.ip_id == ip_id).all()


class UrlTag(Base, BaseModel):
    __tablename__ = 'url_tag'
    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False)
    tag_id = Column(Integer, nullable=False)
    is_del = Column(TINYINT(1))
    create_ts = Column(Integer)
    update_ts = Column(Integer)

    def __init__(self, *arg, **kw):
        self.create_ts = kw.get("create_ts", None)
        self.id = kw.get("id", None)
        self.is_del = kw.get("is_del", None)
        self.metadata = kw.get("metadata", None)
        self.tag_id = kw.get("tag_id", None)
        self.update_ts = kw.get("update_ts", None)
        self.url_id = kw.get("url_id", None)


class OwnerInfo(Base, BaseModel):
    __tablename__ = 'owner_info'

    id = Column(Integer, primary_key=True)
    ADDR = Column(String(255))
    ANADDR = Column(String(255))
    ENTTYPE = Column(String(255))
    ENTTYPENAME = Column(String(255))
    HIGHLIGHTTITLE = Column(String(255))
    INVOPT = Column(String(255))
    JYFW = Column(TEXT)
    NBXH = Column(String(255))
    PRIPID = Column(String(255))
    QYBM = Column(String(255))
    QYWZ = Column(String(255))
    REGNO = Column(String(255))
    REGSTATECODE = Column(String(255))
    REGSTATE_CN = Column(String(255))
    REGUNIT = Column(String(255))
    REGUNITNAME = Column(String(255))
    SQ = Column(String(255))
    S_EXT_NODENUM = Column(String(255))
    TEL = Column(String(255))
    UBINDTYPE = Column(String(255))
    UBINDTYPENAME = Column(String(255))
    UNITCODE = Column(String(255))
    UNITNAME = Column(String(255))
    XZQHBM = Column(String(255))
    is_del = Column(Integer)
    update_ts = Column(Integer)
    create_ts = Column(Integer)

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
        self.update_ts = kw.get("update_ts", None)


if __name__ == '__main__':
    # createInitFunction(Beian)
    # createInitFunction(Ip)
    # createInitFunction(Org)
    # createInitFunction(Url)
    # createInitFunction(UrlIp)
    createInitFunction(QueryType)
