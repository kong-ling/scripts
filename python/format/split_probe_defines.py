import os
import sys
import re

master_and_base = {}
probes = []
base_address = 0

file_for_defines = sys.argv[1]

fh = open(file_for_defines)
fh_header = open('probe.h', 'w')

for l in fh.readlines():
    #print(l),
    if 'Reserved' in l:
        continue

    (addr, reg_name, probe_name) = re.split(r'\s+', l.strip())
    if base_address == 0: #find the base address
        base_address = int(addr, 16)
    #print(regs, addr, base, master)
    #reg_name_in_short = reg_name.replace('slice0_xtc_packet_probe_main_Probe_', '')
    #reg_name_in_short = reg_name.replace('noc_primary_error_observer_main_', '')
    #print('index: %d' % reg_name.index('main_'))
    reg_name_in_short= reg_name[reg_name.index('main_') + 5 :]
    no_of_spaces = ' ' * (30 - len(reg_name_in_short))
    offset = int(addr, 16) - base_address
    print('{0x%03x, "%s"%s},' % (offset, reg_name_in_short, no_of_spaces))
    master_and_base[offset] = reg_name_in_short
    probes.append(offset)

##print('enum NOC_probes = {')
#for i in range(len(probes)):
#    print('    %03x,' % (probes[i]))
##print('};')

for k in sorted(master_and_base.keys()):
    #print(k, master_and_base[k])
    print('%s%s = 0x%03x, ' % (master_and_base[k], ' ' * (30 - len(master_and_base[k])), k))
