import time
import serial

class relay:
    def __init__(self, com="COM4"):
        self.relay = serial.Serial(com, 9600)

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

if __name__ == '__main__':
    r = relay()
    r.off()
    time.sleep(4)
    r.on()
    r.close()
