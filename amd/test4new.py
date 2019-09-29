import os
import sys


def shift_n_and(data, immediate):
    return ( (data >> (immediate & 0x1f)) & (immediate >> 5))

def func(r1): #python
    r3 = r1
    r10 = shift_n_and(r3, 0x1e8)
    if r10 == 0x5:
        r4 = 1
    else:
        r4 = 0

    #r3 = LdPfpPrgmStrmSelect(r0); #ld r3, `LdPfpPrgmStrmSelect(r0);
    r3 = 1; #ld r3, `LdPfpPrgmStrmSelect(r0);
    r2 = shift_n_and(r3, 0x3c)

    r3 = r1

    print('r1=%x, r2=%x, r3=%x, r4=%x, r10=%x\n' % (r1, r2, r3, r4, r10))

if __name__ == '__main__':
    for data in [0x00000500, 0x0fe00504]:
        func(data)
