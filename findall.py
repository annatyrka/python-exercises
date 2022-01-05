# search() - returns a Match object of the first matched text
# findall() - returns every match in the searched string

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-444-2222 Work: 415-454-3333')
print(mo.group())
mo2 = phoneNumRegex.findall('Cell: 415-444-2222 Work: 415-454-3333')
print(mo2)  # Returns a list
