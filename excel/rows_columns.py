import openpyxl

wb = openpyxl.load_workbook('excel/example.xlsx')
sheet = wb['Sheet1']

print(tuple(sheet['A1':'C3']))
print("")
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
