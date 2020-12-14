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
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
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

    try:
        citronTitle0 = soup.find_all('h2')[0].get_text()
    except IndexError:
        citronTitle0 = soup.find_all('h2')[0].get_text()

    try:
        citronTitle1 = soup.find_all('h2')[1].get_text()
    except IndexError:
        citronTitle1 = soup.find_all('h2')[0].get_text()

    try:
        citronTitle2 = soup.find_all('h2')[2].get_text()
    except IndexError:
        citronTitle2 = soup.find_all('h2')[0].get_text()
    # prev = soup.find_all('h2')[1].get_text()
    # next = soup.find_all('h2')[2].get_text()

    if citronTitle0 not in headlines:
        dateTimeObj = datetime.now()
        timeObj = dateTimeObj.time()
        headlines.append(citronTitle0)
        ticker = ticker_finder.find_ticker(citronTitle0)
        print("-" * 99)
        print()
        print()
        print(timeObj.strftime("%H:%M:%S") + "     CITRON")
        print("\t")
        print(ticker)
        print(citronTitle0)
        print(citronTitle1)
        print(citronTitle2)
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
