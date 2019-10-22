import sys

while True:
    input_hex = raw_input("Please input an hex\n")
    print input_hex
    
    bit_pos = 0
    bit_value = 0
    input_bin = bin(int(input_hex))
    print len(input_bin), input_bin
    shift_times = 0
    while input_int:
        print input_int 
        input >>= shift_times
        shift_times += 1
