import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'

sheet.merge_cells('C2:C4')
sheet['C2'] = 'Three cells merged'

# Set the height nad width:

sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20
wb.save('excel/dimensions.xlsx')
