# at least 8 characters long
# both uppercase and lowercase cahracters
# at least one digit

import re

password_regex = re.compile(r'''(
((?=.*[A-Z])    # at least one capital letter
(?=.*[a-z])      # at least one lowercase letter
(?=.*[0-9])      # at least one digit
).{8,}           # at least 8 characters in total
)''', re.VERBOSE)

#password_test = password_regex.search("aAnANNN9")
#print('The passowrd is ' + password_test.group())


def password_check():
    ppass = input("Enter password: ")
    mo = password_regex.search(ppass)
    if not mo:
        print("Not strong, bling blong")
    else:
        print("Long and strong")


password_check()
