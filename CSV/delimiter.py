import csv

csv_file = open('CSV/example.tsv', 'w')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
csv_writer.writerow(['1', '2', '3'])
csv_writer.writerow(['4', '5', '6'])
csv_file.close()
