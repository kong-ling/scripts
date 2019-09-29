import os
import sys

data_for_xsum = [
    #0x01234567, 0x89abcdef, 0xdeadbeef, 0xfacecafe, 0xfeedface, 0xbeeddeed, 0xbadfacef, 0xcafebeef,
    #0x89abcdef, 0x01234567, 0x01234567, 0x89abcdef, 0x01234567, 0x89abcdef, 0x01234567, 0x89abcdef
    0x01234567, 0x89abcdef, 0xdeadbeef, 0xfacecafe
]

datas = [
    [0x01234567, 0x89ABCDEF, 0xDEADBEEF, 0xFACECAFE], #0191
    [0xFEEDFACE, 0xBEEDDEED, 0xBADFACEF, 0xCAFEBEEF], #8956
    [0x89ABCDEF, 0x01234567, 0x01234567, 0x89ABCDEF], #3C48
    [0xBEEFDEAD, 0xCAFEBEEF, 0x01234567, 0xFACEBEEF], #27D5
    [0xDEEDFACE, 0x87654321, 0xDEADBEEF, 0xFACECAFE], #07AF
]

def calc_xsum_all_bytes(data32):
    '''Calculate 32-bit data's checksum'''
    #extrace hight and low 16-bt data
    #print(data32)
    hi = (data32 & 0xffff0000) >> 16;
    lo = (data32 & 0x0000ffff) >> 0;
    sum = (hi + lo)

    #add the 17th bit (carry bit) to the sum
    sum2 = ((sum & 0xffff0000) >> 16) + (sum & 0x0000ffff)
    #print('    \033[07;32m0x%04X + 0x%04X = 0x%08X ->0x%08X\033[0m' % (hi, lo, sum, sum2))
    #print('\033[07;37m0x%04X + 0x%04X = 0x%08X ->0x%08X\033[0m' % (hi, lo, sum, sum2))
    return sum2

#with start offset
#stofs, from which byte to start the calculation
def calc_xsum_all_bytes_with_offset(data32, stofs):
    '''Calculate 32-bit data's checksum'''
    ###extrace hight and low 16-bt data
    ##data32_changed = data32 & (stofs)
    ##return sum2

# list for 128-bit
# e.g.   [0x01234567, 0x89abcdef, 0xdeadbeef, 0xfacecafe]
def calc_xsum_all_bytes_for_data128(data128):
    '''Calculate 128-bit data's checksum'''
    chksum = []
    for i in range(4): # 4 32-bit word
        xsum = calc_xsum_all_bytes(data128[i])
        chksum.append(xsum)

    sum1 = 0 #direct result by sum
    for i in chksum: # 4 32-bit word
        sum1 = sum1 + i
        sum2 = ((sum1 & 0xffff0000) >> 16) + (sum1 & 0x0000ffff)
        #print('sum1=0x%08X, sum2=0x%08X' % (sum1, sum2))

    return sum2
#convert integer to string
def shift_data128(data128, shift_bytes):
    data_string=''
    data_len = len(data128)

    #convert the data to a string
    for i in range(data_len):
        data_string += ('%08X' % data128[data_len - 1 - i])

    #data128_s_shifted = data_string[0:len(data_string) - 2]
    if shift_bytes == 0:
        data128_s_shifted = data_string
    else:
        data128_s_shifted = data_string[0: -shift_bytes*2]
    print('shift_bytes=%d, data128_s_shifted=%s' % (shift_bytes, data128_s_shifted.rjust(32, '0')))
    data128_shifted = []

    #split the string to integers
    for i in range(data_len):
        if i == 0:
            d = data128_s_shifted[-8-8*i:]
        else:
            d = data128_s_shifted[-8-8*i:-8*i]
        if d == '':
            data128_shifted.append(0)
        else:
            data128_shifted.append(int(d, 16))
        #print(d)
    #print(data128_shifted)
    return data128_shifted

#for i in range(8):
#    shift_data128(data_for_xsum, i)

shifts_xsum_pair = []
for i in range(len(datas)):
    print('-----%d------\n' % i),
    #for d in data:
    #    print('0x%08X' % d),
    #print('\n'),
    xsum_for_shift = []
    for shift_bytes in range(9):
        result = calc_xsum_all_bytes_for_data128( shift_data128(datas[i], shift_bytes))
        #print('\033[07;34mChecksum=0x%08X\033[0m' % result)
        print('Checksum=\033[07;%dm0x%04X\033[0m' % (shift_bytes+31, result))
        xsum_for_shift.append(result)

    shifts_xsum_pair.append(xsum_for_shift)

print('%s/*' % (' '*8)),
for i in range(9):
    print('%5d    ' % i),
print('*/\n')

for i in range(len(shifts_xsum_pair)):
    print('{'),
    for j in range(len(shifts_xsum_pair[i])):
        print('0x%04X,' % shifts_xsum_pair[i][j]),
    print('}, /*%d*/ ' % i)
