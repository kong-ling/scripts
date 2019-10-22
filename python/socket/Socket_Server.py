#from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler
#
#class Server(ForkingMixIn, TCPServer):
#    pass
#
#class Handler(StreamRequestHandler):
#    def handler(self):
#        addr = self.request.getpeername()
#        print 'Got Connections from'.addr
#        self.wfile.write('Thank you for connecting')
#
#server = Server(('localhost', 1234), Handler)
#server.serve_forever()
import socket
import sys
import os
import time
import datetime

connectionNumber = 0

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        print 'Start handler'
        addr = self.request.getpeername()
        print 'Got connection from', addr

        timeStamp     = time.strftime('%Y %m %d %A %X %Z',  time.localtime(time.time()))
        datetimeStamp = datetime.datetime.now().strftime('%Y-%m-%d %A %X.%f %Z')

        #combine the file name
        connection = datetime.datetime.now().strftime('%Y-%m-%d_%A_%X.%f_%Z')


        #write to file for loging
        reques_log = open(connection, 'w') 

        print 'Connection is %s' % connection
        reques_log.write('%s\n' % timeStamp) #the request time
        reques_log.write('%s\n' % datetimeStamp) #the request time
        reques_log.write('%s, %s\n' % addr)      #the request content

        data = self.request.recv(1024)
        print 'Request is : %s' % data
        reques_log.write(data) #the request content
        self.request.send(data)
        #os.system(data);
        reques_log.close()
        return
        
host = socket.gethostname()
print 'Host name is: %s' % host

server = Server((host, 1234), Handler)
server.serve_forever()
