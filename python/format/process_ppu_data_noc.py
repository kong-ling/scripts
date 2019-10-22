import os
import sys

def insert_space(number_of_space):
    return ' ' * number_of_space

niu_def = {}
idx = 0
with open('ppu_data_noc.txt') as f:
    for line in f:
        #print(line)
        line_splitted = line.split()
        if line_splitted:
            (niu, accessible, size, addr) = line_splitted
            #print(line_splitted[0], line_splitted[3])
            niu = niu.replace('.', '_')
            addr= addr.replace('_', '')
            print('%s%s= %3d,' % (niu, insert_space(80 - len(niu)), idx))
            niu_def[niu] = addr
            idx += 1

niu_base_definitions = []
ppu_noc_niu_bases = []
packet_probes = []
packet_observers = []
error_observers = []
noc_nius = []
with open('ppu_data_noc.txt') as f:
    for line in f:
        #print(line)
        line_splitted = line.split()
        if line_splitted:
            (niu, accessible, size, addr) = line_splitted
            #print(line_splitted[0], line_splitted[3])
            niu = niu.replace('.', '_')
            addr= addr.replace('_', '')
            #print('{"%s"%s, %s0x%s},' % (niu.upper(), insert_space(80 - len(niu)), insert_space(8-len(addr)), addr))
            #print('%s%s= %s0x%s,' % (niu.upper(), insert_space(60 - len(niu)), insert_space(8-len(addr)), addr))
            if 'packet_probe' in niu:
                reg = 'packet_probe_regs'
            elif 'packet_observer' in niu:
                reg = 'packet_observer_regs'
            elif 'error_observer' in niu:
                reg = 'error_observer_regs'
            else:
                reg = 'firewall_regs'
            niu_base_definitions.append('BASE_%s%s= %s0x%s,' % (niu.upper(), insert_space(60 - len(niu)), insert_space(8-len(addr)), addr))
            #noc_nius.append('{"%s"%s, 0x%s}' % (niu, insert_space(60 - len(niu)), addr.zfill(8)))
            #noc_nius.append('{"%s"%s, %s%s, %s%s}' % (niu, insert_space(50 - len(niu)), 'BASE_' + niu.upper(), insert_space(50-len(niu)), reg, insert_space(20 - len(reg))))
            size = 'sizeof(%s)/sizeof(%s[0])' % (reg, reg)
            size_with_space = '%s%s' % (size, insert_space(65 -len(size)))
            noc_nius.append('{"%s"%s, %s%s, %s%s, %s}' % (niu, insert_space(50 - len(niu)), 'BASE_' + niu.upper(), insert_space(50-len(niu)), reg, insert_space(20 - len(reg)), size_with_space))
            niu = 'BASE_%s' % niu
            ppu_noc_niu_bases.append(niu.upper())
            if 'error_obser' in niu:
                error_observers.append(niu.upper())
            elif 'packet_obser' in niu:
                packet_observers.append(niu.upper())
            elif 'packet_probe' in niu:
                packet_probes.append(niu.upper())
            else:
                pass
print('*' * 20)
for base in sorted(niu_base_definitions):
    print(base)

def print_sorted_list(l, desc):
    print
    print('unsigned int %s[] = {' % desc)
    for base in sorted(l):
        print('    %s%s,' % (base, insert_space(60 - len(base))))
    print('};')

print_sorted_list(packet_probes, 'packet_probes')
print_sorted_list(packet_observers, 'packet_observers')
print_sorted_list(error_observers, 'error_observers')
print_sorted_list(ppu_noc_niu_bases, 'ppu_noc_niu_bases')
print_sorted_list(noc_nius, 'noc_nius')
