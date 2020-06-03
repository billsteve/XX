#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time        : 2018/7/26 18:17
# @Email       : billsteve@126.com
# @File          : ROOTPATH.py
# @Software  : PyCharm
# ROOT_PATH ===========格式是：root + project + FileType + item
import os
import traceback
import platform

sc = os.sep

if platform.platform().startswith("Win"):
    root_path = "C:\\Users\\billsteve\\Desktop\\tmp" + sc
    root_path = "D:\\tmp" + sc
else:
    root_path = "/home/data" + sc

root_path_log = root_path + "logs" + sc
root_path_liebao = root_path + "liebao" + sc
root_path_liebao_log = root_path_liebao + "logs" + sc
root_path_liebao_html = root_path_liebao + "html" + sc
root_path_liebao_cache = root_path_liebao + "cache" + sc
root_path_liebao_json = root_path_liebao_log + "jsons" + sc
root_path_liebao_font = root_path_liebao + "font" + sc
root_path_html = root_path + "html" + sc
root_path_cache = root_path_liebao_cache
EXCEPT_PATH = root_path_liebao_log + "parse_fail.log"
NO_MORE_PATH = root_path_liebao_log + "no_more.log"
NO_DATA_PATH = root_path_liebao_log + "no_data.log"
INCOMPLETE_PATH = root_path_liebao_log + "imcomplete.log"

# car
root_path_car = root_path + "car" + sc
root_path_car_html = root_path_car + "html" + sc
root_path_car_json = root_path_car + "json" + sc
root_path_car_json_car = root_path_car_json + "car" + sc
root_path_car_json_price = root_path_car_json + "price" + sc
root_path_car_json_sale = root_path_car_json + "sale" + sc
root_path_car_json_energy = root_path_car_json + "energy" + sc
root_path_car_html_level = root_path_car_html + "level" + sc

# 12315
root_path_12315 = root_path + "12315" + sc
root_path_12315_log = root_path + "log" + sc

# media
root_path_media = root_path + "media" + sc
root_path_media_html = root_path_media + "html" + sc
root_path_media_json = root_path_media + "json" + sc
root_path_media_log = root_path_media + "log" + sc
root_path_media_html_detail = root_path_media_html + "detail" + sc

# 智汉
root_path_zh = root_path + "zh" + sc
root_path_zh_cache = root_path_zh + "cache" + sc
root_path_zh_log = root_path_zh + "log" + sc
root_path_zh_json = root_path_zh + "json" + sc
root_path_zh_log_json = root_path_zh_log + "json" + sc

# GOV
root_path_gov = root_path + "gov" + sc
root_path_gov_cache = root_path_gov + "cache" + sc
root_path_gov_log = root_path_gov + "log" + sc
root_path_gov_json = root_path_gov + "json" + sc

# aiweibang
root_path_awb = root_path + "awb" + sc
root_path_awb_cache = root_path_awb + "cache" + sc
root_path_awb_log = root_path_awb + "log" + sc
root_path_awb_json = root_path_awb + "json" + sc

# LOG地址
Project_log = root_path_zh_log
EXCEPT_PATH = Project_log + "parse_fail.log"
NO_MORE_PATH = Project_log + "no_more.log"
NO_DATA_PATH = Project_log + "no_data.log"
INCOMPLETE_PATH = Project_log + "imcomplete.log"

# _var = vars()
# for k in dir():
#     if k.startswith("root_path"):
#         file_path = _var[k].strip().rstrip(os.sep)
#         isExists = os.path.exists(file_path)
#         if not isExists:
#             try:
#                 os.makedirs(file_path)
#             except:
#                 traceback.print_exc()
