#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/2/23 18:15
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : Headless.py
# @Des         : 
# @Software : PyCharm
from selenium import webdriver


def get(url):
    options = webdriver.FirefoxOptions()
    options.set_headless()
    options.add_argument('-headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)
    driver.close()
    html = driver.page_source
    return html


if __name__ == '__main__':
    print(get("http://httpbin.org/get"))
