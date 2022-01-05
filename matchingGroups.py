import re
heroRegex = re.compile(r'Batman|Tina')
mo = heroRegex.search('Batman and Tina')
print(mo.group())
