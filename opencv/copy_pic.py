#!--coding=utf-8--

import argparse
import sys


'''
with open('introduction.jpg', 'rb') as pic_rd:
    contents = pic_rd.read()

#for l in contents:
#    print('%02X' % l),

with open('introduction_out.jpg', 'wb') as pic_wr:
    #for idx, data in enumerate(contents):
    #    pic_wr.write(data)
    pic_wr.write(contents)
'''
###################################################

if sys.argv[1]:
    pic = sys.argv[1]
    pic_out = pic.replace('.jpg', '_out.jpg')
    print(pic_out)
else:
    sys.exit()

with open(pic, 'wb') as pic_wr:
    with open(pic_out, 'rb') as pic_rd:
        for idx, line in enumerate(pic_rd):
            print(idx, '==>', [hex(x) for x in list(line)])
            pic_wr.write(line)

#for data in list(open('introduction.jpg', 'rb')):
#    print(data),
