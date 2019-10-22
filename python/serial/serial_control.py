# -*- coding: UTF-8 -*-

import os
import sys
import time
import datetime
import serial
import signal
import traceback
import threading
import binascii

tests = ['acc_ddr_1', 'acc_ddr_2', 'acc_ddr_3']

class Ser:
    def __init__(self, portName='com5'):
        #serial port
        #self.ser = serial.Serial(port=portName, baudrate=115200, stopbits=serial.STOPBITS_TWO, dsrdtr=True)

        #this is very critical that the COM port is using 1-stop bit, instead of 2-stop bits
        self.ser = serial.Serial(port=portName, baudrate=115200, stopbits=serial.STOPBITS_ONE)
        self.ser.timeout = 0.5
        self.ser.name = portName
        self.lines = 0;

    def printIdle(self):
        while True:
            pass
            #print('*')
            time.sleep(10)

    def serialWrite(self, str):
        self.ser.write(str)

    def run_tests(self, testcases):
        for t in testcases:
            self.ser.write('cv upc %s\n' % t)

    def serialRead(self):
        while True:
            #print('read')
            self.lines = self.lines + 1
            line = self.ser.readline()
            print(line)
            if '[U-BOOT]' in line:
                self.run_tests(tests)
            else:
                pass

def handler(signum, frame):
    print('Signal handler call with signal', signum)
    sys.exit(0)

if __name__ == '__main__':

    #print(sample)
    #for ch in sample:
    #    print(ord(ch)),

    try:
        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)

        ser = Ser('com5')
        #ser.serialWrite('cv tpcu icc')

        serRead = threading.Thread(target = ser.serialRead)
        #serWrite = threading.Thread(target = ser.serialWrite)
        idlePrint = threading.Thread(target = ser.printIdle)

        serRead.setDaemon(True)
        serRead.start()
        #serWrite.setDaemon(True)
        #serWrite.start()
        idlePrint.setDaemon(True)
        idlePrint.start()

        while True:
            pass
    except Exception, exc:
        print exc

