import bs4
example_file = open('web_scraping/example.html')
example_soup = bs4.BeautifulSoup(example_file.read(), 'html.parser')
elems = example_soup.select('#author')
print(type(elems))
print(len(elems))
print(elems[0].attrs)
print(elems[0].getText())
