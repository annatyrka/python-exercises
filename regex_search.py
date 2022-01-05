from pathlib import Path
import re


folder = Path('/Users/annatyrka/PythonPractice/')
txt_files = list(folder.glob('*.txt'))
pattern = input("What are you looking for? ")
pattern_regex = re.compile(pattern)
for txt_file in txt_files:
    # print(txt_file)
    file_object = open((txt_file), 'r')
    found_pattern = pattern_regex.findall(file_object.read())
    print(f"{txt_file}: found patterns: {found_pattern}")
