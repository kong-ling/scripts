import time
import serial
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Power control using CH340')
parser.add_argument('-p', '--port', dest='port', required=True, help='the serial port\'s full name for the switch')
parser.add_argument('-d', '--duration', dest='duration', default=1, required=False, help='duration for off')
parser.add_argument('-r', '--repeats', dest='repeats', default=1, required=False, help='repeat times for on/off')
args = parser.parse_args()

class relay:
    def __init__(self, com="COM4"):
        self.relay = serial.Serial(com, 9600)
        self.com = com
        print('Using %s' % self.com)

    def on(self):
        self.relay.write([0x11])
        time.sleep(0.1)
        n=self.relay.inWaiting()
        return ord(self.relay.read(n))

    def off(self):
        self.relay.write([0x21])
        time.sleep(0.1)
        n=self.relay.inWaiting()
        return ord(self.relay.read(n))

    def status(self):
        self.relay.write([0x31])
        time.sleep(0.1)
        n=self.relay.inWaiting()
        return ord(self.relay.read(n))

    def close(self):
        self.relay.close()
        print('Closing %s' % self.com)

if __name__ == '__main__':
    port = args.port.upper()
    duration = float(args.duration)
    repeats = int(args.repeats)

    #with open('config', 'r') as f:
    #    for line in f:
    #        line = line.strip()
    #        if 'port=' in line:
    #            #print(line.index('='))
    #            port=line[line.index('=') + 1:]
    #            #print(port)
    #        elif 'time=' in line:
    #            #print(line.index('='))
    #            duration=int(line[line.index('=') + 1:], 10)
    #            #print(duration)
    print('port=%s, duration=%2.2f, repeats=%d' % (port, duration, repeats))
    print(port)
    r = relay(port.upper())
    #r = relay('COM6')
    for i in range(repeats):
        r.off()
        print(r.status())
        time.sleep(duration)
        r.on()
        print(r.status())
    r.close()
