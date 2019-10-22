import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Calculate tips')
parser.add_argument('-a', '--amount', dest='sum', required=True, help='the actual paid amount')

args = parser.parse_args()

for i in range(5):
    paid = float(args.sum)
    rate = 1.15 + 0.05*i
    total = paid * rate
    print('%.2f x %.2f = %.2f' % (paid, rate, total))
