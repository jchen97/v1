import requests
from bs4 import BeautifulSoup
import random
import formatV1
import winsound
import ticker_finder
import time

articles = {}
count = 0

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 YaBrowser/18.3.1.1232 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
]

url = "https://hindenburgresearch.com/"

headlines = []


def hindenburg():
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"

    soup = BeautifulSoup(r.content, 'html.parser')
    theTitle = soup.find_all('h1')[0].get_text()

    if theTitle not in headlines:
        headlines.append(theTitle)
        ticker = ticker_finder.find_ticker(theTitle)
        formatV1.website_printout(theTitle, ticker, url)
        print("\t")
        winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\multigunshots.wav', winsound.SND_FILENAME)

    # time.sleep(5)