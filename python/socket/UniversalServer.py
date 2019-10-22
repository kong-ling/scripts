import os
import sys
import re
import socket
import argparse
import datetime

class Server:
    def __init__(self, port = 1234):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        self.port = port
        sock.bind((host, port))
        sock.listen(10)

        while True:
            try:
                print(datetime.datetime.now())
                connection, address = sock.accept()
                received = connection.recv(1024)
                print('Connection from %s:%s' % (address, received))
                print('Received=[%s]' % received)
                connection.send(received)
            except:
                print('timeout')

if __name__ == '__main__':
    Server(1234)
