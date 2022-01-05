import csv

output_file = open('CSV/output.csv', 'w', newline="")
output_writer = csv.writer(output_file)
output_writer.writerow(['I', 'am', 'worth', 'it'])
output_writer.writerow(['I', 'will', 'make', 'it'])
output_file.close()
