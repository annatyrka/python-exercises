# Searching for product on Amazon and opening up tp 5 items in a separate tab

import sys
import webbrowser
import bs4
import requests

# https://www.amazon.co.uk/s?k=pillow

res = requests.get("https://www.amazon.co.uk/s?k=" + " ".join(sys.argv[1:]))
print(res.raise_for_status())
print("Searching...")

elem = bs4.BeautifulSoup(res.text, 'html.parser')
elem_items = elem.select("data-uuid")

for i in range(min(5, len(elem_items))):
    url_to_open = "opening https://www.amazon.co.uk/s?k=" + \
        elem_items[i].get('data-uuid')
    print(url_to_open)
    webbrowser.open(url_to_open)
