#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2018/9/22 0:57
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Tax.py
# @Software : PyCharm
from mongoengine import *


class Tax(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


if __name__ == '__main__':
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
    pass
