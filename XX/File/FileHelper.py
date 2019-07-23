# -*- encoding:utf8 -*-
import os
import shutil
import time
import traceback

import XX.Encrypt.EncryptHelper as cenc


def addLineN(key): return key + "\n" if key else key


# 文件帮助类
class FileHelper(object):
    """docstring for  FileHelper"""

    # 为行添加换行符
    def __init__(self, arg=""):
        super(FileHelper, self).__init__()
        self.arg = arg

    @staticmethod
    def getFileList(file_path, *arg, **kw):
        for parent, dirnames, filenames in os.walk(file_path):
            dirnames.sort()
            for filename in filenames:
                yield parent, filename

    @staticmethod
    def getFilleSize(fp, *args, **kw):
        return os.path.getsize(fp)

    @staticmethod
    def readFileContent(file_path, *arg, **kw):
        try:
            return open(file_path, "r", encoding="utf-8").read()
        except TypeError:
            return open(file_path, "r").read()
        except:
            traceback.print_exc()
            return

    @staticmethod
    def readFileLines(file_path, *arg, **kw):
        try:
            return open(file_path, "r", encoding="utf-8").readlines()
        except TypeError:
            return open(file_path, "r").readline()
        except:
            traceback.print_exc()
            return

    @staticmethod
    def saveFile(file_path, content="", method="a", *arg, **kw):
        try:
            FileHelper.mkdir(FileHelper.getFilePathAndName(file_path)[0])
            return open(file_path, method, encoding="utf-8").write(content)
        except TypeError:
            open(file_path, method).write(content)
            return len(content)
        except:
            traceback.print_exc()
            return

    @staticmethod
    def mkdir(file_path):
        file_path = file_path.strip()
        file_path = file_path.rstrip("\\")
        file_path = file_path.rstrip("/")
        isExists = os.path.exists(file_path)
        if not isExists:
            try:
                os.makedirs(file_path)
            except:
                traceback.print_exc()
                return
        return True

    @staticmethod
    def getFilePathAndName(filename):
        return os.path.split(filename)

    @staticmethod
    def getFileExt(filename):
        return os.path.splitext(filename)

    @staticmethod
    def renameFile(filename, tofilename):
        return os.rename(filename, tofilename)

    @staticmethod
    def isFileExit(fpath):
        return 1 if os.path.isfile(fpath) else 0

    @staticmethod
    def removeFile(fpath, ts=0):
        if ts and FileHelper.isFileExit(fpath) and time.time() - os.path.getmtime(fpath) > ts:
            if FileHelper.isFileExit(fpath):
                if int(time.time()) - FileHelper.getCreateTs(fpath) > ts:
                    os.remove(fpath)
                return not FileHelper.isFileExit(fpath)
            else:
                return 1
        elif FileHelper.isFileExit(fpath):
            os.remove(fpath)
            return not FileHelper.isFileExit(fpath)
        else:
            return 1

    @staticmethod
    def moveFile(ffrom, fto):
        FileHelper.mkdir(FileHelper.getFilePathAndName(fto)[0])
        if not FileHelper.isFileExit(fto):
            return shutil.move(ffrom, fto)
        else:
            return -1

    @staticmethod
    # c\4\c\c4ca4238a0b923820dcc509a6f75849b
    def getMd5Name(hash_string):
        md5_str = cenc.Encrypt.md5(hash_string)
        return md5_str[0] + os.sep + md5_str[1] + os.sep + md5_str[2] + os.sep + md5_str

    @staticmethod
    def copy(ffrom, fto):
        FileHelper.mkdir(FileHelper.getFilePathAndName(fto)[0])
        try:
            return shutil.copy(ffrom, fto)
        except shutil.SameFileError as e:
            print(e)
            return 0

    @staticmethod
    def mk16dir(root_path):
        words = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        len_file = len(words)
        for i in range(len_file):
            for j in range(len_file):
                for k in range(len_file):
                    FileHelper.mkdir(root_path + str(words[i]) + os.sep + str(words[j]) + os.sep + str(words[k]) + os.sep)
                    print(root_path + str(words[i]) + os.sep + str(words[j]) + os.sep + str(words[k]) + os.sep)

    # 获取文件创建时间
    @staticmethod
    def getCreateTs(fp):
        return os.path.getctime(fp)

    # 获取更新时间
    @staticmethod
    def getUpdateTs(fp):
        return os.path.getmtime(fp)

    # 添加PYTHONPAH
    @staticmethod
    def addPythonPath(path):
        import sys
        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), path)))

    # 修改后缀名
    @staticmethod
    def modifySuffix(fp, suffix):
        if FileHelper.isFileExit(fp):
            portion = os.path.splitext(fp)
            new_name = portion[0] + "." + str(suffix)
            os.rename(fp, new_name)
        else:
            raise FileNotFoundError


if __name__ == "__main__":
    pass
    # print(FileHelper.getFileName("E:\\t82.html"))
    # print(FileHelper.getFileExt("E:\\t82.html"))

    # FileHelper.saveFile("E:\\ele\\ele\\111.txt", "12121")
    # print(FileHelper.getMd5Name("1"))

    r = FileHelper.removeFile("C:\\Users\\billsteve\\Desktop\\tmp\\1.txt")
    print(r)
    # print(FileHelper.getUpdateTs("d:\\1.html"))
