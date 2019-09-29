#coding: utf8
#!/usr/bin/env python
#! usr/bin/python
#coding=utf-8

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Crypto import Random

# padding
BS = AES.block_size # aes128 bit
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
        # 这里统一把加密后的字符串转化为16进制字符串
        # 在下节介绍base64时解释原因
        return b2a_hex(iv + ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = a2b_hex(ciphertext)
        iv = ciphertext[0:AES.block_size]
        ciphertext = ciphertext[AES.block_size:len(ciphertext)]
        cryptor = AES.new(self.key, self.mode, iv)
        plaintext = cryptor.decrypt(ciphertext)
        return plaintext.rstrip(chr(0))

# 测试模块
if __name__ == '__main__':
    # 密钥长度可以为128 / 192 / 256比特，这里采用128比特
    # 指定加密模式为CBC
    demo = aesdemo(b'keyven__keyven__', AES.MODE_CBC)
    import sys
    e = demo.encrypt(sys.argv[1])
    d = demo.decrypt(e)
    print "encrypto: ", e
    print "decrypto: ", d
