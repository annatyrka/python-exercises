import csv
import os

os.chdir('/Users/annatyrka/PythonPractice/CSV/Headers')
os.makedirs('Header_Removed', exist_ok=True)

# Loop through every file oin the cwd:

for csv_file in os.listdir('.'):
    if not csv_file.endswith('.csv'):
        continue

    print(f"Removing headers from {csv_file}...")

    csv_rows = []
    current_file = open(csv_file)
    csv_reader = csv.reader(current_file)
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue    # skip first row
        csv_rows.append(row)
    current_file.close()

    # Write out the CSV file

    new_file = open(os.path.join('Header_Removed', csv_file), 'w')
    file_writer = csv.writer(new_file)
    for row in csv_rows:
        file_writer.writerow(row)
    new_file.close()
