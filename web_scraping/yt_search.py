# YouTube search

import sys
import requests
import webbrowser
import bs4

res = requests.get(
    "https://www.youtube.com/results?search_query=philippines")
print(res.raise_for_status())
print("Searching...")
with open('web_scraping/you_tube.html', 'wb') as yt:
    for chunk in res.iter_content(100000):
        yt.write(chunk)
yt_soup = bs4.BeautifulSoup(res.text, "html.parser")
yt_elems = yt_soup.select("what should go here")
print(yt_elems[:10])

for i in range(min(5, len(yt_elems))):
    video_to_open = "https://www.youtube.com/" + yt_elems[i].get('href')
    print(video_to_open)
    # webbrowser.open(video_to_open)
