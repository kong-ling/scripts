import ctypes
import enum

#Load TRACE32 Remote API DLL
pl2303 = ctypes.cdll.LoadLibrary('PL2303DLL.dll')
#pl2303 = ctypes.WinDLL.LoadLibrary('PL2303DLL.dll')

print('pl2303 handling\n')

