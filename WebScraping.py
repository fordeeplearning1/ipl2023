import requests
from bs4 import BeautifulSoup

sites = ['https://www.crictracker.com/cricket-match-predictions/', 'https://www.cricketbetting.net/betting-tips-and-prediction']

for site in sites:
    # Making a GET request
    r = requests.get(site)

    # check status code for response received
    # success code - 200
    # print(r)
    print(site)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # find all the anchor tags with "href"
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
        # print(link.get('href'))

    if site == 'https://www.crictracker.com/cricket-match-predictions/':
        ipl_links = [i for i in links if 'ipl-2023' in i if 'match-prediction-' in i]
    if site == 'https://www.cricketbetting.net/betting-tips-and-prediction':
        ipl_links = [i for i in links if 'ipl' in i and 'dream' not in i if '-vs-' in i]

    ipl_links_unique = list(dict.fromkeys(ipl_links))

    for url in ipl_links_unique:
        if site == 'https://www.crictracker.com/cricket-match-predictions/':
            r1 = requests.get('https://www.crictracker.com' + url)
        if site == 'https://www.cricketbetting.net/betting-tips-and-prediction':
            r1 = requests.get(url)
        # Parsing the HTML
        soup1 = BeautifulSoup(r1.content, 'html.parser')
        # print(soup1.prettify())
        if site == 'https://www.crictracker.com/cricket-match-predictions/':
            s1 = soup1.text.split('Match Prediction')[-1].split('\n')[0]
            # s2 = [i.text for i in s1 if "Prediction" in i.text]
            prediction = [i for i in url.split('/') if '-vs-' in i if 'match-prediction'][0] + "-" + s1
        if site == 'https://www.cricketbetting.net/betting-tips-and-prediction':
            s1 = soup1.find('div', class_='predictionwon')
            text = s1.find_all('p')[0].text
            prediction = [i for i in url.split('/') if '-vs-' in i][0] + ":" + text
        print(prediction)
