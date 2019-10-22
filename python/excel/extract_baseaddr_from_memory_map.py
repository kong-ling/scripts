import xlwt
import xlrd

HEADER = 1

file2open = 'PROJECT_Address_Map.xlsx'
file2write = 'PROJECT_Address_Map.txt'
d = xlrd.open_workbook(file2open)
baseaddr = open(file2write, 'w')

sheet = d.sheet_by_name('PROJECT_Address_Map')
number_of_rows =  sheet.nrows
number_of_cols =  sheet.ncols
colnames = sheet.row_values(1)
print(number_of_rows)
print(number_of_cols)
print(colnames)


SUB_SYSTEM    = colnames.index('Subsystem ')
SUB_MODULE    = colnames.index('Submodule')
SIZE_HEX      = colnames.index('Size (Hex)')
SIZE          = colnames.index('Size')
ADDRESS_START = colnames.index('Address Start (Hex)')
ADDRESS_END   = colnames.index('Address End (Hex)')
PATH          = colnames.index('path')
ESSENCE_XML   = colnames.index('Essence xml')
TARGET_NIU    = colnames.index('Target NIU Name')

interested_columns = [SUB_SYSTEM, SUB_MODULE, SIZE_HEX, SIZE, ADDRESS_START, ADDRESS_END, TARGET_NIU]
#for column in interested_columns:
#    print(column),

list = []
#for line in range(24, number_of_rows):
for line in range(24, 1068):
#for line in range(24, 50):
    value = sheet.row_values(line)
    print(line, value),
    ###for col in interested_columns:
    ###    print(value[col]),
    if value[SUB_MODULE]:
        module_name = value[SUB_MODULE].strip()
        module_name = module_name.replace(' ', '_')

        if 'Reserved' in value[SUB_MODULE]:
            pass
        else:
            #line_content = "%d, [%-s] => %s # %8s, %s%s\n" % (line+1, value[SUB_MODULE], value[ADDRESS_START], value[SIZE], value[PATH], value[ESSENCE_XML])
            #line_content = "%d, [%-s] => %s # %8s, %s%s\n" % (line+1, module_name, value[ADDRESS_START], value[SIZE], value[PATH], value[ESSENCE_XML])
            line_content = "%d, %s, 0x%s, %s, 0x%s, %s, %s\n" % (line+1, module_name, value[ADDRESS_START], value[TARGET_NIU], value[SIZE], value[PATH], value[ESSENCE_XML])
            #line_content = "%s, 0x%s\n" % (value[TARGET_NIU], value[ADDRESS_START])
            print(line_content)
            baseaddr.write(line_content)
    else:
        pass

baseaddr.close()
