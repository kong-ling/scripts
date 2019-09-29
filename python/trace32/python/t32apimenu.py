#!/usr/bin/python
# -*- coding: latin-1 -*- 
# --------------------------------------------------------------------------------
# @Title: Python example demonstrating various functions of the TRACE32 remote API
# @Description:
#  After establishing a remote connection with TRACE32 PowerView a menu offers
#  various API commands for selection. For accessing real HW the data memory 
#  location can be specified by <hexaddr>.
#
#  Syntax:   t32apimenu.py [--node <ip-addr>] [--port <num>] [--address <hexaddr>]
#
#  Example:  t32apimenu.py --node localhost --port 20000 --address 0x400C000
#
#  TRACE32's configuration file "config.t32" has to contain these lines:
#    RCL=NETASSIST
#    PORT=20000
#  The port value may be changed but has to match with the port number 
#  used with this python script.
#
#
# @Keywords: python
# @Author: WBA
# @Copyright: (C) 1989-2015 Lauterbach GmbH, licensed for use with TRACE32(R) only
# --------------------------------------------------------------------------------
# $Id: t32apimenu.py 80488 2017-01-15 17:28:05Z jvogl $ 
#

import sys, getopt, time, ctypes, array, os, platform
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

T32_OK = 0
T32_MEMORY_ACCESS_DATA=0
sel = '  '
address = 0xffffffff
pcval = c_long(0xffffffff)
wp = array.array('i', list(range(512)))
wpbuffer = (c_ulong * 256).from_buffer(wp) 
wpbuffer[0]=0xcafefeca
rw = array.array('i', list(range(4)))
rwbuffer = (c_ulong * 2).from_buffer(rw) 
rwbuffer[0] = 0xcafefeca
rwbuffer[1] = 0xbabebeba
ui32val = array.array('i', list(range(16)))
pui32val = (c_ulong * 8).from_buffer(ui32val) 
ui16val = array.array('i', list(range(64)))
pui16val = (c_ushort * 32).from_buffer(ui16val) 
EXIT_SUCCESS=0
EXIT_FAILURE=1
T32_MEMORY_ACCESS_PROGRAM=0x1
retval = EXIT_SUCCESS
PROGNAME=os.path.basename(__file__)

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()


def main(argv):
  try:
   opts, args = getopt.getopt(argv,"hn:p:a:",["node=","port=","address="])
  except getopt.GetoptError:
    print(" %s [--node <name_or_IP>] [--port <num>] [--address <hexaddr>]" %(PROGNAME))
    sys.exit(EXIT_FAILURE)
  node = 'localhost'
  port = '20000'
  hexaddr = '0xffffffff'
  string=create_string_buffer(50)
  string='Data.DUMP D:0x1000      '
  sel=create_string_buffer(3)
  sel='  '
  for opt, arg in opts:
    if opt == '-h':
      print("")
      print(" Syntax: %s [--node <name_or_IP>] [--port <num>] [--address <hexaddr>]" %(PROGNAME))
      print(" Example: %s  --node localhost   --port 20000  --address 0x400C000" % (PROGNAME))
      print("")
      print(" Hexaddress is used by Read/WriteMemory if real hardware is accessed.")
      print("")
      sys.exit(EXIT_SUCCESS)
    elif opt in ("-n", "--node","-N","--NODE"):
      node = arg
    elif opt in ("-p", "--port","-P","--PORT"):
      port = arg
    elif opt in ("-a", "--address","-A","--ADDRESS"):
      hexaddr = arg  
  address=hexaddr
  address=int(address,16)
  j=1
  m=0
  ### Debugger operation
  t32api.T32_Config(b"NODE=",node.encode('latin-1'))
  if t32api.T32_Config(b"PORT=",port.encode('latin-1'))!=T32_OK:
    print(' Invalid port number \'%s\' specified.'%(port))
    sys.exit(EXIT_FAILURE)
  t32api.T32_Config(b"PACKLEN=",b"1024")
  print("")
  print(' Connecting...')
  for i in range (1, 3):
    if t32api.T32_Init()==T32_OK:
      if t32api.T32_Attach(1)==T32_OK:
        print(' Successfully established a remote connection with TRACE32 PowerView.')
        break
      else :
        if i==1:
          print(' Failed once to established a remote connection with TRACE32 PowerView.')
          t32api.T32_Exit()
        elif i==2 :
          print(' Failed twice to established a remote connection with TRACE32 PowerView.')
          print(' Terminating ...')
          sys.exit(EXIT_FAILURE)
    else :
      if i==1:
        print(' Failed once to initialize a remote connection with TRACE32 PowerView.')
        t32api.T32_Exit()
      elif i==2 :
        print(' Failed twice to initialize a remote connection with TRACE32 PowerView.') 
        print(' Terminating ...')
        sys.exit(EXIT_FAILURE)
  
 # send input command to TRACE32 PowerView for execution and return any message 
  if hexaddr[0]=='0' and hexaddr[1]=='x':
    list1 = list(string)
    for i in range (0,len(hexaddr)):
      list1[12+i] = hexaddr[i]
    if 12+len(hexaddr)<len(list1):
      for i in range (12+len(hexaddr),len(list1)):
        list1[i]=''
    string= ''.join(list1)
  else:
    print('Invalid hexaddress',hexaddr, ' specified.')
    sys.exit(EXIT_FAILURE)
 # setup TRACE32 PowerView in order to display all important information
  
  systemstate =c_uint(0)
  t32api.T32_Cmd(b"WINCLEAR APIWin1")
  t32api.T32_Cmd(b"WINCLEAR APIWin2")
  t32api.T32_Cmd(b"WINCLEAR APIWin3")
  t32api.T32_Cmd(b"WINCLEAR APIWin4")
  t32api.T32_Cmd(b"WINCLEAR APIWin5")
  t32api.T32_Cmd(b"WINCLEAR APIWin6")
  t32api.T32_Cmd(b"PRINT")
  t32api.T32_Cmd(b"PRINT")
  t32api.T32_Cmd(b"WINPOS 0 15% , , , , APIWin1")
  t32api.T32_Cmd(b"SYStem")
  t32api.T32_Cmd(b"WINPOS 0 0 40% 35% , , APIWin2")
  t32api.T32_Cmd(b"AREA")
  t32api.T32_Cmd(b"WINPOS 0 60% 40% 45% , , APIWin3")
  t32api.T32_Cmd(b"Register /SpotLight")
  t32api.T32_Cmd(b"EVAL SIMULATOR()")
  retval = t32api.T32_EvalGet(pui32val)
  if ((retval != T32_OK) or (pui32val[0] == 0)) :    #/* marginal setup in case of */
    t32api.T32_Cmd(b"WINPOS 40% 0 60% 40% , , APIWin4")  #/* real HW or eval-failure   */
    t32api.T32_Cmd(b"Data.List")
    t32api.T32_Cmd(b"WINPOS 40% 40% 60% 40% , , APIWin5")
    t32api.T32_Cmd(string.encode('latin-1'))
    if (address == 0xffffffff) :
      t32api.T32_Cmd(b"PRINT \042Real hardware is accessed but no address\042")
      t32api.T32_Cmd(b"PRINT \042for data access has been specified,\042")
      t32api.T32_Cmd(b"PRINT \042Read/WriteMemory will access D:0x1000\042")
      t32api.T32_Cmd(b"PRINT")
      print("") 
      print("")
      print(" Syntax: %s.py [--node <name_or_IP>] [--port <num>] [-address <hexaddr>]" %( PROGNAME))
      print(" Example: %s.py  --node localhost   --port 20000  --address 0x400C000\n" % (PROGNAME))
      print("")
      print(" Hexaddress is used by Read/WriteMemory if real hardware is accessed.")
      print("")
      print("")
      print(' Real hardware is accessed but no address for data access')
      print(' has been specified, Read/WriteMemory will access D:0x1000')
      address = 0x1000
  else:
    t32api.T32_Cmd(b"SYStem.Up")
    t32api.T32_Cmd(b"Data.Assemble P:0x0++0x40 nop")
    t32api.T32_Cmd(b"EVAL CPU()")     #/* for EVAL CPU() size of */
    t32api.T32_EvalGetString(string.encode('latin-1')) #/* string is sufficient   */
    if ( string[:len('TC')] == 'TC'):
      t32api.T32_Cmd(b"Data.Assemble P:0x40 j 0x0")
    else:
      t32api.T32_Cmd(b"Data.Assemble P:0x40 b 0x0")
    t32api.T32_Cmd(b"Register.Set PC P:0x0");
    t32api.T32_Cmd(b"WINPOS 40% 0 60% 40% , , APIWin4")
    t32api.T32_Cmd(b"Data.List")
    t32api.T32_Cmd(b"WINPOS 40% 40% 60% 40% , , APIWin5")
    t32api.T32_Cmd(b"Data.Dump D:0x1000")
    address = 0x1000
  t32api.T32_Cmd(b"WINPOS 40% 75% 60% 25% , , APIWin6")
  t32api.T32_Cmd(b"Break.List")
 
  # select and execute remote API function
  
  while True :
    print("")
    print("")
    print(' Please select an action or exit with \'q\':')
    print("")
    print(' p Ping          rm ReadMemory           d do test.cmm')
    print(' s Step          wm WriteMemory          S Stop script')
    print(' g Go            wp WritePipelined       x TestSequence')
    print(' b Break         rr ReadRegister         j JtagTapAccess')
    print(' c CpuState      wr WriteRegister        T TraceData')
    print(' R Reset         rb ReadBreakpoint       i IntegratorData')
    print(' n Nop           wb WriteBreakpoint')
    print(' f NopFail       rp ReadProgCounter      t TerminateTRACE32')
    print("")
    i = 0
    k = 0
    list1 = list(sel)
    list1 = ''
    sel= ''.join(list1)
    list1='tt'
    while (len(sel) == 0) or (((sel[0] == 'r') or (sel[0] == 'w')) and (len(sel) == 1)) :
      i=i+1
      if i%4<2 :
        sys.stdout.write( '\r>' +sel )
      else :
        sys.stdout.write( '\r>' +sel )
      sys.stdout.flush()
      time.sleep(0.25)
      if k==0:
        sel=getch().decode('latin-1')
        k=k+1
      else:
        list1 = list(sel)
        list1 = sel + getch().decode('latin-1')
        sel= ''.join(list1)
        k=k+1      
    sys.stdout.write( '\r>'+ sel)
    if ((sel[0] == 'q') or (sel[0] == 'Q')) :
      print("")
      print("")
      print(' Program has been terminated by pressing %c' %sel[0])
      break
    retval = T32_OK
    if sel[0]=='p':
      retval = t32api.T32_Ping()             
    elif sel[0]=='s':
      retval = t32api.T32_Step()
    elif sel[0]=='g':
      retval = t32api.T32_Go()
    elif sel[0]=='b': 
      retval = t32api.T32_Break()
    elif sel[0]=='R':
      retval = t32api.T32_ResetCPU()
    elif sel[0]=='n': 
      retval = t32api.T32_Nop() 
    elif sel[0]=='f':
      t32api.T32_NopFail()
    elif sel[0]=='d': 
      retval = t32api.T32_Cmd(b"do test.cmm")
    elif sel[0]=='S': 
      retval = t32api.T32_Stop()
    elif sel[0]=='t': 
      retval = t32api.T32_Terminate(0)
    elif sel[0]=='r':
      if sel[1]=='m' :
        retval = t32api.T32_ReadMemory(address, T32_MEMORY_ACCESS_DATA, pui32val, 8)
        if retval == T32_OK:
          print("")
          print("") 
          print(' Read 8 bytes, started at address D:0x%s data is 0x%s 0x%s:'%(format(address,'0x'),format(pui32val[0],'0x') , format(pui32val[1],'0x')))
      elif sel[1]=='r':
        retval = t32api.T32_ReadRegister(0xfc, 0, pui32val)
        if retval == T32_OK : 
          print("")
          print("")
          sys.stdout.write (' Read registers R2-R7, content is:')
          sys.stdout.flush()
          for i in range (2,8):
            sys.stdout.write( ' 0x%s' %( format(pui32val[i],'0x' )))
            sys.stdout.flush()
      elif sel[1]=='p':
        retval = t32api.T32_ReadPP(pui32val)
        if retval == T32_OK:
          print("")
          print("")
          print(' Read register ProgramCounter, content is 0x%s' %(format( pui32val[0],'0x')))
      elif sel[1]=='b':
        retval = t32api.T32_ReadPP(pui32val)
        if (retval == T32_OK) :
          retval = t32api.T32_ReadBreakpoint(pui32val[0], T32_MEMORY_ACCESS_PROGRAM, pui16val, 32)
        if (retval == T32_OK) :
          print("")
          print("")
          print(' Tested for breakpoints at address P:0x%s -- 0x%s'%(format(pui32val[0],'0x'),format(pui32val[0]+0x1f,'0x')))
          print("")
          noactive=0
          for i in range (0,32):
            if  pui16val[i] !=0:
              print(' Breakpoint is active at address P:0x%x' %(pui32val[0]+i))
              noactive=1
          if noactive==0:
            print(' No active breakpoints.')
      else:
        print("")
        print("")
        print(' Invalid selection!')
    elif sel[0]=='w':
      if sel[1]=='m':
        rwbuffer[0] ^= 0x70404070
        rwbuffer[1] ^= 0x70404070
        retval = t32api.T32_WriteMemory(address, T32_MEMORY_ACCESS_DATA,rwbuffer, 8)
        if (retval == T32_OK):
          print("")
          print("")
          print(' Wrote 8 bytes of new data, started at address D:0x%s ' %(format(address,'0x'))) 
          print(' enter \'rm\' for readout.')
      elif sel[1]=='p':
        wpbuffer[0] ^= 0x70404070
        for i in range  (1,256):
          wpbuffer[i] = wpbuffer[0]
        retval = t32api.T32_WriteMemoryPipe(address, T32_MEMORY_ACCESS_DATA, wpbuffer, 1024)|t32api.T32_WriteMemoryPipe(0, 0, 0, 0)
        if (retval == T32_OK):
          print("")
          print("")
          print(' Wrote 1024 bytes of new data, started at address D:0x%s , see TRACE32 Data.Dump window.' %(format(address,'0x')))
      elif sel[1]=='r':
        m=m+1
        pui32val[0] = m
        for i in range (2,8):
          pui32val[i] = pui32val[0] + i
        retval = t32api.T32_WriteRegister(0xfc, 0, pui32val)
        if (retval == T32_OK):
          print("")
          print("")
          print(' Wrote new data to registers R2-R7, enter \'rr\' for readout.')
      elif sel[1]=='b':
        if ((j == 1) or (pcval == 0xffffffff)) :
          j = 0 #set
          retval = t32api.T32_ReadPP(byref(pcval))
        else:
          j = 1; #delete
        if (retval == T32_OK) :
          retval = t32api.T32_WriteBreakpoint(pcval,T32_MEMORY_ACCESS_PROGRAM,(j<<8)|(1<<4)|(1<<3),8)
          if (retval == T32_OK):
            retval = t32api.T32_WriteBreakpoint(pcval.value+0xf,T32_MEMORY_ACCESS_PROGRAM,(j<<8)|(1<<0),1)
          if (retval == T32_OK):
            if j==1:
              print("")
              print("")
              print(' Deleted breakpoints at adresses P:0x%s--0x%s and P:0x%s'%(format(pcval.value,'0x') ,format(pcval.value + 0x7,'0x'),format(pcval.value + 0xf,'0x')))
              print(' enter \'rb\' for readout.')
            else :
              print("")
              print("")
              print(' Set breakpoints at adresses P:0x%s--0x%s and P:0x%s'%(format(pcval.value,'0x') ,format(pcval.value + 0x7,'0x'),format(pcval.value + 0xf,'0x')))
              print(' enter \'rb\' for readout.')
      else:
        print("")
        print("")
        print(' Invalid selection!')
    elif sel[0]=='c':
      retval = t32api.T32_GetState(byref(systemstate))
      if (retval == T32_OK) :
        states= ["down", "halted", "stopped", "running"]
        systemstate.value=(systemstate.value) & 0x3; #safeguard the little trick
        print("")
        print("")
        print(' Current system state is:', states[systemstate.value])
    elif sel[0]=='x':
      print("")
      print("")
      for i in range(1,11) :
        retval = t32api.T32_Step()
        if (retval == T32_OK) :
          retval = t32api.T32_ReadPP(pui32val)
          if (retval == T32_OK):
            print(' Performed single step, value of ProgramCounter is 0x%s' %(format(pui32val[0],'0x')))
    elif sel[0]=='j':
      buffer = array.array('i', list(range(4)))
      pbuffer = (c_ubyte * 4).from_buffer(buffer) 
      pbuffer[0] =  ord('a')
      pbuffer[1] =  ord('b')
      pbuffer[2] =  ord('c')
      pbuffer[3] =  ord('d')
      retval = t32api.T32_TAPAccessShiftIR(0, 32, pbuffer, pbuffer)
      if (retval == T32_OK):
        print("")
        print("")
        print(' Data received from TAP controller is: 0x%s 0x%s 0x%s 0x%s' %(format(pbuffer[0],'02x'),format(pbuffer[1],'02x'),format(pbuffer[2],'02x'),format(pbuffer[3],'02x')))
    elif sel[0]=='T' or sel[0]=='i':
      states = ["off", "armed", "triggered", "breaked"]
      total = c_int()
      min = c_int()
      max = c_int()
      buf = array.array('i', list(range(80)))
      pbuf = (c_ubyte * 80).from_buffer(buf) 
      for i in range (0,80):
        pbuf[i] = 0xaa
      #Trace|Integrator
      if (sel[0]=='T'):
        retval = t32api.T32_GetTraceState(0, byref(systemstate), byref(total), byref(min), byref(max))
      else:
        retval = t32api.T32_GetTraceState(1, byref(systemstate), byref(total), byref(min), byref(max))
      if (retval == T32_OK) :
        systemstate.value=systemstate.value & 0x3 #/*safeguard the little trick*/
        if (sel[0]=='T'):
          print("")
          print("")
          print(' Trace state is: ',states[systemstate.value], ' total buffer size is %s' %format(total.value,'0d'))
          print(' Trace records range from entry',int(min.value) ,' to', int(max.value),'latest ones are:')
        else:
          print("")
          print("")
          print(' Integrator state is: ',states[systemstate.value], ' total buffer size is %s' %format(total.value,'0d'))
          print(' Trace records range from entry',int(min.value) ,' to', int(max.value),'latest ones are:')
        if (max.value - min.value + 1 > 20):
          num=20
        else:
          num=max.value - min.value + 1
        if ((num > 0) and (systemstate.value == 0)) :
          if sel[0]=='T':
            retval = t32api.T32_ReadTrace(0, max.value - num + 1, num, 0x10, pbuf)#  4 bytes are written to 'buf' for 
          else:
            retval = t32api.T32_ReadTrace(1, max.value - num + 1, num, 0x10, pbuf)
          if (retval == T32_OK) :                                                  #  each mask-bit with value '1'     
            print("")
            print("")
            for i in range (0,num*4,4 ):
              print(' Record %s: Physical program address: 0x%s%s%s%s' %(int(max.value - num + 1 + i/4),format(pbuf[i+3], '02x'),format(pbuf[i+2], '02x'),format(pbuf[i+1], '02x'),format(pbuf[i], '02x')))# trace data is always little endian 
    else:
      print("")
      print("")
      print(' Invalid selection!')
    if (retval != T32_OK):
      print("")
      print("")
      print(' !!!Failed to execute remote command!!!')
    print("") 
    

  if t32api.T32_Exit()!= T32_OK:
    print(' Failed to close the remote connection port on the dos shell application\'s side.')
    sys.exit(EXIT_FAILURE)
  else :
    sys.exit(retval)
if __name__ == "__main__":
   main(sys.argv[1:])