
PPU_DATA_LMEM_17_0_L = 0x31400000
PPU_MSS_NOC_SLAVE_DMIF_L = 0x80000000
tb_list_base_addr = {}
tb_ddr_size = {}
tb_list_ptrQ = {}
num_tb_ptrs=100

#d-dict
#n- indent number
def out_dict(d, n, desc):
    print(desc)
    for k in sorted(d.keys()):
        print("%s%d -> 0x%08X" % (' '*n, k, d[k]))

for k in range(8):
    #tb_list_base_addr[k] =  k * 32'h1000_0000;
    tb_list_base_addr[k] =  PPU_DATA_LMEM_17_0_L + (k+1) * 0x10000
    tb_ddr_size[k] = 0x2;
    # initializing 100 DDR page ptrs in TB list
    for pg in range(num_tb_ptrs):
        tb_ptr_start = PPU_MSS_NOC_SLAVE_DMIF_L + (k+1) * 0x1000
        pg_ptr = pg * (2**(10+tb_ddr_size[k]))
        #print("pg_ptr=%05x" % pg_ptr)
        tb_list_ptrQ[k] = (tb_ptr_start + pg_ptr)


    print('tb_ptr_start: %08x' % tb_ptr_start)
    #out_dict(tb_list_ptrQ, 4)

out_dict(tb_list_base_addr, 0, 'tb_list_base_addr')
out_dict(tb_ddr_size, 0, 'tb_ddr_size')
out_dict(tb_list_ptrQ, 0, 'tb_list_ptrQ')
