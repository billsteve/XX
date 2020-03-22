#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/14 14:18
# @Author   : Peter
# @Site       : Model基类
# @File        : BaseModel.py
# @Software: PyCharm
from sqlalchemy import func, or_


class BaseModel:
    # TODO: pk = "id"

    # 更新model
    @staticmethod
    def merge_model(model, session, commit=True):
        session.merge(model)
        if commit:
            session.commit()

    # 添加model
    @staticmethod
    def add_model(model, session, commit=True):
        session.add(model)
        if commit:
            session.commit()

    # query
    @staticmethod
    def query(sql, session, *args, **kwargs):
        return session.execute(sql)

    # 通过id查询
    @classmethod
    def get(cls, _id, session):
        return session.query(cls).get(_id)

    # 查询所有
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    # 查询所有
    @classmethod
    def get_all_by_condition(cls, cond, session, relation="and", **kw):
        condition = list()
        for k, v in dict(cond).items():
            condition += [getattr(cls, k) == v]
        if relation == "and":
            return session.query(cls).filter(*condition).order_by("id").all()
        elif relation == "or":
            return session.query(cls).filter(or_(*condition)).order_by("id").all()
        else:
            return session.query(cls).all()

    # 查询所有id
    @classmethod
    def get_all_ids(cls, session):
        return session.query(cls.id).all()

    # 根据名字查找
    @classmethod
    def get_by_name(cls, name, session):
        return cls.getByKV("name", name, session)
        # return session.query(cls).filter(cls.name == name).all()

    # 从偏移量查找
    @classmethod
    def get_by_from_id(cls, from_id, session, **kw):
        if kw.get("where"):
            condition = list()
            for k, v in dict(kw.get("where")).items():
                condition += [getattr(cls, k) == v]
            if condition:
                return session.query(cls).filter(cls.id > from_id).filter(*condition).limit(kw.get("limit", 10)).all()
        return session.query(cls).filter(cls.id > from_id).limit(kw.get("limit", 10)).all()

    # 从偏移量查找，对ID取模
    # SELECT * FROM table_name WHERE id >{from_id} AND id % {mod} = {left}
    @classmethod
    def get_by_from_id_and_mod(cls, from_id, mod, left, session, **kw):
        if kw.get("where"):
            condition = list()
            for k, v in dict(kw.get("where")).items():
                condition += [getattr(cls, k) == v]
            if condition:
                return session.query(cls).filter(cls.id > from_id, cls.id % mod == left).filter(*condition).limit(kw.get("limit", 10)).all()
        return session.query(cls).filter(cls.id > from_id, cls.id % mod == left).limit(kw.get("limit", 10)).all()

    # 从偏移量查找部分字段，对ID取
    @classmethod
    def get_colums_by_from_id_and_mod(cls, Colums, from_id, mod, left, session, **kw):
        cls_colum = []
        for Colum in Colums:
            cls_colum.append(getattr(cls, Colum))
        return session.query(tuple(cls_colum)).filter(cls.id > from_id, cls.id % mod == left).limit(kw.get("limit", 10)).all()

    # 更新id
    @classmethod
    def update_id(cls, _id, to_id, session):
        res = session.execute("UPDATE " + str(cls.__tablename__) + " set id = " + str(to_id) + " WHERE id = " + str(_id) + " LIMIT 1")
        session.commit()
        return res

    # 更新字段
    @classmethod
    def update_kv(cls, _id, k, v, session):
        res = session.execute("UPDATE " + str(cls.__tablename__) + " set " + str(k) + " = '" + str(v) + "' WHERE id = '" + str(_id) + "' LIMIT 1")
        session.commit()
        return res

    # 更新字段
    @classmethod
    def update_kvby_condition(cls, cond_k, cond_v, value_k, value_v, session, limit=1):
        res = session.execute("UPDATE " + str(cls.__tablename__) + " set " + str(value_k) + " = '" + str(value_v) + "' WHERE " + cond_k + " = " + str(cond_v) + " LIMIT " + str(limit))
        session.commit()
        return res

    # 根据字段值获取ID
    @classmethod
    def get_id_by_kv(cls, k, v, session, **kw):
        return session.query(cls.id).filter(getattr(cls, k) == v).order_by("id").limit(kw.get("limit", 1)).all()

    # 根据多个字段值获取ID
    @classmethod
    def get_id_by_condition(cls, d, session, **kw):
        condition = list()
        for k, v in dict(d).items():
            condition += [getattr(cls, k) == v]
        return session.query(cls.id).filter(*condition).order_by("id").limit(kw.get("limit", 1)).all()

    # 根据字段值获取信息
    @classmethod
    def get_by_kv(cls, k, v, session, **kw):
        return session.query(cls).filter(getattr(cls, k) == v).order_by("id").limit(kw.get("limit", 10)).all()

    # 根据字段值获取信息
    @classmethod
    def get_by_condition(cls, d, session, relation="and", **kw):
        condition = list()
        for k, v in dict(d).items():
            condition += [getattr(cls, k) == v]
        if relation == "and":
            return session.query(cls).filter(*condition).order_by("id").limit(kw.get("limit", 10)).all()
        elif relation == "or":
            return session.query(cls).filter(or_(*condition)).order_by("id").limit(kw.get("limit", 10)).all()
        else:
            return None

    # 查询总条数
    @classmethod
    def get_count(cls, session):
        return session.query(func.count(cls.id)).scalar()

    # 获取TopN
    @classmethod
    def get_top_n(cls, order, session, **kwargs):
        return session.query(cls).order_by(order).limit(kwargs.get("limit", 10)).all()

    # TODO:Test
    @classmethod
    def get_k_region(cls, k, start_v, end_v, session, **kwargs):
        return session.query(cls).filter(getattr(cls, k) >= start_v, getattr(cls, k) < end_v).order_by(kwargs.get("order", "id")).limit(kwargs.get("limit", 10)).all()

    # ++
    @classmethod
    def increase_kv_by_id(cls, id_, k, session, **kwargs):
        res = session.query(cls).filter(cls.id == id_).update({
            getattr(cls, k): getattr(cls, k) + kwargs.get("incr", 1)
        })
        session.commit()
        return res

    # concat
    @classmethod
    def concat_kv_by_id(cls, id_, k, v, session, **kwargs):
        res = session.query(cls).filter(cls.id == id_).update({
            getattr(cls, k): func.concat(getattr(cls, k), v)
        })
        session.commit()
        return res

    # concat  UPDATE tb k_value = concat(k1,k2)
    @classmethod
    def concat_kk_2_k_by_id(cls, id_, k1, k2, k_value, session, **kwargs):
        res = session.query(cls).filter(cls.id == id_).update({
            getattr(cls, k_value): func.concat(getattr(cls, k1), func.concat(getattr(cls, k2)))
        })
        session.commit()
        return res

    # concat UPDATE tb k_value = concat(k,v)
    @classmethod
    def concat_kv_2_k_by_id(cls, id_, k, v, k_value, session, **kwargs):
        res = session.query(cls).filter(cls.id == id_).update({
            getattr(cls, k_value): func.concat(getattr(cls, k), v)
        })
        session.commit()
        return res


def create_init_function(cls):
    import types

    print("""def __init__(self, *arg, **kw):""")
    for k in dir(cls):
        if not (str(k).startswith("_") or isinstance(getattr(cls, k), types.FunctionType)):
            print("""    self.{attr} = kw.get("{attr}")""".format(attr=k))
