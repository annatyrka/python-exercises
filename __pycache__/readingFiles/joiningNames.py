# forward slash (/) - path separator on Mac and Linux
# the / operator that we normalluy use for division can also combine Path objects and strings

from pathlib import Path
import os
my_files = ['accounts.txt', 'setails.csv', 'invite.docx']
for file_name in my_files:
    print(Path(r'C:/Users/AT', file_name))

print(Path('spam') / 'bacon' / 'eggs')
print(Path.cwd())
print(Path.home())
