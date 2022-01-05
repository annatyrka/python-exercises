import sys
import pyperclip

"""
List of animals
List of aquarium life
List of biologists by author abbreviation
Lists of cultivars
"""

text = pyperclip.paste()
lines = text.split("\n")
for item in range(len(lines)):
    lines[item] = "* " + lines[item]
text = "\n".join(lines)

(pyperclip.copy(text))
