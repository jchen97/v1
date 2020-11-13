import time

import requests
from bs4 import BeautifulSoup
import winsound
import ticker_finder

articles = {}
count = 0


def info():

    r = requests.get("https://www.theinformation.com/briefings")
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.content)
    print(soup.find_all('a'))


def info_articles():

    r = requests.get("https://www.theinformation.com/articles")
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.content)
    print(soup.find_all('a'))
    # time.sleep(5)
