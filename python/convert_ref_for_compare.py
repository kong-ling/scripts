from __future__ import print_function
import os
import sys
import re
import string
import datetime
from os.path import join, getsize

start_time = datetime.datetime.now()
startTime = start_time.strftime("%Y-%m-%d_%H:%M:%S.%f")
currentDir = os.getcwd()

def check_xgxx_esx_latest_hw(dir_in_lte_ip_work):
    assert os.path.isdir(dir_in_lte_ip_work), 'make sure directory argment should be directory'

    #define list and dicts for test result
    results = []
    test_entries = []
    test_dict_pass = {}
    test_dict_fail = {}
    test_dict_gen  = {}
    #test_dict = {'bwcSwSystemRx_paraTransMode3_01_level1':{'PASS':[], 'FAIL':[], 'GEN':[]}}
    test_dict = {}

    for root, dirs, files in os.walk(dir_in_lte_ip_work, topdown = True):
        for fl in files:
            file_name = os.path.join(root, fl)
            if ('irx_cam' in file_name or 'irx_rsm' in file_name or 'irx_rsmn' in file_name) and 'ref' in file_name:
                print(file_name)


    return(results, test_dict, test_entries)

fid = open('result.txt', 'w')


if __name__ == '__main__':
    (results, test_dict, test_entries) = check_xgxx_esx_latest_hw(currentDir)

    #for k, v in test_dict['PASS'].items():
    #    #print(k, '-\033[07;31mFAIL\033[0m>', len(v), v)
    #    print(('%s -> %s') % (k, '-\033[07;32mPASS [%d]\033[0m>' % len(v)), v)

    #for k, v in test_dict['FAIL'].items():
    #    #print(k, '-\033[07;31mFAIL\033[0m>', len(v), v)
    #    print(('%s -> %s') % (k, '-\033[07;31mFAIL [%d]\033[0m>' % len(v)), v)

    fid.write('test_dict = \n{\n')
    for k, v in test_dict.items():
        #print(k, '-\033[07;31mFAIL\033[0m>', len(v), v)
        print(('%s %s') % (k, '\033[07;31m->[%d]\033[0m' % len(v)), v)
        fid.write('    \'%s\' : %s,\n' % (k, v))
    #write the end of the file
    fid.write('}')
    fid.close()


##################################################################################
###   basic information of the program
##################################################################################

#show basic information about the execution
print("Run  \033[07;32m%s\033[0m" % (__file__))
print("From \033[07;32m%s\033[0m" % (currentDir))

end_time = datetime.datetime.now()
endTime = end_time.strftime("%Y-%m-%d_%H:%M:%S.%f")

#second and microsecond
duration_s  = (end_time - start_time).seconds
duration_ms = (end_time - start_time).microseconds

#float number with seconds and microseconds
duration = duration_s + duration_ms / 1000000.0

print("Run  \033[07;32m%s\033[0m" % (__file__))
print("From \033[07;32m%s\033[0m" % (currentDir))
print("Start at:  \033[07;32m%s\033[0m" % (startTime))
print("End at:    \033[07;32m%s\033[0m" % (endTime))
print("Duration:     \033[07;32m%s s\033[0m" % (duration_s))
print("Duration_ms:  \033[07;32m%s ms\033[0m" % (duration_ms))
print("Duration:  \033[07;32m%s Seconds\033[0m" % (duration))
