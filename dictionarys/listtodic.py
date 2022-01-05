import os
from pathlib import Path


# os.makedirs('test/test')
# Path.cwd()
# print(Path.cwd().is_absolute())
# print(Path('PythonPractice/test/test').is_absolute())
# rint(os.path.abspath('PythonPractice/test/test'))
# p = Path('/Users/annatyrka/PythonPractice')
# print(p.parent)
# for pyfile in p.glob('*'):
# print(pyfile)
"""
a = Path('spam.txt')
a.write_text("Hello, world!")
print(a.read_text())

text = Path('/Users/annatyrka/PythonPractice/spam.txt')
with open(text, 'a') as spam:
    spam.write("\nI'm still learning")

print(text.read_text())

print(Path('spam', 'bacon', 'eggs'))
print(Path.home())
"""
# os.chdir('/Users/annatyrka/PythonPractice/dictionarys/')
print(Path.cwd())
print(Path.home())
print(os.path.abspath('listtodic.py'))
print(os.path.split('/Users/annatyrka/PythonPractice/dictionarys/listtodic.py'))

p = Path('/Users/annatyrka/PythonPractice/InputValidation')
print(list(p.glob('*')))
