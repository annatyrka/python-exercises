# strip() reemoves spaces at the beginning and at the end of the string
# txt.strip(".,a") - optional parameters - a set of characters to be removed

import re
import pyperclip


strip_regex = re.compile(r'\S.+\S')


def strip_regex_version():
    txt = pyperclip.paste()
    mo = strip_regex.search(txt)
    if not mo:
        print("No matches found")
    else:
        print(mo.group())
        pyperclip.copy(mo.group())


strip_regex_version()
