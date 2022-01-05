import csv
import os
# PyPDF2.PdfFileReader(obj_file)
os.chdir('CSV')
print(os.getcwd())

example_file = open('example.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data)
