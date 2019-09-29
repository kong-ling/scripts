import os
import sys
import glob

for element in glob.glob(sys.argv[1]):
#for element in glob.glob('bwcSwOdrxProcDecodePdsch_para*4Rx*'):
    #print(element)
    os.system('find %s -name "*.txt" | xargs ls | xargs grep "Result: P"' % element)
