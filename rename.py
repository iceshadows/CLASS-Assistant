import os
import xlrd
data = xlrd.open_workbook('namelist.xlsx')
table = data.sheets()[0]
rows = table.nrows
dir = 'd:/DCIM/'
if os.path.exists(dir):
    dies = os.listdir(dir)
    temp = 3
    for diec in dies:
        row = temp -1
        houzhui = os.path.splitext(diec)[-1]
        idnum = table.cell(row,0).value
        name = table.cell(row,1).value
        filename =dir+str(int(table.cell(row,2).value))+houzhui
        textname = idnum+'_'+name+houzhui
        os.rename(filename,textname)
        temp=temp+1
    # return 0
else:
    print ("dir not exists")