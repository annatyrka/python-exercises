# https://www.google.com/maps/place/your_address_strinf

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.co.uk/maps/place/' + address)
