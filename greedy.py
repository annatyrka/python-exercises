import re

greedyhaRegex = re.compile(r'(Ha){3,5}')
mo = greedyhaRegex.search("HaHaHaHa")
print(mo.group())

non_greedyhaRegex = re.compile(r'(Ha){3,5}?')
mo1 = non_greedyhaRegex.search("HaHaHaHa")
print(mo1.group())

# {}? - non-greedy match
# ()? - optional group
