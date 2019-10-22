import os
import sys
import datetime

while True:
    for i in range(13):
        print datetime.datetime.now()
        print i
        print os.popen("ping 127.0.0.1").read()
