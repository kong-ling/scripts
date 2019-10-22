import os
import sys
import string
import re

input_file = sys.argv[1]
input_file_name = os.path.splitext(input_file)[0]
output_file = os.path.splitext(input_file)[0] + '.c'
print(input_file)
print(output_file)

fr = open(input_file, 'r')
fw = open(output_file, 'w')

pattern0 = re.compile(r'(\w+)')
pattern1 = re.compile(r'(\w+) (\w+) (\w+)')       # offset, bytes, length
pattern2 = re.compile(r'(\w+) (\w+) (\w+) (\w+)') # data
lineNr = 0
for line in fr:
    lineNr = lineNr + 1
    #print(lineNr, '->', line),
    try:
        line = line.replace('\n', '')
        res = line.split(' ')

        if len(res) == 1:
            #print(lineNr, len(res)),
            #print(lineNr),
            fw.write('\n')
        elif len(res) == 3: # data is in decimal
            res_new = ''
            for data in res:
                res_new = res_new + data + ',';
            fw.write(res_new + '\n')
        else:               #data is in hex mode
            res_new = ''
            for data in res:
                res_new = res_new + '0x' + data + ',';
            fw.write(res_new + '\n')

    except:
        pass

fr.close()
fw.close()
