import bs4

example_file = open('web_scraping/example.html')
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
p_elems = example_soup.select('p')

print(p_elems)
print(len(p_elems))
print(p_elems[0])
print(p_elems[1].getText())
print("")

span_elem = example_soup.select('span')[0]
print(span_elem)
print(span_elem.get('id'))
print(span_elem.attrs)
