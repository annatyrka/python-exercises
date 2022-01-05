import csv

example_file = open('CSV/example.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
    print(f"Row #{example_reader.line_num} {row}")
