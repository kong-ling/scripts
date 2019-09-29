import os
import subprocess

try:
    output = subprocess.Popen(["devcon","status","*"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)    #useing comma "," not space " " in Popen[]. replace the key word "*" to what you want to search.
    stdout, stderr = output.communicate()
    print("output: \n", output)
    print("stdout: \n", stdout) # output here if ok.
    print("stderr: \n", stderr)  # output if no arg
except subprocess.CalledProcessError:
    print('Exception handled')
