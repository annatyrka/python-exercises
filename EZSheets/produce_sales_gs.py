import ezsheets

gs = ezsheets.Spreadsheet('excel/ProduceSales')
sheet = gs[0]

print(sheet.getRow(1))

column_one = sheet.getColumn(1)
sheet.updateRow(3, ['Avocado', '2', '3'])

for i, value in enumerate(column_one):
    column_one[i] = value.upper()

sheet.updateColumn(1, column_one)
