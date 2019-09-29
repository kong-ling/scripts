#!/usr/bin/env python
#! usr/bin/python #coding=utf-8

from Crypto.Cipher import AES
import base64
from Crypto import Random

# padding算法
BS = AES.block_size # aes数据分组长度为128 bit
pad = lambda s: s + (BS - len(s) % BS) * chr(0) 

class aesdemo:
    def __init__(self, key,mode):
        self.key = key
        self.mode = mode

    def encrypt(self, plaintext):
        # 生成随机初始向量IV
        iv = Random.new().read(AES.block_size)
        cryptor = AES.new(self.key, self.mode, iv)
        ciphertext = cryptor.encrypt(pad(plaintext))
        print 'ciphertext %s' % ciphertext
        return base64.encodestring(iv + ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = base64.decodestring(ciphertext)
        iv = ciphertext[0:AES.block_size]
        ciphertext = ciphertext[AES.block_size:len(ciphertext)]
        cryptor = AES.new(self.key, self.mode, iv)
        plaintext = cryptor.decrypt(ciphertext)
        return plaintext.rstrip(chr(0))

# 测试模块
if __name__ == '__main__':
    demo = aesdemo(b'keyven__keyven__', AES.MODE_CBC)
    import sys
    e = demo.encrypt(sys.argv[1])
    d = demo.decrypt(e)
    print "encryto: ", e
    print "decryto: ", d
