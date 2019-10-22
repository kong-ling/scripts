# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import re
import re
import time
import datetime

result_dir = '/p/libdev/lte_ip.work/lingkong/xg766_es1_latest_hw'
result_file = 'lteSwOcrxProcPdcchDecodingCA_para3CA_01_level1/reports_lingkong/case_053__2018-01-18_09_54_42.txt'

# the full path for the file
f = '/'.join([result_dir, result_file])
print(f)

t = time.ctime(os.path.getmtime(f))

print('create time: %s' % t)

file_name = '2018-01-18_09_54_42'
file_ctime = datetime.datetime.strptime(file_name,'%Y-%m-%d_%H_%M_%S')
print('file_ctime=%s' % file_ctime)
