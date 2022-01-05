"""
1. Get the text from the clipboard.
2. Find all phone numbers and emails in the text.
3. Paste them onto the clipboard.
"""

import re
import pyperclip
# Regex for matching phones. 000-000-0000

phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)                       # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2-5})?    # extension
)""", re.VERBOSE)

# Regex for matching emails. firstlast@gmail.com
email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)""", re.VERBOSE)

# Find matches in clipboard text.
txt = str(pyperclip.paste())

# Find all matches
matches = []
for groups in phone_regex.findall(txt):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_num += " x" + groups[8]
        matches.append(phone_num)

for groups in email_regex.findall(txt):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard\:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found")
