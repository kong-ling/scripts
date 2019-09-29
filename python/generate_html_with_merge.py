#!/usr/bin/env python

# ------------------------------------------------------------------------------
#                             Intel Confidential
# ------------------------------------------------------------------------------
#    Copyright (C) 2018 Intel Corporation
#    Copyright (C) 2015 - 2017 Intel Deutschland GmbH
# ------------------------------------------------------------------------------

#####################################################################
## generate report in html format
## testlist should be provided, 
## otherwise, $(workAlgorithms/testlist.txt will be used
#####################################################################

import re
import os
import string
import datetime
import sys

#import user defined module
import analyze_path
import html_defs as defs

currentDir  = os.getcwd()
currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

## parse /p/libdev/lte_ip.work2/lingkong/xg732_es1_latest_hw
result_path = currentDir.split('/')
print result_path

#usage
if len(sys.argv) < 2 :
    print 'Usage:'
    print 'python %s testlist' % currentDir
    print 'if testlist is missing, the default will be usd\n'
    testlist = '%s/testlist.txt' % os.getenv('workAlgorithms') #the default testlist
else:
    testlist = sys.argv[1] #the second is testlist

HTML_BODY = '''
    <body>
        <h3><a href="%s">Results</a></h3>
        <pre>CurDir:   %s</pre>
        <pre>testlist: %s</pre>
        <pre>Branch:   latest</pre>
        <pre>Target:   HW level 1</pre>
        <pre>Run Time: %s</pre>
        <pre>Testlist: %s</pre>
        <pre>-</pre>
''' % (currentDir, currentDir, result_path[-1], currentTime, testlist)


#print cli arguments
for i in range(len(sys.argv)):
    print 'argv[%s] = %s' % (i, sys.argv[i])


print "At %s Executing %s\nFrom path:%5s\n" % (currentTime, __file__, currentDir)

########################################################################
#
#  get testEntry and test from analyze_path
#
########################################################################

tests = analyze_path.get_test_info_from_testlist_split(testlist)
items = tests.items()

#########################################################################
##  generate the html for reporting
#########################################################################
html_file = open('test_%s.html' % currentTime, 'w')
html_file.write('<!DOCTYPE html>')
html_file.write(defs.HTML_HEADER)
html_file.write(HTML_BODY)
html_file.write(defs.SEARCH_INPUT)
html_file.write(defs.TABLE_HEAD)

TEST_INDEX          = 0
TEST_ENTRY_NAME     = 1
TEST_REPORT_FOLDER  = 2
TEST_REPORT_NAME    = 3
TEST_CASE           = 3
TEST_NUMBER         = 4
TEST_TIME           = 5
TEST_VERDICT        = 4

indent_4  = '    '
indent_8  = '%s%s' % (indent_4, indent_4)
indent_12 = '%s%s' % (indent_8, indent_4)
indent_16 = '%s%s' % (indent_8, indent_8)


file_list = os.popen('find . -name "*.txt" | xargs ls | xargs grep Result')
#print file_list.read()
info = file_list.readlines()
for line in info:
    line = line.strip('\r\n')

    #just for debugging
    print line

    #./bwcSwSystemRx_paraPdcchOnly_01_level1/reports_lingkong/case_001__2017-05-31_07_30_05.txt:Result: PASS
    pattern = re.compile(r"(\w+)\/(\w+)\/(case.+)\.txt:Result:\ (\w+)")

    match = pattern.search(line)
    #print match
    if match:
        test_index         = match.group(TEST_INDEX)
        test_entry         = match.group(TEST_ENTRY_NAME)
        test_report_folder = match.group(TEST_REPORT_FOLDER)
        #test_report_name   = match.group(TEST_CASE) + '_' + match.group(TEST_NUMBER)+ '__' + match.group(TEST_TIME)
        test_report_name   = match.group(TEST_REPORT_NAME)
        test_verdict       = match.group(TEST_VERDICT)

        testcase    = test_report_name.split('__')
        tester_name = test_report_folder.split('_')

        html_file.write('%s<tr>\n' % indent_12)

        try:
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_index, tests[test_entry][1]))
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_entry, test_entry))
            html_file.write('%s<td style="width:90px;"> %s</td>\n' % (indent_16, tests[test_entry][5]))
        except:
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_index, '?'))
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_entry, test_entry))
            html_file.write('%s<td style="width:90px;"> %s</td>\n' % (indent_16, 'MissingIdx'))

        html_file.write('%s<td style="width:90px;"><a href="./%s/%s/%s.txt">%s</a></td>\n' % (indent_16, test_entry, test_report_folder, test_report_name, testcase[0]))
        html_file.write('%s<td style="width:90px;">%s</td>\n' % (indent_16, testcase[1]))
        html_file.write('%s<td style="width:90px;"><a href="./%s/%s/%s">xtRiscTb.m</a></td>\n' % (indent_16, test_entry, testcase[0], 'xtRiscTb.m'))

        if test_verdict == 'PASS':
            html_file.write('%s<td><span class="pass">%s</span></td>\n' % (indent_16, test_verdict))
        else:
            html_file.write('%s<td><span class="fail">%s</span></td>\n' % (indent_16, test_verdict))

        html_file.write('%s<td style="text-align:center;">%s</td>\n' % (indent_16, tester_name[1]))

        html_file.write('%s<td style="width:90px;"><a href="./%s/%s_run/%s">run_log</a></td>\n' % (indent_16, test_entry, test_report_folder, test_report_name))
        html_file.write('%s</tr>\n' % indent_12)

    else:
        print 'no match found...'
html_file.write(defs.TABLE_TAIL)

html_file.write(defs.FUNC_FOR_SEARCH)

html_file.write(defs.HTML_TAIL)
html_file.close()
