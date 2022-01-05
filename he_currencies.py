import requests
import bs4
import pprint

res = requests.get('website')
res.raise_for_status()

from_USD = bs4.BeautifulSoup(res.text, 'html.parser')
from_USD_soup = from_USD.select('#historicalRateTbl')
print(from_USD_soup[0].getText())
