#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time       : 2019/4/30 9:58
# @Author    : Bill Steve
# @Email      : billsteve@126.com
# @File         : UpgradeAllPackage.py
# @Des         : 
# @Software : PyCharm
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call

for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name + " -i https://pypi.douban.com/simple ", shell=True)
