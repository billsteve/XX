# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="XX",
    version=open("version.txt", encoding="utf-8").read(),
    description=(
        "Python tools for myself(billsteve@126.com)"
    ),
    long_description="""**Just Test, Just for myself!** 
    
    Not safe,not stable and will boom boom boom.

    Just like these:
        -  https://music.163.com/song?id=3949444&userid=319278554  
        -  https://music.163.com/song?id=474581010&userid=319278554  
        -  https://open.spotify.com/album/47wyCwrChF50ZTFNOuWx99  
        -  https://open.spotify.com/track/3oDFtOhcN08qeDPAK6MEQG  
    """,
    author='bill steve',
    author_email='billsteve@126.com',
    maintainer='bill steve',
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
        "happybase",
        "tld"
    ],

    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
