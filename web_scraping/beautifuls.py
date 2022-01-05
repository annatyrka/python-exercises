import requests
import bs4

res = requests.get("http://nostrach.com")
res.raise_for_status()
# it returns the BeautifulSoup object
no_strach = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(no_strach))

example_file = open("web_scraping/example.html")
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
print(type(example_soup))
