import time
import serial
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='parse the errlog for NOC obs')
parser.add_argument('-i', '--index', dest='index', required=False, help='register index')
parser.add_argument('-v', '--value', dest='value', required=False, help='register value')
args = parser.parse_args()

print(args.index)
print(args.value)

class noc_obs_log:
    def __init__(self, name, value):
        self.name = name
        self.lock = value & 0x1
        self.opc = (value >> 1) & 0xf
        self.errcode = (value >> 8) & 0x7
        self.len1 = (value >> 16) & ((1<<12) - 1)
        self.format = (value >> 31) & 0x1
        print('name   =%s' % self.name)
        print('lock   =%s' % self.lock)
        print('opc    =%s' % self.opc)
        print('errcode=%s' % self.errcode)
        print('len1   =%s' % self.len1)
        print('format =%s' % self.format)

if __name__ == '__main__':
    log = noc_obs_log('errlog0', int(args.value, 16))
