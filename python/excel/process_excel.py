import xlwt
import xlrd
filename = xlwt.Workbook()
sheet=filename.add_sheet("xg766-PVS")
sheet.write(0, 0, 'Device Name')
sheet.write(0, 1, 'Index')
sheet.write(0, 2, 'SNUM')
filename.save("xg766_pvs.xls")




file2open = 'xg766_pvs.xls'
d = xlrd.open_workbook(file2open)

sheet = d.sheet_by_name('xg766-PVS')

value =  sheet.cell_value(0, 1).encode('utf-8')
print(value)
