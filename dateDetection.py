# DD/MM/YYYY
# days: {1,31}, months: {01,12}, years: {1000,2999}

import re
import pyperclip
# [('12','12','2020'),('13','05','2020')] one string for each group
date_regex = re.compile(r'([0-9]{2})/([0-9]{2})/([0-9]{4})')
txt = pyperclip.paste()

matches = []
days = []
months = []
years = []

for groups in date_regex.findall(txt):
    if 0 < int(groups[0]) < 32 and 0 < int(groups[1]) < 12 and 999 < int(groups[2]) < 3000:
        matches.append("/".join([groups[0], groups[1], groups[2]]))
        days.append(groups[0])
        months.append(groups[1])
        years.append(groups[2])

# 04, 06, 09, 11 - 30 days
# 01, 03, 05, 07, 08, 10, 12 - 31 days
# 02 - 28 days
# 02 - 29 days: if year % 4 ==0 and not year % 00 ==0

days_30 = ['04', '06', '09', '11']
days_31 = ['01', '03', '05', '07', '08', '10', '12']

for i in range(len(months)):
    if months[i] in days_30:
        if int(days[i]) > 30:
            print("Wrong date for month " + months[i])
    if months[i] in days_31:
        if int(days[i]) > 31:
            print("Wrong date for month" + month[i])
    if months[i] == '02':
        if int(years[i]) % 4 == 0 and not int(years[i]) % 400 == 0:
            if int(days[i]) > 29:
                print("Wrong date for February")
        elif int(days[i]) > 28:
            print("Wrong date for February")

'''
for groups in date_regex.findall(txt):
    dates = "/".join([groups[0], groups[1], groups[2]])
    if 0 < int(groups[0]) < 32:
        day = " ".join([groups[0]])
    if 0 < int(groups[1]) < 12:
        month = " ".join([groups[1]])
    if 999 < int(groups[2]) < 3000:
        year = " ".join([groups[2]])
    matches.append(dates)
    days.append(day)
    months.append(month)
    years.append(year)
    '''


print(matches, days, months, years, end=" ")
print("")
