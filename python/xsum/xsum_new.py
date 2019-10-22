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

####for i in (range(no_of_data)):
####    data = data_for_xsum[i]
####    xsum = calc_xsum_all_bytes(data_for_xsum[i])
####    print('%d -> 0x%08X -> 0x%08X' % (i, data, xsum))
####    chksum.append(calc_xsum_all_bytes(data_for_xsum[i]))
####
####
####
####sum_for_all= 0
####for i in chksum:
####    print('i=0x%08X' % (i)),
####    #sum_for_all = (sum_for_all + i) & 0xffff
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

for shift_bytes in range(8):
    for data in datas:
        result = calc_xsum_all_bytes_for_data128( shift_data128(data, shift_bytes))
        print('\033[07;34m checksum=0x%08X\033[0m' % result)

'''
for data128 in datas:
    #print(data128)
    result = calc_xsum_all_bytes_for_data128(data128)
    print('\033[07;31m checksum=0x%08X\033[0m' % result)


for data128 in datas_1byte_1:
    #print(data128)
    result = calc_xsum_all_bytes_for_data128(data128)
    print('\033[07;32m checksum=0x%08X\033[0m' % result)

for data128 in datas_2byte_1:
    #print(data128)
    #for d in data128:
    #    print('0x%08X' % d),
    #print('\n')
    result = calc_xsum_all_bytes_for_data128(data128)
    print('\033[07;33m checksum=0x%08X\033[0m' % result)

for data128 in datas_3byte_1:
    #print(data128)
    #for d in data128:
    #    print('0x%08X' % d),
    #print('\n')
    result = calc_xsum_all_bytes_for_data128(data128)
    print('\033[07;34m checksum=0x%08X\033[0m' % result)
datas_1byte = [
    [0x01234500, 0x89ABCDEF, 0xDEADBEEF, 0xFACECAFE], #0191
    [0xFEEDFA00, 0xBEEDDEED, 0xBADFACEF, 0xCAFEBEEF], #8956
    [0x89ABCD00, 0x01234567, 0x01234567, 0x89ABCDEF], #3C48
    [0xBEEFDE00, 0xCAFEBEEF, 0x01234567, 0xFACEBEEF], #27D5
    [0xDEEDFA00, 0x87654321, 0xDEADBEEF, 0xFACECAFE], #07AF
]
datas_1byte_1 = [
    [0xEF012345, 0xEF89ABCD, 0xFEDEADBE, 0x00FACECA], #0191
    [0xEDFEEDFA, 0xEFBEEDDE, 0xEFBADFAC, 0x00CAFEBE], #8956
    [0x6789ABCD, 0x67012345, 0xEF012345, 0x0089ABCD], #3C48
    [0xEFBEEFDE, 0x67CAFEBE, 0xEF012345, 0x00FACEBE], #27D5
    [0x21DEEDFA, 0xEF876543, 0xFEDEADBE, 0x00FACECA], #07AF
]
datas_2byte = [
    [0x01230000, 0x89ABCDEF, 0xDEADBEEF, 0xFACECAFE], #0191
    [0xFEED0000, 0xBEEDDEED, 0xBADFACEF, 0xCAFEBEEF], #8956
    [0x89AB0000, 0x01234567, 0x01234567, 0x89ABCDEF], #3C48
    [0xBEEF0000, 0xCAFEBEEF, 0x01234567, 0xFACEBEEF], #27D5
    [0xDEED0000, 0x87654321, 0xDEADBEEF, 0xFACECAFE], #07AF
]
datas_2byte_1 = [
    [0xCDEF0123, 0xBEEF89AB, 0xCAFEDEAD, 0x0000FACE], #0191
    [0xDEEDFEED, 0xACEFBEED, 0xBEEFBADF, 0x0000CAFE], #8956
    [0x456789AB, 0x45670123, 0xCDEF0123, 0x000089AB], #3C48
    [0xBEEFBEEF, 0x4567CAFE, 0xBEEF0123, 0x0000FACE], #27D5
    [0x4321DEED, 0xBEEF8765, 0xCAFEDEAD, 0x0000FACE], #07AF
]
datas_3byte = [
    [0x01000000, 0x89ABCDEF, 0xDEADBEEF, 0xFACECAFE], #0191
    [0xFE000000, 0xBEEDDEED, 0xBADFACEF, 0xCAFEBEEF], #8956
    [0x89000000, 0x01234567, 0x01234567, 0x89ABCDEF], #3C48
    [0xBE000000, 0xCAFEBEEF, 0x01234567, 0xFACEBEEF], #27D5
    [0xDE000000, 0x87654321, 0xDEADBEEF, 0xFACECAFE], #07AF
]
datas_3byte_1 = [
    [0xABCDEF01, 0xADBEEF89, 0xCECAFEDE, 0x000000FA], #0191
    [0xEDDEEDFE, 0xDFACEFBE, 0xFEBEEFBA, 0x000000CA], #8956
    [0x23456789, 0x23456701, 0xABCDEF01, 0x00000089], #3C48
    [0xFEBEEFBE, 0x234567CA, 0xCEBEEF01, 0x000000FA], #27D5
    [0x654321DE, 0xADBEEF87, 0xCECAFEDE, 0x000000FA], #07AF
]
datas_4byte = [
    [0x00000000, 0x89ABCDEF, 0xDEADBEEF, 0xFACECAFE], #0191
    [0x00000000, 0xBEEDDEED, 0xBADFACEF, 0xCAFEBEEF], #8956
    [0x00000000, 0x01234567, 0x01234567, 0x89ABCDEF], #3C48
    [0x00000000, 0xCAFEBEEF, 0x01234567, 0xFACEBEEF], #27D5
    [0x00000000, 0x87654321, 0xDEADBEEF, 0xFACECAFE], #07AF
]
datas_4byte_1 = [
    [0xFACECAFE, 0x89ABCDEF, 0xDEADBEEF, 0x00000000], #0191
    [0xCAFEBEEF, 0xBEEDDEED, 0xBADFACEF, 0x00000000], #8956
    [0x89ABCDEF, 0x01234567, 0x01234567, 0x00000000], #3C48
    [0xFACEBEEF, 0xCAFEBEEF, 0x01234567, 0x00000000], #27D5
    [0xFACECAFE, 0x87654321, 0xDEADBEEF, 0x00000000], #07AF
]
'''
