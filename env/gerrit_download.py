import os
import sys

print('Executing %s' % sys.argv[0])

if len(sys.argv) < 2 :
    print('''
          Usage: python %s gerritid
          ''' % sys.argv[0])
else:
    reset = 'git reset --hard 8a0596060c788be9b9855cf8a2fc494d2572dd0c'
    download = 'bee download -c 1035235 --keep-origin-metadata'
    print(reset)
    print(download)
    os.system(reset)
    os.system(download)
