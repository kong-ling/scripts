#!/usr/bin/env python

import os
import sys
import datetime
import subprocess

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")


#set the remote build folder for sle test
#usw_build_path = "/local/lingkong/posv_cv-usw/build/configs/polaris_sle"
#usw_build_path = "./build/configs/polaris_sle"
usw_build_path = "./build/configs/polaris_ppu_sle"
#set ppu_image_path = "lingkong@fmci202453.fm.intel.com:/nfs/site/disks/ppa_emulation_disk_01/users/lingkong/test/image"

###################################################################################
####    folsom
###################################################################################
#ppu_image_path = "lingkong@fmci202453.fm.intel.com:/nfs/site/disks/ppa_emulation_disk_01/users/lingkong/ppu_image_18ww37b/image"

###################################################################################
####    santa clara
###################################################################################
#ppu_image_path = "lingkong@sccj019906.sc.intel.com:/nfs/sc/disks/sc_polaris_soccve03/users/lingkong/ppu_image_18ww46a/"
ppu_image_path = "lingkong@sccj019906.sc.intel.com:/nfs/sc/disks/sc_polaris_soccve03/users/lingkong/ppu_image_18ww50d/"
target_folder = 'image_18ww43e'
#ppu_image_path = "lingkong@sccj002328.sc.intel.com:/nfs/site/disks/sc_polaris_emu04/usrs/lingkong/ppu_image_18ww43b/image"

print('build path: %s' % usw_build_path)
print('image path: %s' % ppu_image_path)

#mkdir -p $ppu_image_path
#os.makedirs(ppu_image_path)

files_to_copy = [
    'ppu_slice0/ppu_slice0.iccm.hex',
    'ppu_slice0/ppu_slice0.dccm.hex',
    'ppu_slice0/ppu_slice0.shm0_0_0.hex',
    'ppu_slice0/ppu_slice0.shm0_0_1.hex',
    'ppu_slice0/ppu_slice0.shm0_0_2.hex',
    'ppu_slice0/ppu_slice0.shm0_0_3.hex',
    'ppu_slice0/ppu_slice0.shm0_1_0.hex',
    'ppu_slice0/ppu_slice0.shm0_1_1.hex',
    'ppu_slice0/ppu_slice0.shm0_1_2.hex',
    'ppu_slice0/ppu_slice0.shm0_1_3.hex',
    'ppu_arm0_lmu/ppu_arm0_lmu.lmu1.hex',
    'ppu_arm0_lmu/ppu_arm0_lmu.lmu2.hex',
    'ppu_arm0_lmu/ppu_arm0_lmu.lmu3.hex',
    'ppu_arm_lmu_bios/ppu_arm_lmu_bios.lmu.hex'
]

#scp_cmd = 'scp --password-file ~/ppu/password --overwrite yes '
scp_cmd = 'scp '

#for f in files_to_copy:
#    hex = '%s/%s' % (usw_build_path, f)
#    #print(hex)
#    full_scp_cmd = '%s %s %s' % (scp_cmd, hex, ppu_image_path)
#    print('full_scp_cmd: %s' % full_scp_cmd)
#    #subprocess.Popen(full_scp_cmd)
#    os.system(full_scp_cmd)

cmd = 'scp %s/ppu_*/*.hex %s' % (usw_build_path, ppu_image_path)
print(cmd)
os.system(cmd)
