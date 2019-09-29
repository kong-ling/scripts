import os
import sys

for r1 in (0x500, 0x0fe00504):
    print('r1=%08X' % r1)
    r3 = r1 #mrr r3, r1
    print('r3=%08X' % r3)
    r10 = (r3 >> (0x1e8 & 0x1f)) & (0x1e8 >> 5)#srai r10, r3, 0x1e8;
    print('r10=%08X' % r10)
    if r10 == 0x5: #seqi r4, r10, 0x5;
        r4 = 1
    else:
        r4 = 0
    print('r4=%08X' % r4)
    #r3 = LdPfpPrgmStrmSelect(r0) #ld r3, `LdPfpPrgmStrmSelect(r0);
    r3 = 1 #ld r3, `LdPfpPrgmStrmSelect(r0);
    r2 = (r3 >> (0x3c & 0x1f)) & (0x3c >> 5) #srai r2, r3, 0x3c;
    print('r2=%08X' % r2)
    r3 = r1 #mrr r3, r1;
    print('r3=%08X' % r3)
    print('----------------')
