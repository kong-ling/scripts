import os
import sys
import re
import string
import datetime
import time
import exceptions
from os.path import join, getsize

start_time = datetime.datetime.now()
startTime = start_time.strftime("%Y-%m-%d_%H:%M:%S.%f")

currentDir = os.getcwd()
currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

class TypeError(Exception):
    pass

result_file = './bwcSwSystemRx_paraTransMode2CpExtended_01_level1/reports_lingkong/case_010__2018-02-02_09_10_31.txt'

pattern = re.compile(r'(\d{4}-\d{2}-\d{2}_\d{2}_\d{2}_\d{2})')
#pattern = re.compile(r'2017-11-30_07_10_04')
#pattern = re.compile(r'2018')
match = pattern.search(result_file)

print result_file
print pattern

print match.groups()

if __name__ == '__main__':

    print "Run  \033[07;32m%s\033[0m" % (__file__)

    if (len(os.sys.argv) < 1):
        raise TypeError()
    else:
        print "os.sys.argv[0]: %s" % os.sys.argv[0]

    f = os.sys.argv[0]
    mtime = time.ctime(os.path.getmtime(result_file))
    ctime = time.ctime(os.path.getctime(result_file))


print "at:  \033[07;32m%s\033[0m" % (currentTime)
print "Last modified: %s, last created time:%s" % (mtime, ctime)
time.sleep(2)
#show basic information about the execution
end_time = datetime.datetime.now()
endTime = end_time.strftime("%Y-%m-%d_%H:%M:%S.%f")

#second and microsecond
duration_s  = (end_time - start_time).seconds
duration_ms = (end_time - start_time).microseconds
print("Duration:  \033[07;32m%s Seconds\033[0m" % (duration_ms))

#float number with seconds and microseconds
duration = duration_s + duration_ms / 1000.0

print("Run  \033[07;32m%s\033[0m" % (__file__))
print("From \033[07;32m%s\033[0m" % (currentDir))
print("Start at:  \033[07;32m%s\033[0m" % (startTime))
print("End at:    \033[07;32m%s\033[0m" % (endTime))
print("Duration:  \033[07;32m%s Seconds\033[0m" % (duration))
