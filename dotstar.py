import re

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)', re.DOTALL)
mo = name_regex.search("First Name: Anna\n Last Name: Tyrka")
print(mo.group(1))
print(mo.group(2))
