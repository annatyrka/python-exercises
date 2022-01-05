import pyperclip
import re

# Create phone regex
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )''', re.VERBOSE)

# Create email regex
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username
    @
    [a-zA-Z0-9.]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8]
