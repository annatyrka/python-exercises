import ezsheets

gs = ezsheets.Spreadsheet('Form responses')

emails = []

sheet = gs[0]

for i in range(1, sheet.rowCount+1):
    if sheet['A' + str(i)] not in emails:
        emails.append(sheet['A'+str(i)])
print(emails)
