#! python3
# mcb.pyw - saves and loads pieces of text to the clipboard
# Usage: mcb.pyw save <keyword> - Saves clipboard to keyword
#        mcb.pyw <keyword> - Loads keyword to clipboard
#        mcb.pyw list - Loads all keywords to clipboard
#        mcb.pyw delete - deletes <keword>
#        mcb.pyw delete - deletes all keywords


import sys
import shelve
import pyperclip

mcb_shelf = shelve.open('mcb')
print(type(mcb_shelf))
if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcb_shelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        print(list(mcb_shelf.keys()))
    if sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print(
            f"Text for keyword {sys.argv[1]} copied to clipboard")
# print(mcb_shelf['package'])
mcb_shelf.close()
