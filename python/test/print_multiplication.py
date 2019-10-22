import os
import sys

def print_mul_1_to_9():
    for i in range(1, 10):
        #for j in range(i, 10):
        for j in range(1, i):
            print('%2d x %-2d = %2d' % (i, j, i*j), end=' ')
        print('')

def print_starts():
    for i in range(0, 10):
        temp = i * 2 + 1
        print(' ' * (25 - i), '*' * temp)
    for i in range(0, 10):
        temp = 25 - i * 2 - 1
        print(' ' * (15 + i), '*' * temp)

print_starts()
