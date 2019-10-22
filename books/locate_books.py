import os
import sys
import re
import argparse

parser = argparse.ArgumentParser(description='Copy file to specified folder')
parser.add_argument('-l', '--language', help='specify language')
parser.add_argument('echo', help='test echo')
args = parser.parse_args()

print(args.language)
print(args.echo)

if args:
    lang_pat = re.compile('perl.*\.pdf')

    for root, dirs, files in os.walk('C:\\Users\\lingkong\\', topdown = True):
        for f in files:
            full_f = os.path.join(root, f)
            if lang_pat.search(full_f):
                print(full_f)
                if 'help' not in args.help:
                    os.system('mv %s .' % (full_f))
