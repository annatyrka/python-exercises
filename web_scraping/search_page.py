# https://pypi.org/search/?q=pdf
# Opens several search results

import webbrowser
import requests
import bs4
import sys

print("Searching...")

res = requests.get("http://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
print(res.raise_for_status())

# Retrieve top search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result
link_elems = soup.select('.package-snippet')

# Open a browser tab for each result
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print(url_to_open)
    webbrowser.open(url_to_open)
