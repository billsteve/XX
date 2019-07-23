from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from ..BaseModel import BaseModel

Base = declarative_base()
metadata = Base.metadata


class KeyWordModel(Base, BaseModel):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True)
    key = Column(String(255))

    def __init__(self, *arg, **kw):
        self.key = kw.get("key", None)

    @staticmethod
    def saveKeyWord(data, session):
        key = data.get("key")
        if key:
            exists = KeyWordModel.getByKV("key", key, session)
        else:
            return
        if not exists:
            keyword = KeyWordModel(**data)
            KeyWordModel.addModel(keyword, session)
            return keyword.key
        return exists[0].key
