from __future__ import print_function
import os
import sys
import re
import string
import datetime
import time
import subprocess
from os.path import join, getsize

start_time = datetime.datetime.now()
startTime = start_time.strftime("%Y-%m-%d_%H:%M:%S.%f")
currentDir = os.getcwd()

#regular expression for the test result
#./bwcSwOdrxProcDecodePdsch_paraDecodingCat19_02_level1/reports_lingkong/cases_009_step001_029__2018-01-22_15_52_21.txt
#/nfs/site/proj/libdev/lte_ip.work/lingkong/xg766_es1_latest_hw/bwcSwOdrxProcDecodePdsch_paraDecodingCat19_01_level1/reports_lingkong/cases_001_step001_008__2018-01-22_11_42_25.txt
start_str = '_latest_hw'

if sys.platform == 'linux2':
    pattern = re.compile(r"(\w+_latest_\w+)\/(\w+)\/(\w+)\/(\w+.*)__(\d+.*\d)\.txt")

if sys.platform == 'win32':
    pattern = re.compile(r"(\w+_latest_\w+)\\(\w+)\\(\w+)\\(\w+.*)__(\d+.*\d)\.txt")
    print('Running os windows')

TEST_ENTRY  = 8

TIME_FORMAT_m = '%a %b  %d %H:%M:%S %Y'
TIME_FORMAT_t = '%Y-%m-%d_%H_%M_%S'
PASS='\"Result: PASS\"'
FAIL='\"Result: FAIL\"'
RESULT='\"Result: \"'

test_pass_count = {}

users = ['duanchex', 'qiangjux']
file_ext = ['xml', 'log', 'ssl', 'dat', 'js', 'cmd']
done_sub_comp = ['Fefc', 'Cse', 'Csm', 'Ocrx']
excluded = ['result', 'odrx_l1']

fid_res = open('result.txt', 'w')

def remove_path(p):
    os.system('rm -rfv %s' % p)

def check_xgxx_esx_latest_hw(dir_in_lte_ip_work):

    assert os.path.isdir(dir_in_lte_ip_work), 'make sure directory argment should be directory'

    for root, dirs, files in os.walk(dir_in_lte_ip_work, topdown = True):
        for fl in files:
            #file_name contains the full path including filepath and filename
            file_name = os.path.join(root, fl)
            #print('root=', root)
            (p, f) = os.path.split(file_name)    #p is path, f is the filename with extension

            #keep result.txt, and remove the result from other uses
            ###if 'result.txt' in file_name or 'odrx_l1' in file_name:        #exclude result.txt file
            ###    pass
            if re.search(users[0], file_name): #remove folders from other user
                print('Remove files from %s' % users[0])
                remove_path(p)
            elif re.search(users[1], file_name): #remove folders from other user
                print('Remove files from %s' % users[1])
                remove_path(p)
            else:
                pass

            #remove done_sub_comp test to save spaces
            for dsc in done_sub_comp:
                if re.search('bwcSw%s.*xtRiscTb.m' % dsc, file_name): # test are done
                    remove_path(p)

            if re.search('bwc.*txt', file_name): #for test result
                folders = file_name.split('/');
                k = folders[TEST_ENTRY]
                if not test_pass_count.has_key(k):
                    print('Processing', k)

                if re.search('step', file_name): #for merged test
                    k = 'merged %s' % k
                    test_pass_count.setdefault(k, '')
                    #print(file_name)
                    cmd_grep = 'grep %s %s' % (RESULT, file_name)
                    #print(cmd_grep)
                    out, err = subprocess.Popen(cmd_grep, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE).communicate()
                    verdict = out.splitlines()

                    if len(verdict):
                        #print(file_name)
                        if 'PASS' in verdict[0]:
                            test_pass_count[k] = test_pass_count[k] + ' PASS'
                            #remove unneeded files like *.m, *.xml
                            #os.system('rm -rfv %s' % p)
                            os.system('rm -rfv %s/*.xml' % p)
                            os.system('rm -rfv %s/../cases*' % p)
                            os.system('rm -rfv %s/../*_run*' % p)
                        elif 'FAIL' in verdict[0]:
                            test_pass_count[k] = test_pass_count[k] + ' FAIL'
                        else:
                            test_pass_count[k] = 'NOT_RUN'
                    else:
                        pass
                else:
                    test_pass_count.setdefault(k, 0)
                    test_pass_count[k] = test_pass_count[k] + 1


if __name__ == '__main__':
    check_xgxx_esx_latest_hw(currentDir)

    #for key, value in test_pass_count.items():
    #    print('%-100s => %d' % (key, value))
    #find_test_index_and_total()

    folders_to_tar = []

    print('\n            Summary:')
    # sort using key
    for key in sorted(test_pass_count.keys()):
        #print('%-100s => %4d' % (key, test_pass_count[key]))
        value = test_pass_count[key]
        print('%-80s => %10s' % (key, value))
        if 'merged' in key and 'PASS' in value:
            folders_to_tar.append(key.replace('merged ', ''))

    passed_tests = ' '.join(folders_to_tar)
    #print(passed_tests)
    #os.system('tar -cvf passed_tests.tar %s' % passed_tests)
    for t in folders_to_tar:
        #print('Removing %s' % t)
        print('passed %s' % t)
        #os.system('rm -rfv %s' % t)

    ##################################################################################
    ###   basic information of the program
    ##################################################################################

    #show basic information about the execution

    end_time = datetime.datetime.now()
    endTime = end_time.strftime("%Y-%m-%d_%H:%M:%S.%f")

    #second and microsecond
    duration_s  = (end_time - start_time).seconds
    duration_us = (end_time - start_time).microseconds

    #float number with seconds and microseconds
    duration = duration_s + duration_us / 1000000.0

    print("Run  \033[07;32m%s\033[0m" % (__file__))
    print("From \033[07;32m%s\033[0m" % (currentDir))
    print("Start at:  \033[07;32m%s\033[0m" % (startTime))
    print("End at:    \033[07;32m%s\033[0m" % (endTime))
    print("Duration:     \033[07;32m%s s\033[0m" % (duration_s))
    print("Duration_us:  \033[07;32m%s ms\033[0m" % (duration_us))
    print("Duration:  \033[07;32m%s Seconds\033[0m" % (duration))
