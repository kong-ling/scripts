import os
import sys
import re

pat = '(\w+) = \(unsigned int\)\((\w+) \+ (\w+)\)'
#pat = 'HWa.*PacketProbe(\w+) = \(unsigned int\)\(MSS'

packet_probe = []
error_observer = []
packet_observer = []

io_file = 'config_noc_mio.h'
print('//generated from %s' % io_file)


def insert_space(number_of_space):
    return ' ' * number_of_space

def format_reg(reg, reg_addr):
    reg_formatted = '%s %s; // %s' % (reg, insert_space(20 - len(reg)), reg_addr)
    return reg_formatted

with open(io_file, 'r') as f:
    lineNo = 0
    for line in f:
        lineNo = lineNo + 1
        line = line.strip()
        match = re.search(pat, line)
        if match:
            #print(line),
            reg_name, reg_base, reg_addr = match.groups()
            reg_addr = '0x' + reg_addr[-3:] #only keep the offset value
            #print('%s, %s, %s' % (reg_name, reg_base, reg_addr))
            if 'gMPacketProbeMainProbe' in reg_name:
                #print('%d, %s' % (lineNo, line)),
                reg = reg_name.split('PacketProbeMainProbe')[1]
                packet_probe.append(format_reg(reg, reg_addr))

            if 'MainErrorlogger0' in reg_name:
                #print('%s, %s, %s' % (reg_name, reg_base, reg_addr))
                reg = reg_name.split('MainErrorlogger0')[1]
                #reg_formatted = '%s, %s, // %s' % (reg, insert_space(20 - len(reg)), reg_addr)
                error_observer.append(format_reg(reg, reg_addr))

            if 'Atbendpoint' in reg_name:
                reg = reg_name.split('Atbendpoint')[1]
                packet_observer.append(format_reg(reg, reg_addr))

def generate_struct(regs, desc):
    print('typedef {'),
    for reg in regs:
        print('    unsigned int %s;' % reg)

    print('} T_%s;\n' % desc.upper()),

generate_struct(packet_observer, 'packet_observer')
generate_struct(error_observer, 'error_observer')
generate_struct(packet_probe, 'packet_probe')
