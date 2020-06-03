# -*- coding: utf-8 -*-
import os


def create_model_by_url(url):
    os.system(f"sqlacodegen mysql+pymysql://{url}")


def create_model_by_config(host, port, user, pwd, db):
    create_model_by_url(f"{user}:{pwd}@{host}:{port}/{db}")

# # fp = "C:\\Users\\billsteve\\Desktop\\tmp\\"
# fp = "../Model/SqlAlchemy/T.py"
#
# link = "sqlacodegen mysql+pymysql://root:HBroot21@cd-cdb-f41yw26m.sql.tencentcdb.com:63626/company> "
# link = "sqlacodegen mysql+pymysql://root:HBroot21@cd-cdb-f41yw26m.sql.tencentcdb.com:63626/data_sheet> "
# link = "sqlacodegen mysql+pymysql://root:HBroot21@rm-8vbzabox9s9kvomq61o.mysql.zhangbei.rds.aliyuncs.com:3306/data_sheet> "
# # link = "sqlacodegen mysql+pymysql://root:HBroot21@cd-cdb-f41yw26m.sql.tencentcdb.com:63626/weibo> "
# link = "sqlacodegen mysql+pymysql://root:rebind1234@zh:3306/zhihu > "
# link = "sqlacodegen mysql+pymysql://root:rebind1234@zh:3306/money > "
# # link = "sqlacodegen mysql+pymysql://root:DRsXT5ZJ6Oi55LPQ@localhost:3306/music > "
# # link = "sqlacodegen mysql+pymysql://root:HBroot21@cd-cdb-f41yw26m.sql.tencentcdb.com:63626/money> "
# os.system(link + str(fp))
#
# content = open(fp, encoding="utf-8").read()
# # content = content.replace("INTEGER", "Integer").replace("BIGINT", "BigInteger")
# # content = re.sub("Integer(\(\d+\))", "Integer", content)
# # content = re.sub("BigInteger(\(\d+\))", "BigInteger", content)
# # open(fp, "w", encoding="utf-8").write(content)
# print(content)
