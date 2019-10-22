import os
import sys
import re

#rsync command for the specified user and path
PATH_AT_IMU = r"rsync -rv username@server_folder_path"
#print(PATH_AT_IMU)

#the result will be wrint to rsync_cmd_file
rsync_cmds = open('rsync_cmd_file', 'w')

#list the specified directories
odrx_folders = os.popen('ls -d -1 -rt bwcSwOdrx*')

#process the matched folders
for folder in odrx_folders.readlines():
    folder = folder.strip('\r\n')
    print(folder)

    if '4RxXg766' in folder:
        break

    cmd = '%s/%s .\n' % (PATH_AT_IMU, folder)
    rsync_cmds.write(cmd)

rsync_cmds.close()

#inform the server at remote site, so that the sync can be done automatically or 
#periodically
