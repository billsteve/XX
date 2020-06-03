# -*- coding:utf-8 -*-
import XX.File.FileHelper as cf


def log_file(file_path, content, method="a"):
    try:
        return cf.FileHelper.saveFile(file_path, content, method)
    except:
        import traceback
        traceback.print_exc()
        return


def logToady(file_path, content):
    pass


def get_logger():
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
    # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
    logging.info('this is a loggging info message')
    logging.debug('this is a loggging debug message')
    logging.warning('this is loggging a warning message')
    logging.error('this is an loggging error message')
    logging.critical('this is a loggging critical message')

# get_logger()