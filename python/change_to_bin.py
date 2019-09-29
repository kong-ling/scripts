import os
import sys

if len(sys.argv) < 2:
    print('Welcome')

for i in range(1, len(sys.argv)):
    #print('%d -> %s' % (i, sys.argv[i]))
    if '0x' in sys.argv[i]:
        tmp = int(sys.argv[i], 16)
    else:
        tmp = int(sys.argv[i], 10)
        pass
    bin_str =  bin(tmp)
    print('\n%d -> %d => %s\n' % (i, tmp, bin_str))
    for i in range(len(bin_str) - 2):
        print('%2d' % (len(bin_str) - 3 - i), end=' ')

    print('\n')

    for i in range(len(bin_str) - 2):
        print('%2s' % bin_str[2+i], end=' ')

    print('\n----------------------\n')
