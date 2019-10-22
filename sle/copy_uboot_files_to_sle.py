#!/usr/bin/env python

import os
import sys
import datetime
import subprocess

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")


usw_build_path = "."
target_folder = ''
ppu_image_path = "lingkong@sccj019906.sc.intel.com:/nfs/site/disks/sc_polaris_emu01/usrs/lingkong/xg816_a0/image"
ppu_image_path = ppu_image_path + target_folder

print('build path: %s' % usw_build_path)
print('image path: %s' % ppu_image_path)

files_to_copy = [
    'u-boot-xgold.bin',
    'spl/u-boot-spl-xgold.bin'
]

#scp_cmd = 'scp --password-file ~/ppu/password --overwrite yes '
scp_cmd = 'scp '

for f in files_to_copy:
    hex = '%s/%s' % (usw_build_path, f)
    #print(hex)
    full_scp_cmd = '%s %s %s' % (scp_cmd, hex, ppu_image_path)
    #print('full_scp_cmd: %s' % full_scp_cmd)
    #subprocess.Popen(full_scp_cmd)
    os.system(full_scp_cmd)
