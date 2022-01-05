import random
from pathlib import Path
import os

print(random.random())

print(random.randint(1, 4))
p = Path('test/spam.txt')
print(os.path)
print(os.path.abspath(p))
