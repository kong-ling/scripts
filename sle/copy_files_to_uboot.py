#!/usr/bin/env python

import os
import sys
import datetime
import subprocess

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")


#set the remote build folder for sle test
#usw_build_path = "/local/lingkong/posv_cv-usw/build/configs/polaris_sle"
#usw_build_path = "./build/configs/polaris_sle"
#usw_build_path = './build/configs/polaris_ppu_multicore_sle_uboot'
usw_build_path = './build/configs/xmm8160_a0_ppu_multicore_sle_uboot'
#set ppu_image_path = "lingkong@fmci202453.fm.intel.com:/nfs/site/disks/ppa_emulation_disk_01/users/lingkong/test/image"

###################################################################################
####    folsom
###################################################################################
#ppu_image_path = "lingkong@fmci202453.fm.intel.com:/nfs/site/disks/ppa_emulation_disk_01/users/lingkong/ppu_image_18ww37b/image"

###################################################################################
####    santa clara
###################################################################################
target_folder = 'drivers/xgold/ppu/xgold816/a0'
ppu_image_path = '/local/lingkong/posv_cv-u-boot/%s' % target_folder
#ppu_image_path = "lingkong@sccj002328.sc.intel.com:/nfs/site/disks/sc_polaris_emu04/usrs/lingkong/ppu_image_18ww43b/image"

print('build path: %s' % usw_build_path)
print('image path: %s' % ppu_image_path)

#mkdir -p $ppu_image_path
#os.makedirs(ppu_image_path)

files_to_copy = [
    'ppu_arm0/ppu_arm0.strip',
    'ppu_arm_bios/ppu_arm_bios.strip'
]

#scp_cmd = 'scp --password-file ~/ppu/password --overwrite yes '
scp_cmd = 'cp -f'

for f in files_to_copy:
    hex = '%s/%s' % (usw_build_path, f)
    print(hex)
    full_scp_cmd = '%s %s %s' % (scp_cmd, hex, ppu_image_path)
    print('full_scp_cmd: %s' % full_scp_cmd)
    #subprocess.Popen(full_scp_cmd)
    os.system(full_scp_cmd)

###cmd = 'cp %s/ppu_*/*.hex %s' % (usw_build_path, ppu_image_path)
###print(cmd)
###os.system(cmd)
