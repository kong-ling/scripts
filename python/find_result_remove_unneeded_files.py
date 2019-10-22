from __future__ import print_function
import os
import sys
import re
import string
import datetime
import time
import subprocess
import glob
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

TEST_ENTRY  = 1

TIME_FORMAT_m = '%a %b  %d %H:%M:%S %Y'
TIME_FORMAT_t = '%Y-%m-%d_%H_%M_%S'
PASS='\"Result: PASS\"'
FAIL='\"Result: FAIL\"'
RESULT='\"Result: \"'

test_pass_count = {}

fid_res = open('result.txt', 'w')
def basic_info():
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

def remove_path(p):
    os.system('rm -rfv %s' % p)

def grep_result(f, res):
    '''search 'Result: ' for test verdict
       f:   file to search
       res: verdict for 'Result: PASS' or 'Result: FAIL'
    '''
    cmd_grep = 'grep %s %s' % (res, f)
    #print(cmd_grep)
    out, err = subprocess.Popen(cmd_grep, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE).communicate()
    verdict = out.splitlines()
    if len(verdict):
        #return verdict[0].replace('Result: ', '') #remove 'Result
        return verdict[0]
    else:
        return 'NA'

def tail_of_file(f, lines):
    '''search 'Result: ' for test verdict
       f:   file to search
       lines: the lines to output
    '''
    cmd_grep = 'tail -n %d %s' % (lines, f)
    print("[7;31m[47m%s [m " % cmd_grep)
    out, err = subprocess.Popen(cmd_grep, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE).communicate()
    verdict = out.splitlines()
    #print(verdict)
    print('\n'.join(verdict))

def get_test_iterations(f):
    '''search the test's iterations
       f:   file to search
    '''
    cmd_grep = 'tac %s | grep -m 1 "Start iteration"' % f
    print("[7;31m[47m%s [m " % cmd_grep)
    out, err = subprocess.Popen(cmd_grep, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE).communicate()
    verdict = out.splitlines()
    #print(verdict)
    print('\n'.join(verdict))

def remove_txt_and_append_run(log):
    run_log = log.replace(r'.txt', '') #remove .txt
    run_log = run_log.replace(r'/case', r'_run/case') #add _run to report_lingkong to point to the run log file
    return run_log


def check_xgxx_esx_latest_hw(dir_in_lte_ip_work):
    assert os.path.isdir(dir_in_lte_ip_work), 'make sure directory argment should be directory'
    for root, dirs, files in os.walk(dir_in_lte_ip_work, topdown = True):
        for fl in files:
            #file_name contains the full path including filepath and filename
            file_name = os.path.join(root, fl)
            (p, f) = os.path.split(file_name)    #p is path, f is the filename with extension

            #if re.search(r'./bwc.*txt', file_name): #for test result
            if re.search(r'.txt', file_name): #for test result
                folders = file_name.split('/');
                k = folders[TEST_ENTRY] #find test name
                #print(k)
                test_pass_count.setdefault(file_name, '')
                test_pass_count[file_name] = grep_result(file_name, RESULT)
                get_test_iterations(file_name)

                #####################run_log = remove_txt_and_append_run(file_name)
                #####################print('%s => %s' % (run_log, test_pass_count[file_name]))
                #print(p)
                #print('Processing %s => %s' % (file_name.replace(r'/case', r'_run/case'), test_pass_count[file_name]))
                #./bwcSwOdrxProcDecodePdsch_paraTdd_LBRM_01_level1/reports_lingkong/case_300__2018-11-01_22_10_58.txt => ['Result: PASS']
                #os.system('cp --parents -rfv %s folder_for_txt' % file_name)
            else:
                pass

    return test_pass_count


if __name__ == '__main__':
    #check_xgxx_esx_latest_hw(currentDir)
    folders = sys.argv[1]
    lines = sys.argv[2]
    if folders:
        print(folders)
        for element in glob.glob(folders):
            print(element)
            check_xgxx_esx_latest_hw(element)
    else:
        check_xgxx_esx_latest_hw('.')

    if lines:
        lines_to_output = int(lines)
    else:
        lines_to_output = 5

    folders_to_tar = []

    print('\nSummary:')
    # sort using key
    for key in sorted(test_pass_count.keys()):
        value = test_pass_count[key]
        print('%-80s --> %10s' % (key, value))

    for key in sorted(test_pass_count.keys()):
        value = test_pass_count[key]

        #the case failed
        if 'FAIL' in value:
            #print(key)
            #cmd = 'tail -n 20 %s' % remove_txt_and_append_run(key)
            #print(cmd)
            #os.system(cmd)
            tail_of_file(remove_txt_and_append_run(key), lines_to_output)


    basic_info()
