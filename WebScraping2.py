import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.cricketbetting.net/betting-tips-and-prediction')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# find all the anchor tags with "href"
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
    # print(link.get('href'))

ipl_links = [i for i in links if 'ipl' in i and 'dream' not in i if '-vs-' in i]

for url in ipl_links:
    r1 = requests.get(url)
    # Parsing the HTML
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    # print(soup1.prettify())

    s1 = soup1.find('div', class_='predictionwon')
    text = s1.find_all('p')[0].text
    prediction = [i for i in url.split('/') if '-vs-' in i][0] + ":" + text
    print(prediction)

# are favorites to win