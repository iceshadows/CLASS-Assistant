import xlrd
data = xlrd.open_workbook('namelist.xlsx')
table = data.sheets()[0]
rows = table.nrows
print(rows)
for row in range(rows):
    # print(row)
    idnum = table.cell(row,0).value
    name = table.cell(row,1).value
    print(name +''+idnum)