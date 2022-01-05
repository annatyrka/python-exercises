import pyinputplus as pyip

#response = pyip.inputNum()

#response2 = input('Enter a number: ')

response3 = pyip.inputNum('Enter num: ', blank=True)
response4 = pyip.inputNum('Enter num: ', min=4, lessThan=8)
response5 = pyip.inputNum('Enter num: ', timeout=10)
help(pyip.inputChoice)
