import requests
from bs4 import BeautifulSoup
import random
import formatV1
import winsound
import ticker_finder
from datetime import datetime

articles = {}
count = 0

user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # Firefox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

url = "https://citronresearch.com/"

headlines = []


def citron(session):
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    try:
        r = session.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"

    soup = BeautifulSoup(r.content, 'html.parser')

    citronTitle0 = soup.find_all('h2')[0].get_text()

    try:
        citronTitle1 = soup.find_all('h1')[0].get_text()
    except IndexError:
        citronTitle1 = "----------"

    try:
        citronTitle2 = soup.find_all('h1')[1].get_text()
    except IndexError:
        citronTitle2 = "----------"

    try:
        citronTitle3 = soup.find_all('h2')[1].get_text()
    except IndexError:
        citronTitle3 = "----------"

    try:
        citronTitle4 = soup.find_all('h2')[2].get_text()
    except IndexError:
        citronTitle4 = "----------"
    # prev = soup.find_all('h2')[1].get_text()
    # next = soup.find_all('h2')[2].get_text()

    if citronTitle1 not in headlines:
        dateTimeObj = datetime.now()
        timeObj = dateTimeObj.time()
        headlines.append(citronTitle1)
        ticker = ticker_finder.find_ticker(citronTitle1)
        print("-" * 99)
        print()
        print()
        print(timeObj.strftime("%H:%M:%S") + "     CITRON")
        # print("\t")
        # print(ticker)
        print(citronTitle0)
        print(citronTitle1)
        print(citronTitle2)
        print(citronTitle3)
        print(citronTitle4)
        print("\t")
        winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\multigunshots.wav', winsound.SND_FILENAME)


def citrontest():
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"

    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.get_text)
