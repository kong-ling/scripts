import time
import os
import sys
import random

print('Executing %s' % sys.argv[0])
offset=0
result={}

for arg in sys.argv:
    print(arg)

if len(sys.argv) > 2:
    dryrun = 1
else:
    dryrun = 0

#for offset in range(0x246):
for offset in range(0x0,0x246):
    #print(offset)
    idx = offset * 4
    a = random.randint(0, 0x100000000)
    #print(idx, '0x%08X' % a)

    if idx in range(0x20c, 0x400, 4):
        print('%03X' % idx),
        continue
    if idx in range(0x404, 0x800, 4):
        print('%03X' % idx),
        continue
    if idx in range(0x808, 0x900, 4):
        print('%03X' % idx),
        continue
    if idx in range(0x918, 0xa00, 4):
        break

    #a = ocp_xactor_ppu_mss_config_noc_read32(0x32440000 + idx)
    result[idx] = (a)
    #time.sleep(0.1)

    offset=offset+1

#for i in reversed(range(len(result))):
for k in reversed(sorted(result.keys())):
    #print(i),
    #print('%03X->0x%08X' % (i*4, result[i])),
    ##print('0x%08X' % ( result[i])),
    #print('0x%03X:0x%08X' % (k, result[k])),
    #print('0x%03X' % (k)),
    offset = k & 0xF
    if offset == 0:
        print('offset0'),
    if offset == 4:
        print('offset4'),
    if offset == 8:
        print('offset8'),
    if offset == 0xc:
        print('offsetC'),
    if k % 0x10 == 0:
        print(':0x%03X\n' % k),
