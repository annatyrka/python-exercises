
import os
from pathlib import Path
import send2trash

#import send2trash
#shutil.copy(p/'PythonPractice/spam.txt', p/'PythonPractice'/'test/spam2.txt')

#shutil.copytree(p/'PythonPractice/test/', p/'PythonPractice/ecommerce/')

#shutil.move(p/'PythonPractice/regex_search2.py', p/'PythonPractice/testing')
bacon_file = open('bacon.txt', 'a')

bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()
sendtotrash.sen2trash('bacon.txt')
