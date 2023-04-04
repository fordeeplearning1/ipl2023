import requests
from bs4 import BeautifulSoup
import pandas as pd

# Making a GET request
r = requests.get('https://www.crictracker.com/cricket-match-predictions/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# find all the anchor tags with "href"
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
    # print(link.get('href'))

ipl_links = [i for i in links if 'ipl-2023' in i]
# ipl_links[0]

# ipl_links_unique = list(set(ipl_links))
ipl_links_unique = list(dict.fromkeys(ipl_links))

for url in ipl_links_unique:
    r1 = requests.get('https://www.crictracker.com' + url)
    # Parsing the HTML
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    # print(soup1.prettify())

    # s1 = soup1.find_all('h3')
    s1 = soup1.text.split('Match Prediction')[-1].split('\n')[0]
    # s2 = [i.text for i in s1 if "Prediction" in i.text]
    prediction = [i for i in url.split('/') if '-vs-' in i][0] + "-" + s1
    print(prediction)
# "Today's Match Prediction:"
