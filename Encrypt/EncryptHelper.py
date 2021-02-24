# -*- coding: utf-8 -*-
import base64
import hashlib


class Encrypt:
    @staticmethod
    def md5(string):
        return hashlib.new("md5", string.encode("utf-8")).hexdigest()


def base64_encode(s):
    base64.b64encode(str(s).encode('utf-8'))


def base64_decode(s):
    base64.b64decode(s).decode("utf-8")


if __name__ == '__main__':
    print(Encrypt.md5("1"))
