import os
import datetime
import serial
import threading
import signal
import traceback


clear_error       = '*CLS'
read_error        = 'system:error?'
meas_volt         = 'MEAS:VOLT?'
meas_curr         = 'MEAS:CURR?'
output_off        = 'output off'
output_on         = 'output on'
output_off_status = 'OUTPUT OFF'
output_on_status  = 'OUTPUT ON'
output_stat       = 'output:state?'
idn               = '*IDN?'
check_limit       = 'current?'
#check_limit       = 'apply?\r\n'

is_exit = False

serial_lock = threading.RLock() #Create a lock object

def handler(signum):
    is_exit = True
    print("Receive a signal %d, is_exit = %d" % (signum, is_exit))


class Serial_Control_Port:
    "The serail port to control power supply"

    def __init__(self, portName='com5'):
        #serial port
        self.ser = serial.Serial(port=portName, baudrate=115200, stopbits=serial.STOPBITS_TWO, dsrdtr=True)
        self.ser.timeout = 0.5

    def ReceiveResult(self):
        serial_lock.acquire()
        result = self.ser.readline()
        serial_lock.release()
        return result

    def SendCMD(self, cmd):
        serial_lock.acquire()
        self.ser.flushInput()
        cmd = '*WAI; %s; *WAI\r\n' % cmd
        self.ser.write(bytes(cmd, 'utf-8'))
        serial_lock.release()

    def SendCMD_and_ReceiveResult(self, cmd):
        serial_lock.acquire()
        #print(cmd)
        cmd = '*WAI; %s; *WAI\r\n' % cmd
        #cmd = '%s\r\n' % cmd
        #self.ser.write('*WAI;%s;*WAI\r\n' % cmd)
        try:
            self.ser.flushInput()
            self.ser.write(bytes(cmd, 'utf-8'))
        except TypeError as e:
            print(cmd)
            print('SendCMD_and_ReceiveResult:', e)
            traceback.print_exc()
            #raw_input('Press any key')

        output = self.ser.readline()
        #self.ser.write('*OPC?') #Operation Complete?
        serial_lock.release()
        return output

    def ReadError(self):
        #read error
        return self.SendCMD_and_ReceiveResult(read_error)

    def SelectOutput(self, output):
        #output selection,
        self.SendCMD('INST:NSEL %d' % output)

    def ReadIDN(self):
        #read IDN
        self.ReceiveResult()
        return self.SendCMD_and_ReceiveResult(idn)

    def ReadOutputStatus(self):
        #read output status
        #self.ReceiveResult()
        return self.SendCMD_and_ReceiveResult(output_stat)

    def ReadLimit(self):
        #read output status
        return self.SendCMD_and_ReceiveResult(check_limit)

    def ReadVoltage(self, limit):
        #read Voltage
        if limit == True:
            volt = self.SendCMD_and_ReceiveResult('voltage?')
        else:
            volt = self.SendCMD_and_ReceiveResult('meas:volt?')
        #print("volt=%s" % volt)
        #print("volt.rstrip=%s" % volt.rstrip())

        if 'E' in volt:
            try:
                f_volt = float(volt.rstrip())
            except Exception as e:
                print('ReadVoltage:', e)

            #print("f_volt=%s" % f_volt)
            return f_volt

    def ReadCurrent(self, limit):
        #read Current
        if limit == True:
            curr = self.SendCMD_and_ReceiveResult('current?')
        else:
            curr = self.SendCMD_and_ReceiveResult('meas:curr?')
        #print("curr=%s" % curr)
        #print("curr.rstrip=%s" % curr.rstrip())
        if 'E' in curr:
            try:
                f_curr = float(curr.rstrip())
            except Exception as e:
                print('ReadCurrent:', e)

            #print("f_curr=%s" % f_curr)
            return f_curr

if __name__ == '__main__':

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    com = Serial_Control_Port('com1')

    print('Program start %s' % datetime.datetime.now())
    #print("%s" % list_serial_ports()


