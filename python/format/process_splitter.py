import os
import sys
splitted = []
with open('splitter.txt', 'r') as f:
    for l in f:
        if 'Not allocated' in l:
            pass
        else:
            splitted = l.split()
            offset = splitted[0]
            desc = splitted[1]
            print('{0x%03X, "%s"},' % (int(offset, 16), desc))
