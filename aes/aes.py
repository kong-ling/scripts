import os
import sys
import string

a='abcdefghijklmnop'

for i in range(len(a)):
    #print(a[i], hex(ord(a[i]))),
    print(hex(ord(a[i]))),
    if (i % 4 == 0):
        print('\n')
