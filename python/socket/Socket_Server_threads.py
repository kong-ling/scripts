#from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
#
#class Server(ThreadingMixIn, TCPServer):
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
import threading
import signal
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

#open a terminal
os.system('xterm&');

mutex = threading.Lock()

current_working_dir = os.getcwd(); #current working directory
requests = current_working_dir + '/requests';
print('requests = %s' % requests);

#create folder for reqeusts
if not os.path.exists(os.getcwd() + '/request/'):
    os.mkdir(os.getcwd() + '/request/');

if os.path.isfile(requests):
    fh_requests = open(requests, 'r') #read
    connectionNumber = int(fh_requests.readline())
    print 'connectionNumber = %d\n' % connectionNumber
    fh_requests.close() #close the file
else:
    connectionNumber = 0

class Server(ThreadingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        global connectionNumber
        if mutex.acquire():
            connectionNumber += 1
            mutex.release()

        print 'Start handler : %5d' % connectionNumber
        addr = self.request.getpeername()
        print '  Got connection from', addr

        timeStamp     = time.strftime('%Y %m %d %A %X %Z',  time.localtime(time.time()))
        timeStamp_timezone  = time.strftime('%Z',  time.localtime(time.time())) # get timezone information
        datetimeStamp = datetime.datetime.now().strftime('%Y-%m-%d %A %X.%f') + ' ' + timeStamp_timezone

        #combine the file name
        connection = datetime.datetime.now().strftime('%Y-%m-%d_%A_%X.%f')
        #connection = datetime.datetime.now().strftime('%Y-%m-%d_%A_%H_%M_%S_%f')

        #write to file for loging
        request_log_name = os.getcwd() + '/request/' + connection + '_' + timeStamp_timezone 
        request_log = open(request_log_name, 'w') 
        
        ## just for debug
        #print('  request_log_name = %s' % request_log_name)
        #print '  Connection is %s' % request_log_name

        request_log.write('%s\n' % timeStamp) #the request time
        request_log.write('%s\n' % datetimeStamp) #the request time
        request_log.write('%s, %s\n' % addr)      #the request content

        data = self.request.recv(1024) #received info from requester
        print '  Request is : %s' % data
        request_log.write(data) #the request content

        #send back to the requester for acknoledge
        self.request.send(data)
        #os.system(data);
        request_log.close()
        return
        
host = socket.gethostname()
print 'Host name is: %s' % host
os.system('echo lingkong | mail -s "server info" kong.ling@intel.com -- -f kong.ling@intel.com');

#Enable the server to allow the reuse of an address
TCPServer.allow_reuse_address = True

server = Server((host, 1234), Handler)

#Once Ctrl+C is pressed, following function will be executed
# write the request number into a file for recording
def sigint_handler(signum, frame):
    global server
    print 'Ctrl+C is pressed!'
    
    fh_requests = open(requests, 'w') #write
    print 'connectionNumber = %d\n' % connectionNumber
    fh_requests.write(str(connectionNumber))
    fh_requests.close() #close the file
    print 'Shutdown server'
    print server.fileno()
    #server.shutdown() #close server
    print 'Shutdown complete'
    #server.serve_close()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)  #Ctrl+C will send SIGINT
signal.signal(signal.SIGTERM, sigint_handler) #kill PID works as well, SIGTERM


server.serve_forever()
