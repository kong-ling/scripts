#! /usr/bin/python
# code for linux
import socket
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:
    try:
        print(s.recvfrom(65535))
    except:
        print('except')
        pass

