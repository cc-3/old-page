import os
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


__ALL__ = ['encrypt', 'decrypt']


BS = 16


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    if (type(s[-1]) == int):
        return s[0: -s[-1]]
    return s[0: -ord(s[-1])]


def encrypt(raw):
    rawkey = os.environ.get('AUTOGRADERS_KEY')
    key = hashlib.sha256(rawkey.encode()).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw)).decode()


def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    rawkey = os.environ.get('AUTOGRADERS_KEY')
    key = hashlib.sha256(rawkey.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:])).decode()
