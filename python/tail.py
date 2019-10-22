import os
import sys
import re


#f = '/nfs/xa/proj/libdev/lte_ip.work/lingkong/xg766_es1_latest_hw/bwcSwSystemRx_paraBandwidth_01_level1/reports_lingkong_run/case_001__2018-02-26_18_21_32'
f = sys.argv[1]

f_content = os.popen('tail -n 500 %s' % f)
print(f_content)

ITERATION_NO = r"Start iteration (\d+)"
pat = re.compile(ITERATION_NO)

iter_list = []
for line in f_content.readlines():
    #print line,
    res = pat.search(line)
    if res:
        print(res.group(1))
        iter_list.append(res.group(1))

print('Iteration numbers = %s\n' % iter_list[-1])
