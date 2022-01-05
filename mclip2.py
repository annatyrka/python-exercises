import sys
import pyperclip

TEXT = {"Approved": "Thank you for providing requested info. Your submission has been approved.",
        "Declined": "The information provided is insufficient. Please make necessary updates"}

# sys.argv - where the commend line arguments are stored, first item file name

if len(sys.argv) < 2:
    print("You have not provided the keyword")

keyphrase = sys.argv[1]
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " has been copied to clipboard.")
else:
    print("Text not found in TEXT")
