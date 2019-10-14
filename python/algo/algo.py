import os
import sys

def sushu(d):
    if d <= 1:
        return -1
    if d % 2 ==0:
        return 1
    print('%4d:' % d, end='')
    for i in range(2, d):
        if d % i == 0:
            print(i, end=', ')
    print('\n')

if __name__ == '__main__':
    for i in range(1000):
        sushu(i)
    sushu(999999937)
