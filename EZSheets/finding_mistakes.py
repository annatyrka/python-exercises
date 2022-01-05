import ezsheets

gs = ezsheets.Spreadsheet('Bean Count')
sheet = gs[0]

for i in range(2, 15002):
    if int(sheet.getRow(i)[0]) * int(sheet.getRow(i)[1]) == int(sheet.getRow(i)[2]):
        continue
    else:
        print("Row %s has inncorect data" % i)
