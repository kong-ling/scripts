import os
import sys
import re

init_or_targ = '(\w+)\s+: (Flow:.*PPU_CONTROL_NOC_TOP\/)(.*)'
with open('Polaris_NoC_PPU_CONTROL.PPU_CONTROL_NOC_TOP_Arch.PPU_CONTROL_NOC_TOP_rtl.info', 'r') as f:
    for line in f:
        if 'InitFlow' in line:
            print('char * init_flow[] = {')
        elif 'TargFlow' in line:
            print('char * targ_flow[] = {')
        else:
            match = re.search(init_or_targ, line)
            if match:
                    #print('%s:"%s"' % (match.group(1), match.group(3)));
                    print('    "%s",' % (match.group(3)));
