import ctypes
import enum

#Load TRACE32 Remote API DLL
t32api = ctypes.cdll.LoadLibrary('t32api64.dll')

#TRACE32 Debugger or Simulator as debug device
T32_DEV = 1

#Configuire communication channel to the Trace32 device
# use b for byte encoding of strings
t32api.T32_Config(b'NODE=', b'localhost')
t32api.T32_Config(b'PORT=', b'20000')
t32api.T32_Config(b'PACKLEN=', b'1024')

#Establish communication channel
rc = t32api.T32_Init()
rc = t32api.T32_Attach(T32_DEV)
rc = t32api.T32_Ping()

#Trace32 control commands
rc = t32api.T32_Cmd(b'per.set.simple E:0x30000C %long 0xabcdbeef')
rc = t32api.T32_Cmd(b'per.set.simple E:0x30001C %long 0xbeefabcd')
rc = t32api.T32_Cmd(b'print %color.red "hello"')
#Release communication channel
rc = t32api.T32_Exit()
