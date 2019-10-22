import sys
import os
import re
import string

#compress_script_path = "%s/BwcStimuliConvert/bin/fix_compress_dump.py" % os.getenv('workHostMatlab')
compress_script_path = "%s/BwcStimuliConvert/bin" % os.getenv('workHostMatlab')
print(compress_script_path)

sys.path.append(compress_script_path)
#print(sys.path)

import fix_compress_dump


def compress_decompress_ref_data(refDatFile):
    #'''
    #    compress and decompress the data, backup the origin file to backup folder
    #    then write to the same file
    #'''
    print('Processing %s' % refDatFile)
    src_dir = os.path.dirname(refDatFile)

    if src_dir == '':
        src_dir = '.'
    else:
        pass
    backup_dir = '%s/backup' % src_dir

    backup_name = '%s/%s' % (backup_dir, os.path.basename(refDatFile))
    print('   Backup: %s' % backup_name)

    #make backup dir
    try:
        os.makedirs(backup_dir)
    except Exception as e: #if backup folder exist, skip
        #print('%s', e)
        pass

    #backup refDatFile to backup folder
    #os.rename(refDatFile, backup_name)

    #open the backup file and write to the origin file
    #fid = open('/p/libdev/lte_ip.work/lingkong/xg766_es1_latest_hw/bwcSwLtxProcPusch_para_01_level1/case_001/ssl_slv12_ref.dat', 'r')
    #fid = open(backup_name, 'r')
    #fid_out = open(refDatFile, 'w')
    fid_out = open(backup_name, 'w')
    fid= open(refDatFile, 'r')
    for line in fid.readlines():
        #print(line),
        line = line.strip('\r\n')
        line_splited = line.split(' ') #split using space

        # blank line and header line containing (offset, length, bitwidth)
        if len(line_splited[0]) == 0 or len(line_splited) == 3:
            fid_out.write('%s\n' % line)
        else: #compress and decompress
            outdata = []
            for i in range(0, len(line_splited)):
                data = line_splited[i]
                print(data),
                #try:
                #    hexd= hex(int(data, 16))
                #    print(hexd)
                #except Exception as e:
                #    print 'Error : %s' % e
                hex_h= (int(data[0:3], 16)) #first half
                hex_l= (int(data[3:], 16)) #second half
                #print ('hex: %03X %03X') % (hex_h, hex_l), 
                compressed_h = fix_compress_dump.lte_compress(hex_h, 0)
                compressed_l = fix_compress_dump.lte_compress(hex_l, 0)
                decompressed_h = fix_compress_dump.lte_decompress(compressed_h)
                decompressed_l = fix_compress_dump.lte_decompress(compressed_l)
                converted = (decompressed_h << 12) + (decompressed_l << 0)
                outdata.append(converted)

            output = '%06X' % outdata[0]
            for i in range(1, len(line_splited)):
                output = '%s %06X' % (output, outdata[i])
            print('%s\n' % output)
            fid_out.write('%s\n' % output)

    fid.close()
    fid_out.close()

if __name__ == '__main__':
    #fid = open('/p/libdev/lte_ip.work/lingkong/xg766_es1_latest_hw/bwcSwLtxProcPusch_para_01_level1/case_001/ssl_slv12_ref.dat', 'r')
    ref = '/p/libdev/lte_ip.work/lingkong/xg766_es1_latest_hw/bwcSwSystemRx_paraBandwidth_01_level1/case_001_backup/irx_cam0_ref.dat'
    compress_decompress_ref_data(sys.argv[1])
