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
    print(groups)
