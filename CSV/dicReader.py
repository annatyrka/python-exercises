import csv

example_file = open('CSV/examplewithHeader.csv')
example_DictReader = csv.DictReader(example_file)

for row in example_DictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
example_file.close()

another_file = open('CSV/example.csv')
csv_reader = csv.DictReader(another_file, ['time', 'name', 'amount'])

for row in csv_reader:
    print(row['time'], row['name'], row['amount'])
another_file.close()
