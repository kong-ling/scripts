#!/usr/bin/python
# -*- coding: latin-1 -*- 
# --------------------------------------------------------------------------------
# @Title: TRACE32 Remote API that use T32_Cmd() and T32_GetMessage()
# @Description: 
#  TRACE32 Remote API sample program illustrating the use of T32_Cmd() 
#  and T32_GetMessage() This demo send a command to TRACE32 PowerView 
#  and request any AREA message. 
#
#  Syntax:   t32apicmd.py  [--node <ip-address>]  [--port <num>]  <cmd>
#
#  Example:  t32apicmd.py --node localhost --port 20000 PRINT VERSION.BUILD()
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
# $Id: t32apicmd.py 80488 2017-01-15 17:28:05Z jvogl $ 
# 
 
import sys, getopt, ctypes, os, platform
from ctypes import *

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

### Setup connection
T32_OK = 0
WIN_MESSAGEMODENONE       = 0x00
WIN_MESSAGEMODEINFO       = 0x01
WIN_MESSAGEMODEERROR      = 0x02
WIN_MESSAGEMODESTATE      = 0x04
WIN_MESSAGEMODEWARNINFO   = 0x08
WIN_MESSAGEMODEERRORINFO  = 0x10
WIN_MESSAGEMODETEMP       = 0x20
WIN_MESSAGEMODETEMPINFO   = 0x40
node = ''
port = ''
cmd = ''
PROGNAME=os.path.basename(__file__)
def main(argv):
  try:
   opts, args = getopt.getopt(argv,"hn:p:",["node=","port="])
  except getopt.GetoptError:
    print('%s -n <node> -p <port>  <cmd>'%PROGNAME)
    sys.exit(2)
  node = 'localhost'
  port = '20000'
  cmd = ''
  
  for opt, arg in opts:
    if opt == '-h':
      print('%s --node <node> --port <port> <cmd>'%PROGNAME)
      sys.exit()
    elif opt in ("-n", "--node","-N","--NODE"):
      node = arg
    elif opt in ("-p", "--port","-P","--PORT"):
      port = arg
  option=0
  for i in range (1,len(sys.argv)):
    if option == 0:
      if sys.argv[i]=='-n' or sys.argv[i]=='-p' or sys.argv[i]=='-N' or sys.argv[i]=='-P' or sys.argv[i]=='--node' or sys.argv[i]=='--NODE' or sys.argv[i]=='--port' or sys.argv[i]=='--PORT' :
         option=1
      else :
        cmd= cmd + ' ' + sys.argv[i]
    else :
      option=0
  
  
  ### Debugger operation
  t32api.T32_Config(b"NODE=",node.encode('latin-1'))
  if t32api.T32_Config(b"PORT=",port.encode('latin-1'))!=T32_OK:
    print('Invalid port number',port,'specified.')
    sys.exit()
  t32api.T32_Config(b"PACKLEN=",b"1024")
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
  
 # send input command to TRACE32 PowerView for execution and return any message 
  if len(cmd)>2040:
    print('Failed to send remote command, command exceeds 2040 characters.')
    sys.exit()
  msgstring=create_string_buffer(50)
  msgtype=c_ulonglong(0)
  if t32api.T32_Cmd(b'PRINT')==T32_OK:
    if t32api.T32_Cmd(cmd.encode('latin-1'))==T32_OK:
      if t32api.T32_GetMessage(byref(msgstring), byref(msgtype))==T32_OK:
        if msgtype.value < (WIN_MESSAGEMODETEMPINFO << 1):
          if msgtype.value != WIN_MESSAGEMODENONE and not((len(msgstring.value) == 0) and (msgtype.value & (WIN_MESSAGEMODETEMPINFO | WIN_MESSAGEMODETEMP))):
            if msgtype.value & WIN_MESSAGEMODEINFO:
              print('info message:', msgstring.value)
            if msgtype.value & WIN_MESSAGEMODESTATE:
              print('status message:', msgstring.value)
            if msgtype.value & WIN_MESSAGEMODEWARNINFO:
              print('warning message:', msgstring.value)
            if (msgtype.value & WIN_MESSAGEMODEERRORINFO) or (msgtype.value & WIN_MESSAGEMODEERROR):
              print('error message:', msgstring.value)
            if (msgtype.value & WIN_MESSAGEMODETEMPINFO) or (msgtype.value & WIN_MESSAGEMODETEMP):
              print('miscellaneous message: %s' %msgstring.value)
          else:
            print('Successfully executed user command %s' %cmd)
        else:
          print('Failed to determine the type of the return message.')
      else:
        print('Failed to query return message.')
    else:
      print('Failed to execute erroneous user command %s' %cmd)
  else:
    print('Failed to execute \'T32_Cmd(""PRINT"")')
  print ("")

  if t32api.T32_Exit()!= T32_OK:
    print(' Failed to close the remote connection port on the dos shell application\'s side.')
  sys.exit()
if __name__ == "__main__":
   main(sys.argv[1:])