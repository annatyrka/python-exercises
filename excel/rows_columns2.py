import openpyxl

wb = openpyxl.load_workbook('excel/example.xlsx')

sheet = wb.active
print(list(sheet.columns)[0])
print(list(sheet.rows)[0])
