import os
import sys
import datetime
import subprocess

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

files_of_u_boot_to_copy = [
    'u-boot-xgold.bin',
    'spl/u-boot-spl-xgold.bin'
]

def copy_u_boot_files_to_sle_server():
    '''start to copy files to sle server'''
    for f in files_of_u_boot_to_copy:
        full_scp_cmd = 'scp %s %s%s' % (f, vnc_server_name, image_folder_on_sle_server)
        print(full_scp_cmd)
        os.system(full_scp_cmd)

vnc_server_name = '%s@sccj018021.sc.intel.com' % os.environ.get('USER')
image_folder_on_sle_server = '/nfs/site/disks/sc_polaris_emu01/usrs/lingkong/xg816_a0/sle_for_mss/image'

cmds_for_u_boot = [
    #'make distclean',
    'make xgold816_a0_sle_defconfig all -j96',
    #'python /local/lingkong/posv_cv_scripts-scripts/sle/copy_uboot_files_to_sle.py',
    'scp %s %s:%s/' % (files_of_u_boot_to_copy[0], vnc_server_name, image_folder_on_sle_server),
    'scp %s %s:%s/' % (files_of_u_boot_to_copy[1], vnc_server_name, image_folder_on_sle_server),
    #'ssh lingkong@sccj019906.sc.intel.com "cd %s; source generate_ecc_file"' % image_folder_on_sle_server
    'ssh lingkong@sccj019906.sc.intel.com "cd %s; source ubootbin2hex816.sh"' % image_folder_on_sle_server
]


for cmd in cmds_for_u_boot:
    print(cmd)
    os.system(cmd)
