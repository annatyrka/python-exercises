import csv

output_file = open('CSV/output_headers.csv', 'w')
output_DictWriter = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
output_DictWriter.writeheader()
output_DictWriter.writerow(
    {'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_DictWriter.writerow(
    {'Name': 'Ciapek', 'Pet': 'cat', 'Phone': '555-2345'})
output_DictWriter.writerow(
    {'Pet': 'dog', 'Name': 'Reksio', 'Phone': '555-3456'})
output_file.close()
