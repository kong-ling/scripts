import os
import sys
import re
import string

currentDir = os.getcwd()

print "Executing %s\nFrom path:%5s\n" % (__file__, currentDir)

#log file for run
file_list_for_run      = os.popen('find . -type f -name "*.txt" | xargs ls | xargs grep Result')
file_list_for_gen      = os.popen('find . -type f -name "case*" | xargs grep __gen')
file_list_for_xtRistTb = os.popen('find . -type f -name "xtRiscTb.m"')


for element in file_list_for_run:
    print 'file_list_for_run: ', element

for element in file_list_for_gen:
    print 'file_list_for_gen: ', element

for element in file_list_for_xtRistTb:
    print 'file_list_for_xtRistTb: ', element

#def get_test_info_from_testlist(tests = '/home/git.view/lingkong/ibis_development/lte_phy/lte_fw/tools/ltephyhostmatlab/utils/testlist.txt'):
def get_test_info_from_testlist(tests = '/home/git.view/lingkong/ibis_se_phy_mainline/lte_phy/lte_se/tools/ltephyhostmatlab/utils/testlist.txt'):
    #testlist is the output of lteDispHwTests
    fh = open(tests, 'r')

    Idx       = 1
    Subcomp   = 2
    TestEntry = 3
    TestEntry_slice = 4
    Levels    = 5
    TestCases = 6
#| 001 |    FEFC | bwcSwFefcProcFft_para:01                                            |  1     | merged [1:1:11]                                                                                                                                                                                                             | 
    #pattern = re.compile(r'^\|\s(\d+)\s\|\s+(\w+)\s+\|\s+(\w+):(\w+)\s*\|\s+(\d \d)\s+\|')
    #pattern = re.compile(r'^\|\s(\d+)\s\|\s+(\w+)\s+\|\s+(\w+):(\w+)\s*\|\s+(\w+|\w \w+)\s+\|\s+\[\d+:\d+:\d+\]\s+')
    #pattern = re.compile(r'^\|\s(\d+)\s\|\s+(\w+)\s+\|\s+(\w+):(\w+)\s*\|\s+(\w+|\w \w+)\s+\|\s+((merged){0,1}\s+\[\d+:\d+:\d+\])')
    pattern = re.compile(r'^\|\s(\d+)\s\|\s+(\w+)\s+\|\s+(\w+):(\w+)\s*\|\s+(\w+|\w \w+)\s+\|\s*(\w*\s*\[\d+:\d+:\d+\])')

    loop = 0

    dict_test = {}
    for each_line in fh:
        loop = loop + 1

        try:
            #if (loop >= 337) and (loop <= 344):
            #print loop
            each_line = each_line.strip('\r\n')
            match = pattern.match(each_line)
            print match.groups()
            folder_for_test= '%s/%s_%s' % (match.group(Idx), match.group(TestEntry), match.group(TestEntry_slice))
            print folder_for_test
            #print each_line

            #add to dict
            #key = '%s_%s' % (match.group(TestEntry), match.group(TestEntry_slice))
            key = match.group(Idx)
            dict_test[key] = match.groups()
        except:
            print loop
            print 'Something wrong happened...'

    fh.close()
    return dict_test

#get_test_info_from_testlist()
tests = get_test_info_from_testlist()

items = tests.items()
items.sort()
for (k,v) in items:
    print '[%s] => ' % k, v
