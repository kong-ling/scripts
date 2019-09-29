
testlist='/nfs/iind/disks/oc6ws_vol6/lingkong/xg766_se_development/lte_phy/lte_se/algorithms/testlist.txt'


# | 1300 |     LTX | bwcSwLtxProcPusch_paraCqiR13:01                                     |  1 2   | merged [1:1:75]                                                                       | 
def find_test_index_and_total():
    '''find the test's total testcase number from  testlist'''
    fh = open(testlist)
    all_tests = fh.readlines()
    for t in all_tests:
        t = t.strip()
        tlist = t.split('|')

        #remove spaces
        if len(tlist) > 4:
            print(tlist.strip())


if __name__ == '__main__':
    find_test_index_and_total()
