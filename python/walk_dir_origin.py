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

#regular expression for the test result
#./bwcSwOdrxProcDecodePdsch_paraDecodingCat19_02_level1/reports_lingkong/cases_009_step001_029__2018-01-22_15_52_21.txt
#/nfs/site/proj/libdev/lte_ip.work/lingkong/xg766_es1_latest_hw/bwcSwOdrxProcDecodePdsch_paraDecodingCat19_01_level1/reports_lingkong/cases_001_step001_008__2018-01-22_11_42_25.txt
#start_str = '_latest_hw/'
start_str = '_latest_hw'

if sys.platform == 'linux2':
    pattern = re.compile(r"(\w+_latest_\w+)\/(\w+)\/(\w+)\/(\w+.*)__(\d+.*\d)\.txt")

if sys.platform == 'win32':
    pattern = re.compile(r"(\w+_latest_\w+)\\(\w+)\\(\w+)\\(\w+.*)__(\d+.*\d)\.txt")
    print('Running os windows')

TEST_DIR    = 1
TEST_ENTRY  = 2
TEST_REPORT = 3
TEST_CASE   = 4
TEST_TIME   = 5

#dictionary for the test result
# {'testentry':(pass_list, fail_list, gen_list)}
#test_entries = []
#test_dict_pass = {'testentry':[[], [], []]}
#test_dict_pass = {}
#test_dict_fail = {}
#test_dict_gen  = {}
#results = []

def check_xgxx_esx_latest_hw(dir_in_lte_ip_work):
    assert os.path.isdir(dir_in_lte_ip_work), 'make sure directory argment should be directory'

    #define list and dicts for test result
    results = []
    test_entries = []
    test_dict_pass = {}
    test_dict_fail = {}
    test_dict_gen  = {}
    test_dict = {'PASS':[], 'FAIL':[], 'GEN':[]}

    for root, dirs, files in os.walk(dir_in_lte_ip_work, topdown = True):
        for fl in files:
            file_name = os.path.join(root, fl)
            #print(file_name)

            #res = pattern.match(file_name, file_name.index(start_str) + len(start_str))
            # search is better than match, since match start from the beginning by default
            res = pattern.search(file_name)

            #only ODRX will be analyzed
            #if res and ('SwOdrx' in file_name):
            if res:
                #print(file_name)

                ## for debug purpose
                #res = pattern.match(file_name, file_name.index(start_str) + len(start_str))
                res = pattern.search(file_name)
                test_dir    = res.group(TEST_DIR)
                test_entry  = res.group(TEST_ENTRY)
                test_report = res.group(TEST_REPORT)
                test_case   = res.group(TEST_CASE)
                test_time   = res.group(TEST_TIME)
                #print(res.groups())
                test_result = list(res.groups())

                # open the result for to check the test resut: "Result: PASS", or "Result: FAIL"
                fid = open(file_name, 'r')
                # TODO: optimize by reading just the tail of the file

                #if the variable is not defined, define the dict dynamically
                if test_entry not in test_dict_pass.keys():
                    #print('\033[07;32mdefine test_dict_pass\033[0m')
                    test_dict_pass[test_entry] = [] #define dict

                if test_entry not in test_dict_fail.keys():
                    #print('\033[07;31mdefine test_dict_fail\033[0m')
                    test_dict_fail[test_entry] = [] #define dict

                testcase = '__'.join([test_case, test_time])
                #print(testcase)
                if 'Result: PASS' in fid.read():
                    verdict = 'PASS' #green
                    verdict_color = '\033[07;32mPASS\033[0m' #green
                    #print(verdict_color)
                    test_dict_pass[test_entry].append(testcase)
                else:
                    verdict = 'FAIL' #red
                    verdict_color = '\033[07;31mFAIL\033[0m' #red
                    #print(verdict_color)
                    test_dict_fail[test_entry].append(testcase)

                #add verdict to the list
                test_result.append(verdict)
                #print(test_result)

                fid.close()
                results.append(file_name)

                if test_entry in test_entries:
                    pass
                else:
                    test_entries.append(test_entry)
            else:
                #print('.', end='')
                pass


    return(results, test_dict, test_entries, test_dict_pass, test_dict_fail, test_dict_gen)


if __name__ == '__main__':
    (results, test_dict, test_entries, test_dict_pass, test_dict_fail, test_dict_gen) = check_xgxx_esx_latest_hw(currentDir)
    #check_xgxx_esx_latest_hw('.')
    #for test in test_entries:
    #    print(test)
    for res in results:
        #print(res)
        pass
    #for k, v in test_dict_pass.items():
    #    #print(k, '-\033[07;32mPASS\033[0m>', len(v), v)
    #    #print(('%s -> %s[%d]') % (k, '-\033[07;32mPASS\033[0m>', len(v)), v)
    #    #print(('%s -> %s') % (k, '-\033[07;32mPASS [%d]\033[0m>' % len(v)), v)
    #    print(('%s -> %s') % (k, '-\033[07;32mPASS [%d]\033[0m>' % len(v)))
    #for k in sorted(test_dict_pass.keys()):
    #    #print(k, '-\033[07;32mPASS\033[0m>', len(v), v)
    #    #print(('%s -> %s[%d]') % (k, '-\033[07;32mPASS\033[0m>', len(v)), v)
    #    #print(('%s -> %s') % (k, '-\033[07;32mPASS [%d]\033[0m>' % len(v)), v)
    #    #print(('%s -> %s') % (k, '-\033[07;32mPASS [%d]\033[0m>' % len(test_dict_pass.keys())))
    #    print(k)
    for k, v in test_dict_fail.items():
        #print(k, '-\033[07;31mFAIL\033[0m>', len(v), v)
        print(('%s -> %s') % (k, '-\033[07;31mFAIL [%d]\033[0m>' % len(v)), v)

    for k, v in test_dict.items():
        #print(k, '-\033[07;31mFAIL\033[0m>', len(v), v)
        print(('%s -> %s') % (k, '-\033[07;31m test_dict [%d]\033[0m>' % len(v)), v)
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
