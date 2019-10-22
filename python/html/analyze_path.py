import os
import sys
import re
import string

currentDir = os.getcwd()


#log file for run
file_list_for_run      = os.popen('find . -type f -name "*.txt" | xargs ls | xargs grep Result')
file_list_for_gen      = ''
file_list_for_xtRistTb = ''

#################################################
## debug
#################################################
#print '\nfile_list_for_gen: '
#for element in file_list_for_gen:
#    print element.strip()
#
#print '\nfile_list_for_xtRistTb: '
#for element in file_list_for_xtRistTb:
#    print element.strip()
#
#print '\nfile_list_for_run     : '
#for element in file_list_for_run:
#    print element.strip()

def get_test_info_from_testlist_split(tests = '/home/git.view/lingkong/fwi_ibis_development/lte_phy/lte_fw/tools/ltephyhostmatlab/utils/testlist.txt'):

    #testlist is the output of lteDispHwTests
    print 'Processing %s\n' % tests
    fh = open(tests, 'r')

    Idx       = 1
    Subcomp   = 2
    TestEntry = 3
    TestEntry_slice = 4
    Levels    = 5
    TestCases = 6
#| 001 |    FEFC | bwcSwFefcProcFft_para:01                                            |  1     | merged [1:1:11]                                                                                                                                                                                                             | 

    loop = 0

    dict_test = {}
    for each_line in fh:
        loop = loop + 1

        try:
            #if (loop >= 337) and (loop <= 344):
            #print loop
            each_line = each_line.strip('\r\n')
            match =  each_line.split('|')

            for i in range(len(match)):
                match[i] = match[i].strip()

            if len(match) <= 4:
                continue
            #print each_line

            #add to dict

            #key = match[Idx]
            # concate key
            origin_testEntry = match[TestEntry]
            #print 'origin_testEntry = %s\n' % origin_testEntry
            temp_testEntry = origin_testEntry.replace('_carrIdx0', '')
            #print 'temp_testEntry = %s\n' % temp_testEntry
            #key = '%s_level1' % (match[TestEntry])
            key = '%s_level1' % (temp_testEntry)
            key = key.replace(':', '_')
            #print 'key1=%s' % key1
            dict_test[key] = match
            #print '%s =>' % key, dict_test[key]

        except:
            #print loop
            #print 'Something wrong happened...'
            pass

    fh.close()
    return dict_test

if __name__ == '__main__':
    print "Executing %s\nFrom path:%5s\n" % (__file__, currentDir)
    if len(sys.argv) < 2:
        tests = get_test_info_from_testlist_split()
    else:
        tests = get_test_info_from_testlist_split(sys.argv[1])
    
    items = tests.items()
    items.sort()
    for (k,v) in items:
        print '[%s] --> ' % k, v

