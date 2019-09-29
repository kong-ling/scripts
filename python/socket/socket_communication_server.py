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
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
#ec_sise = os.environ['EC_SITE']
ec_sise = ''
#host = host + '.' + ec_sise + '.intel.com'
port = 1234
print('host name is: %s' % host)

# for server point
if '-server' in sys.argv:  #server
    print('server program running')
    sock.bind((host, port))

    sock.listen(10)

    #connection.settimeout(5)
    while True:
        try:
            print('\n\n')
            print(datetime.datetime.now())
            print('Wait for new request ...')
            print('\n\n')
            connection, address = sock.accept()

            received = connection.recv(1024)

            #send back to counerpart
            print('Got connection from %s: %s' % (address, received))

            connection.send(received)

            #convert the command to sting for host to run
            cmd_seq = received.split(' ')
            cmd = ''
            for seq in cmd_seq:
                if '@' not in seq and 'from' not in seq:
                    cmd = cmd + ' ' + seq
            print('received=[%s]' % received)
            cmd_strip = cmd.strip()
            print('cmd=[%s]' % cmd.strip)
            os.system(cmd_strip)
        except socket.timeout:
            print('time out')

# for client point
if '-client' in sys.argv:  #client
    #print 'client program running'
    sock.connect((host, port))
    loop = 1

    #send sys.argv[1], and wait for response from server
    #if the recevied from the server is the same as sys.argv[1], exit the program
    #otherwise, retransmit the string
    while True:
        #print 'Send \'%s\'' % (sys.argv[2])
        #print 'User Name: %s' % os.environ.get('USER')
        #request_to_send = sys.argv[2] + ' from ' + os.environ.get('USER') + '@' + host
        request_to_send = sys.argv[2]
        sock.send(request_to_send)      #send to server
        response_received = sock.recv(1024)  #receive the response from server
        if (response_received == request_to_send):
            print('Your request is: [%s]' % response_received)
            #time.sleep(1);
            break
        loop += 1


#both server point and client point need this operation
sock.close
