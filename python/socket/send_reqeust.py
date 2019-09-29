#!/usr/bin/python
# this is the program for socket communication
# it can be used both for server and client
# python socket_communication.py -server  for server
# python socket_communication.py -client  for client
# sys.argv[0]  : script name
# sys.argv[1]  : -server or -client
# sys.argv[2]  : string to send to server

import socket
import time
import sys
import os
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
#parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
parser.add_argument("-s", "--server",    action='store', default='client', choices=['server', 'client'], help="select server or client")
parser.add_argument("-c", "--cmd",       action='store', help="user command for server")

args = parser.parse_args()
print args

#answer = args.square ** 2
#
#if args.verbosity:
#    print('The square of {} equals {}'.format(args.square, answer))
#else:
#    print answer

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
#port = 1235
port = 16897
print 'host name is: %s' % host

# for server point
if 'server' is args.server:  #server
    print 'server program running'
    sock.bind((host, port))

    sock.listen(10)

    #connection.settimeout(5)
    while True:
        try:
            connection, address = sock.accept()

            received = connection.recv(1024)

            #send back to counerpart
            print 'Got connection from %s: %s' % (address, received)

            connection.send(received)
        except socket.timeout:
            print 'time out'

# for client point
if 'client' is args.server:  #client
    print 'client program running'
    #sock.connect((host, port))
    sock.connect(('10.238.65.115', port))
    #sock.connect(('10.122.117.64', port))
    #sock.connect(('10.123.81.7', port))
    loop = 1

    while True:
        print 'Send \'%s\'' % (args.cmd)
        print 'User Name: %s' % os.environ.get('USER')
        request_to_send = args.cmd + ' from ' + os.environ.get('USER') + '@' + host
        sock.send(request_to_send)      #send to server
        response_received = sock.recv(1024)  #receive the response from server
        if (response_received == request_to_send):
            print 'Your request is: %s' % response_received
            #time.sleep(1);
            break
        loop += 1


#both server point and client point need this operation
sock.close
