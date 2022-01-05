import re

# Passing a string value to reperenting your regular expression to re.compile()
# return a Regex pattern object (or simply, a Regex object).

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Now the phoneNumRegex variable contains a Regex object

mo = phoneNumRegex.search("My number is 415-555-4242.")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
