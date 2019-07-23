#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/1/3 22:04
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : setup.py
# @Des         : 
# @Software : PyCharm
import time
from setuptools import setup, find_packages

setup(
    name="XX",
    version=time.strftime('%Y%m%d.%H%M', time.localtime(int(time.time()))),
    description=(
        "x's tools"
    ),
    long_description="""**Just Test** 
    
    Not safe,not stable and will boom boom boom.

    Just like these:
        -  https://music.163.com/song?id=3949444&userid=319278554  
        -  https://music.163.com/song?id=474581010&userid=319278554  
        -  https://open.spotify.com/album/47wyCwrChF50ZTFNOuWx99  
        -  https://open.spotify.com/track/3oDFtOhcN08qeDPAK6MEQG  
    """,
    author='billsteve',
    author_email='billsteve@126.com',
    maintainer='billsteve',
    maintainer_email='billsteve@126.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/billsteve',

    install_requires=[
        "scrapy",
        "scrapyd",
        "scrapyd-client",
        "scrapy-redis",
        "pyquery",
        "redis",
        "requests",
        "pymysql",
        "sqlalchemy",
        "logzero",
        "happybase"
    ],

    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
