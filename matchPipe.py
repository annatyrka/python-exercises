import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search("Batman and Tina Fey")
mo2 = heroRegex.search("Batman Tina Fey")

print(mo1.group())
print(mo2.group())
