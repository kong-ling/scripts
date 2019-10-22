#
#  TRACE32 Remote API sample program written in Python, illustrating
#  the use of T32_Cmd() for sending a command to TRACE32 PowerView.
#
#  For remote access TRACE32's configuration file "config.t32" has to contain these lines:
#
#    RCL=NETASSIST
#    PORT=20000
#
#  This default port value may be changed but has to match the subsequently specified value.
#  This sample program also shows how to establish and close a remote connection with TRACE32.
#
#  (C) 1989-2014 Lauterbach GmbH, licensed for use with TRACE32(R) only
#
##############################################################################################


from ctypes import *
t32api  = CDLL("./t32api.so")

t32api.T32_Config("NODE=","localhost")
t32api.T32_Config("PORT=","20000")
t32api.T32_Config("PACKLEN=","1024")

t32api.T32_Init()
t32api.T32_Attach(1)
t32api.T32_Ping()

t32api.T32_Cmd("AREA")

t32api.T32_Exit()
