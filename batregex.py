import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = batRegex.search("Batmobile batman Batbat")
print(mo1.group())
