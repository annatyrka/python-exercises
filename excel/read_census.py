import openpyxl
import pprint

print('Opening workbook...')
census_wb = openpyxl.load_workbook('excel/censuspopdata.xlsx')
sheet = census_wb.active
county_data = {}

# Fill in county_data with each county's population and tracts.
print('Reading rows...')

for row in range(2, sheet.max_row+1):
    # Each row has data for one census tract.

    state = sheet['B'+str(row)].value
    county = sheet['C' + str(row)].value
    population = sheet['D' + str(row)].value

    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts': 0, 'population': 0})

    # Each row represents one census tract, so increment by one.
    county_data[state][county]['tracts'] += 1

    # Increase the county pop by the pop in census tract.
    county_data[state][county]['population'] += int(population)

# Open a new text file and write the contents of county_data to it.
print('Writing results...')

result_file = open('excel/cencus2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('Done')
