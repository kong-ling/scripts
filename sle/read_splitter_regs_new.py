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
for offset in range(0x246):
    #print(offset)
    idx = offset * 4
    a = random.randint(0, 0x100000000)
    #print(idx, '0x%08X' % a)

    if (idx==0x4):
        result[idx] = ''
        continue
    if (idx>=0x20c and idx<0x400):
        continue
    if (idx>=0x404 and idx<0x800):
        continue
    if (idx>=0x808 and idx<0x900):
        continue
    if (idx )  >=0x918:
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
    if type(result[k]) == str:
        print('%s' % (' ' * 10)),
    else:
        print('0x%08X' % (result[k])),
    if k % 0x10 == 0:
        print('<-0x%03X\n' % k),

for k in range(len(result)):
    if k % 4 == 0:
        print(': %d\n' % k),
    print('0x%03X' % k),
