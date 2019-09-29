import os
import sys
import re

master_and_base = {}
nius = []

file_for_defines = sys.argv[1]

fh = open(file_for_defines)
fh_header = open('noc_nius.h', 'w')

for l in fh.readlines():
    #print(l),
    (regs, master_long, base, master) = re.split(r'\s+', l.strip())
    #print(regs, master_long, base, master)
    print('{"%-s"%s, %s}, //%d' % (master_long, ' ' * (65-len(master_long)), base, len(master_long)))
    master_and_base[master_long] = base
    nius.append(master_long)

#for v in sorted(master_and_base.values()):
#    print(v)
print('enum NOC_NIUS = {')
for i in range(len(nius)):
    print('    %s%s= %3s,' % (nius[i], ' ' *(65 - len(nius[i])), i))
print('};')


print('switch (base) {')
for i in range(len(nius)):
    struct = ''
    if 'ErrorLogger' in nius[i]:
        struct = 'error_observer_regs'
    elif 'packet_probe' in nius[i]:
        struct = 'packet_probe_regs'
    elif 'packet_observer' in nius[i]:
        struct = 'packet_observer_regs'
    else:
        continue
    #print('    %s%s= %3s,' % (nius[i], ' ' *(65 - len(nius[i])), i))
    total = 'sizeof(%s)/sizeof(%s[0])' % (struct, struct)
    #print('    case noc_nius[%s].base%s: niu= %s%s; total = %s; break;' % (nius[i], ' '*(65 - len(nius[i])), struct, ' '*(20 - len(struct)), total))
    print('    else if (base == noc_nius[%s].base) {noc_observer.niu = %s; noc_observer.total = %s;}' % (nius[i], struct, total))
print('}')
