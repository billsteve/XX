# -*- coding: utf-8 -*-
import hashlib


class Encrypt():
    @staticmethod
    def md5(string):
        return hashlib.new("md5", string.encode("utf-8")).hexdigest()


if __name__ == '__main__':
    print(Encrypt.md5("1"))
