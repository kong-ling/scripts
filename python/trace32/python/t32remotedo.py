#!/usr/bin/python
# -*- coding: latin-1 -*- 
# --------------------------------------------------------------------------------
# @Title: Python script sending all commands of a PRACTICE script to TRACE32 
# @Description: 
#  The program creates a connection to TRACE32 and sends all commands from the
#  specified PRACTICE file (*.cmm) to TRACE32 for execution.
#  It can also be called without a file name but it will wait for a command list
#  that should end with CTRL+Z
#
#  The port on which TRACE32 listens for API connections can optionally be
#  set with the --port <n> parameter.
#
#  Syntax:   t32remotedo.py [--node <ip-address>] [--port <number>] [file]
#
#  Example:  t32remotedo.py  --node localhost --port 20002 test1.cmm test2.cmm
#  Example:  t32remotedo.py  --node localhost --port 20002 
#            go
#            break
#            step
#            ^Z
#
#  TRACE32's configuration file "config.t32" has to contain these lines:
#    RCL=NETASSIST
#    PORT=20000
#  The port value may be changed but has to match with the port number 
#  used with this python script.
#
# @Keywords: python
# @Author: WBA
# @Copyright: (C) 1989-2015 Lauterbach GmbH, licensed for use with TRACE32(R) only
# --------------------------------------------------------------------------------
# $Id: t32remotedo.py 80488 2017-01-15 17:28:05Z jvogl $ 
# 

import sys, getopt, ctypes, array, atexit, signal, os, platform
from ctypes import *
from signal import SIGINT

# auto-detect the correct library
if (platform.system()=='Windows') or (platform.system()[0:6]=='CYGWIN') :
  if ctypes.sizeof(ctypes.c_voidp)==4:
    # WINDOWS 32bit
    t32api = ctypes.CDLL("./t32api.dll")
    # alternative using windows DLL search order:
#   t32api = ctypes.cdll.t32api
  else:
    # WINDOWS 64bit
    t32api = ctypes.CDLL("./t32api64.dll")
    # alternative using windows DLL search order:
#   t32api = ctypes.cdll.t32api64
elif platform.system()=='Darwin' :
  # Mac OS X
  t32api = ctypes.CDLL("./t32api.dylib")
else :
  if ctypes.sizeof(ctypes.c_voidp)==4:
    # Linux 32bit
    t32api = ctypes.CDLL("./t32api.so")
  else:
    # Linux 64bit
    t32api = ctypes.CDLL("./t32api64.so")

T32_OK = 0
EXIT_SUCCESS=0
EXIT_FAILURE=1
PROGNAME=os.path.basename(__file__)
def help():
  print(" %s [OPTION]... [FILE]..." %(PROGNAME))
  print("") 
  print("Mandatory arguments to long options are mandatory for short options too.")
  print("-h, --help                 print this help text")
  print("-n, --node=NODE            the node name of the Trace32 instance")
  print("-l, --packlen=PACKLEN      the packet length to use")
  print("-p, --port=PORT            the port of the Trace32 instance")
  print("-v, --verbose              print commands sent to Trace32 instance")
  
def atexit_handler():
  t32api.T32_Exit()

def signal_handler(sig1, sig2):
  sys.exit(EXIT_FAILURE)

def send_commands(file, verbose):
  line = create_string_buffer(800)
  for line in file: 
    line=line.rstrip()
    if (verbose=='1') :
      print(line)
    error = t32api.T32_Cmd(line.encode('latin-1'))
    if (error != T32_OK) :
      print("command failed: \"%s\""% (line))
      sys.exit(EXIT_FAILURE)

def main(argv):
  try:
   opts, args = getopt.getopt(argv,"hn:l:p:v:",["node=","packlen=","port=","verbose="])
  except getopt.GetoptError:
    help()
    sys.exit(EXIT_FAILURE)
  node = 'localhost'
  port = '20000'
  packlen = '1024'
  verbose = '0'
  for opt, arg in opts:
    if opt == '-h':
      help()
      sys.exit(EXIT_SUCCESS)
    elif opt in ("-n", "--node","-N","--NODE"):
      node = arg
    elif opt in ("-l", "--packlen","-L","--PACKLEN"):
      packlen = arg
    elif opt in ("-p", "--port","-P","--PORT"):
      port = arg
    elif opt in ("-v", "--verbose","-V","--VERBOSE"):
      verbose = arg
  option=0
  j=0
  max=0
  listoffiles=array.array('i',list(range(50)))
  for i in range (1,len(sys.argv)):
    if option == 0:
      if sys.argv[i]=='-n' or sys.argv[i]=='-p' or sys.argv[i]=='-N' or sys.argv[i]=='-P' or sys.argv[i]=='--node' or sys.argv[i]=='--NODE' or sys.argv[i]=='--port'  \
      or sys.argv[i]=='--PORT' or sys.argv[i]=='-l' or sys.argv[i]=='-L' or sys.argv[i]=='-v' or sys.argv[i]=='-V' or sys.argv[i]=='--packlen' or sys.argv[i]=='--PACKLEN' or \
      sys.argv[i]=='--verbose' or sys.argv[i]=='--VERBOSE':
         option=1
      else :
        listoffiles[j]= i
        j+=1
        max=j
    else :
      option=0
  if t32api.T32_Config(b"NODE=",node.encode('latin-1'))!=T32_OK:
    print('invalid node: %s' %(node))
    sys.exit(1)
  if t32api.T32_Config(b"PACKLEN=",packlen.encode('latin-1'))!=T32_OK:
    print('invalid packet length: %s' %(packlen))
    sys.exit(1)
  if t32api.T32_Config(b"PORT=",port.encode('latin-1'))!=T32_OK:
    print('port number %s not accepted' %(port))
    sys.exit(1)
  print('Connecting...')
  for i in range (1, 3):
    if t32api.T32_Init()==T32_OK:
      if t32api.T32_Attach(1)==T32_OK:
        print('Successfully established a remote connection with TRACE32 PowerView.')
        break
      else :
        if i==1:
          print('Failed once to established a remote connection with TRACE32 PowerView.')
          t32api.T32_Exit()
        elif i==2 :
          print('Failed twice to established a remote connection with TRACE32 PowerView.')
          print(' Terminating ...')
          sys.exit()
    else :
      if i==1:
        print('Failed once to initialize a remote connection with TRACE32 PowerView.')
        t32api.T32_Exit()
      elif i==2 :
        print('Failed twice to initialize a remote connection with TRACE32 PowerView.') 
        print(' Terminating ...')
        sys.exit()
 
  atexit.register(atexit_handler)
  signal.signal(SIGINT, signal_handler)
  for i in range (0,max):
    try:
      file = open(sys.argv[listoffiles[i]], 'r')
      send_commands(file, verbose)
      file.close()
    except IOError:
      print("cannot open file %s" % (sys.argv[listoffiles[i]]))
    
  if max==0:  
    data = sys.stdin.readlines()
    send_commands(data, verbose)
  sys.exit(EXIT_SUCCESS)
if __name__ == "__main__":
 main(sys.argv[1:])