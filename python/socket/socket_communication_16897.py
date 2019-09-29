# this is the program for socket communication
# it can be used both for server and client
# python socket_communication.py -server  for server
# python socket_communication.py -client  for client

import wx
import socket
import time
import sys
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = sys.argv[0]

print('port=', sys.argv[0])

# for server point
if '-server' in sys.argv:  #server
    print('server program running')
    sock.bind(('localhost', 16897))
    sock.listen(5)

    connection, address = sock.accept()
    #connection.settimeout(5)
    while True:
        try:
            buf = connection.recv(1024)
            print(str(buf, encoding='utf-8'))
            print(buf)
            connection.send(buf)
        except socket.timeout:
            print('time out')

# for client point
if '-client' in sys.argv:  #client
    print('client program running')
    sock.connect(('localhost', 16897))
    time.sleep(1)
    while True:
        user_input = input('input anything:')
        now = datetime.datetime.now()
        print(now, user_input)
        sock.send(bytes(user_input, encoding='utf-8'))
        print(sock.recv(1024))


#both server point and client point need this operation
sock.close
