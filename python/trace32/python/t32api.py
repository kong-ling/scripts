#!/usr/bin/python
# -*- coding: latin-1 -*-
# --------------------------------------------------------------------------------
# @Title: Very simple python example using the TRACE32 Remote API
# @Description: 
#  TRACE32 Remote API sample program written in Python, illustrating
#  the use of T32_Cmd() for sending a command to TRACE32 PowerView
#  via the TRACE32 remote API
#
#  TRACE32's configuration file "config.t32" has to contain these lines:
#    RCL=NETASSIST
#    PORT=20000
#  The port value may be changed but has to match with the port number 
#  used in this python script.
#
# @Keywords: python
# @Author: PHA, HLG
# @Copyright: (C) 1989-2015 Lauterbach GmbH, licensed for use with TRACE32(R) only
# --------------------------------------------------------------------------------
# $Id: t32api.py 80488 2017-01-15 17:28:05Z jvogl $ 
# 

import platform
import ctypes

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

t32api.T32_Config(b"NODE=",b"localhost")
t32api.T32_Config(b"PORT=",b"20000")
t32api.T32_Config(b"PACKLEN=",b"1024")

t32api.T32_Init()
t32api.T32_Attach(1)
t32api.T32_Ping()

t32api.T32_Cmd(b"AREA")

t32api.T32_Exit()
