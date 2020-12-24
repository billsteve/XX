# -*- coding: utf-8 -*-
import base64
import json
import os
import sqlite3

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from win32crypt import CryptUnprotectData


def get_string(local_state):
    with open(local_state, 'r', encoding='utf-8') as f:
        return json.load(f)['os_crypt']['encrypted_key']


def pull_the_key(base64_encrypted_key):
    encrypted_key_with_header = base64.b64decode(base64_encrypted_key)
    encrypted_key = encrypted_key_with_header[5:]
    key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return key


def decrypt_string(key, data):
    nonce, cipherbytes = data[3:15], data[15:]
    aesgcm = AESGCM(key)
    plainbytes = aesgcm.decrypt(nonce, cipherbytes, None)
    plaintext = plainbytes.decode('utf-8')
    return plaintext


def get_cookie_from_chrome(host='www.cnvd.org.cn'):
    import sys
    if sys.platform.lower().startswith("win"):
        local_state = os.environ['LOCALAPPDATA'] + r'\Google\Chrome\User Data\Local State'
        cookie_path = os.environ['LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"
    else:
        local_state = r'/root/.config/google-chrome/Default/Local State'
        cookie_path = r"/root/.config/google-chrome/Default/Cookies"

    # TODO:
    # if os.path.exists(cookie_path+".db"):
    #     os.remove(cookie_path+".db")
    #     print("removed",os.path.exists(cookie_path+".db"))
    # copyfile(cookie_path,cookie_path+".db")

    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookie_path) as conn:
        cu = conn.cursor()
        res = cu.execute(sql).fetchall()
        cu.close()
        cookies = {}
        key = pull_the_key(get_string(local_state))
        for host_key, name, encrypted_value in res:
            if encrypted_value[0:3] == b'v10':
                cookies[name] = decrypt_string(key, encrypted_value)
            else:
                cookies[name] = CryptUnprotectData(encrypted_value)[1].decode()
        return cookies


if __name__ == '__main__':
    s = get_cookie_from_chrome()
    print(s)
