import os
import sys
import subprocess

p = subprocess.Popen('net use',
                    stdout = subprocess.PIPE,
                    stdin = subprocess.PIPE)

print(type(p))
for drv in p.stdout.readlines():
    print(drv.strip())
