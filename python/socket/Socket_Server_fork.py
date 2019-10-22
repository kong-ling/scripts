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

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        print 'Start handler\n'
        while True:
            f = open('cmd_received', 'w')
            data = self.request.recv(1024)
            #print 'Received data is : %s' % data
            f.write('%s' % data)
            self.request.send(data)
            #f.close()
        
host = socket.gethostname()
print 'Host name is: %s' % host

server = Server((host, 1234), Handler)
server.serve_forever()
