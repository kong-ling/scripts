import os
import sys
import re
import socket
import argparse
import datetime

class Client:
    def __init__(self, port = 1234):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        self.port = port
        sock.connect((host, port))

        while True:
            request_to_send = sys.argv[1]
            print(request_to_send)
            sock.send(str.encode(request_to_send))
            response_received = sock.recv(1024)
            if response_received == request_to_send:
                break

if __name__ == '__main__':
    Client(1234)
