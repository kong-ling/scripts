import os
import sys
import re
import string
import datetime
from os.path import join, getsize

currentDir = os.getcwd()
currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

print "Run  \033[07;32m%s\033[0m" % (__file__)
print "From \033[07;32m%s\033[0m" % (currentDir)
print "From \033[07;32m%s\033[0m" % (os.path.dirname(__file__))
print "From \033[07;32m%s\033[0m" % (os.path.abspath(__file__))
print "at:  \033[07;32m%s\033[0m" % (currentTime)


#find the result files
result_file_list = os.popen('find bwcSwIrxProcCopyExt* -name "*2017-12-29*.txt" | xargs ls -rt | xargs grep "Result: "')
print('****************************')
print result_file_list
print('****************************')

#1  bwcSwIrxProcCopyExtMemToIrx_para_01_level1/reports_lingkong/cases_001_step001_003__2017-12-29_04_46_19.txt:Result: PASS
#2  bwcSwIrxProcCopyExtMemToIrx_para_02_level1/reports_lingkong/cases_001_step001_003__2017-12-29_04_46_25.txt:Result: PASS
#pattern = re.compile(r'(\w+)\/(\w+)\/(\w+)__(\d+-\d+-\d+_\d+_\d+_\d+)\.txt:Result:\ (\w+)')
#pattern = re.compile(r'(\w+)\/(\w+)\/(.+\.txt):Result:\ (\w+)')
compiled_pattern = re.compile(r'reports_lingkong')

for line in result_file_list.readlines():
    print(line)
    line = line.strip('\r\n')
    print(line)

    match = compiled_pattern.match(line)
    print('****************************')
    print match
    print('****************************')

    if match:
        print match.groups()
