import ezsheets

ss = ezsheets.Spreadsheet('1sCSXQRPfkKerIlNKNUnQY4qdzjWRzoTvejU4_r2IVUU')

print(ss.title)
# ss.title = 'Python new'  # change the title
print(ss.spreadsheetId)
print(ss.url)
print(ss.sheetTitles)
print(ss.sheets)
# ss.downloadAsExcel('new_excel.xlsx')
sheet = ss[0]
print(sheet['A1'])
print(sheet['A2'])
print(sheet[1, 2])

# gs = ezsheets.upload('excel/multiplication.xlsx')
# print(ezsheets.listSpreadsheets())
