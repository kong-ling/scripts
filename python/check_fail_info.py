import os
import sys
import re


#the result will be wrint to rsync_cmd_file
fail_case_log = open('fail_case_log.txt', 'w')

#list the specified directories
odrx_log_files = os.popen('find bwcSwOdrxProc* -name "*.txt" | xargs ls -rt | xargs grep "Result: F"')

RESULT     = 0
TEST_DIR   = 1
REPORT_DIR = 2
LOG_NAME   = 3
VERDICT    = 4

#process the matched log_files
for log_file in odrx_log_files.readlines():
    log_file = log_file.strip('\r\n')
    print(log_file)

    match = []

    # bwcSwOdrxProcDecodePdsch_paraAllChan_01_level1/reports_lingkong/case_013__2018-01-20_08_38_21.txt:Result: FAIL
    pattern = re.compile(r'(\w+)\/(\w+)\/(\w+.*)\.txt:Result:\ (\w+)')
    match = pattern.match(log_file)
    if match:
        #print match.groups()
        result     = match.group(RESULT)
        test_dir   = match.group(TEST_DIR)
        report_dir = match.group(REPORT_DIR)
        log_name   = match.group(LOG_NAME)
        verdict    = match.group(VERDICT)

        #combine the run log file name
        fail_log = '/'.join([test_dir, report_dir + '_run', log_name])
        #print(fail_log)

        #write the log file's name to file
        fail_case_log.write('%s\n' % fail_log)

        #readback the content from the file's tail
        fail_info = os.popen('tail -n 50 %s' % fail_log)

        fail_detail = fail_info.read()
        #print the fail info into file
        fail_case_log.write(fail_detail)
        #print(fail_detail)
        fail_case_log.write('====================================================================\n')

fail_case_log.close()

#inform the server at remote site, so that the sync can be done automatically or 
#periodically
