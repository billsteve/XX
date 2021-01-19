# -*- encoding:utf8 -*-
import os
import shutil
import time

import XX.Encrypt.EncryptHelper as cenc


def addLineN(key): return key + "\n" if key else key


# 文件帮助类
class FileHelper(object):

    # 为行添加换行符
    def __init__(self, arg=""):
        super(FileHelper, self).__init__()
        self.arg = arg

    @staticmethod
    def get_file_list(file_path, *arg, **kw):
        for parent, dir_names, file_names in os.walk(file_path):
            dir_names.sort()
            for filename in file_names:
                yield parent, filename

    @staticmethod
    def get_file_size(fp, *args, **kw):
        return os.path.getsize(fp)

    @staticmethod
    def read_file_content(file_path, *arg, **kw):
        try:
            return open(file_path, "r", encoding="utf-8").read()
        except TypeError:
            return open(file_path, "r").read()
        except:
            raise

    @staticmethod
    def read_file_lines(file_path, *arg, **kw):
        try:
            return open(file_path, kw.get("method", "r"),
                        encoding=kw.get("encoding", "utf-8")).readlines()
        except TypeError:
            return open(file_path, "r").readline()
        except:
            raise

    @staticmethod
    def save_file(file_path, content="", method="a", *arg, **kw):
        try:
            FileHelper.mkdir(FileHelper.get_file_path_and_name(file_path)[0])
            return open(file_path, method, encoding=kw.get("encoding", "utf-8")).write(content)
        except TypeError:
            open(file_path, method).write(content)
            return len(content)
        except:
            raise

    @staticmethod
    def remove_dir(file_path):
        if not file_path:
            return
        file_path = file_path.strip()
        file_path = file_path.rstrip("\\")
        file_path = file_path.rstrip("/")
        isExists = os.path.exists(file_path)
        if isExists:
            shutil.rmtree(file_path)
        return True

    @staticmethod
    def mkdir(file_path):
        if not file_path:
            return
        file_path = file_path.strip()
        file_path = file_path.rstrip("\\")
        file_path = file_path.rstrip("/")
        exists = os.path.exists(file_path)
        if not exists:
            os.makedirs(file_path)
        return True

    @staticmethod
    def get_file_path_and_name(filename):
        if not filename:
            return None, None
        return os.path.split(filename)

    @staticmethod
    def get_file_ext(filename):
        return os.path.splitext(filename)

    @staticmethod
    def rename_file(filename, to_filename):
        return os.rename(filename, to_filename)

    @staticmethod
    def is_file_exit(path):
        return 1 if path and os.path.isfile(path) else 0

    @staticmethod
    def remove_file(path, ts=0):
        if ts and FileHelper.is_file_exit(path) and time.time() - os.path.getmtime(path) > ts:
            if FileHelper.is_file_exit(path):
                if int(time.time()) - FileHelper.get_create_ts(path) > ts:
                    os.remove(path)
                return not FileHelper.is_file_exit(path)
            else:
                return 1
        elif FileHelper.is_file_exit(path):
            os.remove(path)
            return not FileHelper.is_file_exit(path)
        else:
            return 1

    @staticmethod
    def move_file(ffrom, fto):
        FileHelper.mkdir(FileHelper.get_file_path_and_name(fto)[0])
        if not FileHelper.is_file_exit(fto):
            return shutil.move(ffrom, fto)
        else:
            return -1

    @staticmethod
    # c\4\c\c4ca4238a0b923820dcc509a6f75849b
    def get_md5_name(hash_string):
        md5_str = cenc.Encrypt.md5(hash_string)
        return md5_str[0] + os.sep + md5_str[1] + os.sep + md5_str[2] + os.sep + md5_str

    @staticmethod
    def copy(file_from, file_to):
        FileHelper.mkdir(FileHelper.get_file_path_and_name(file_to)[0])
        return shutil.copy(file_from, file_to)

    @staticmethod
    def mk16dir(root_path):
        words = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        len_file = len(words)
        for i in range(len_file):
            for j in range(len_file):
                for k in range(len_file):
                    FileHelper.mkdir(
                        root_path + str(words[i]) + os.sep + str(words[j]) + os.sep + str(words[k]) + os.sep)
                    print(root_path + str(words[i]) + os.sep + str(words[j]) + os.sep + str(words[k]) + os.sep)

    # 获取文件创建时间
    @staticmethod
    def get_create_ts(fp):
        return os.path.getctime(fp)

    # 获取更新时间
    @staticmethod
    def get_update_ts(fp):
        return os.path.getmtime(fp)

    # 添加PYTHON环境变量
    @staticmethod
    def add_python_path(path):
        import sys
        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), path)))

    # 修改后缀名
    @staticmethod
    def modify_suffix(fp, suffix):
        if FileHelper.is_file_exit(fp):
            portion = os.path.splitext(fp)
            new_name = portion[0] + "." + str(suffix)
            os.rename(fp, new_name)
        else:
            raise FileNotFoundError


if __name__ == "__main__":
    pass
    # print(FileHelper.getFileName("E:\\t82.html"))
    # print(FileHelper.getFileExt("E:\\t82.html"))

    # FileHelper.saveFile("E:\\ele\\ele\\111.log", "12121")
    # print(FileHelper.getMd5Name("1"))

    r = FileHelper.remove_file("C:\\Users\\billsteve\\Desktop\\tmp\\1.log")
    print(r)
    # print(FileHelper.getUpdateTs("d:\\1.html"))
