#! /usr/bin/env python
import os
import sys

routeid_table = sys.argv[1]
print('routeid_table = %s' % routeid_table)

fh = open(routeid_table)

for l in fh.readlines():
    #print(l),
    (initiator, target, init_flow, targ_flow, targ_subrange, base_addr) = l.split(' ')
    print('initiator=%30s, target=%30s, init_flow=0x%s, targ_flow=0x%s, targ_subrange=0x%s, base_addr=0x%s' % (initiator, target, init_flow, targ_flow, targ_subrange, base_addr))
