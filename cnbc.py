import feedparser
import formatV1
import winsound
import ticker_finder
from collections import deque

urls = {
    "https://www.cnbc.com/id/15837362/device/rss/rss.html": "us",
    "https://www.cnbc.com/id/19832390/device/rss/rss.html": "eu",
    "https://www.cnbc.com/id/19794221/device/rss/rss.html": "as",
    "https://www.cnbc.com/id/100003114/device/rss/rss.html": "main",
    "https://www.cnbc.com/id/10001147/device/rss/rss.html": "bus",
    "https://www.cnbc.com/id/19854910/device/rss/rss.html": "tech"
}

#currently unused...need to transition
q = deque()

articles = {}

count = 0

# implementation idea:
# scrape multiple/many headlines per rss feed, by checking multiple "new"'s (headline titles) in the url values
# instead of replacing the last url, ADD more dict entries to make a collection of all cnbc articles


def fill():
    global count
    for key in urls:
        headlines = feedparser.parse(key)
        for i in range(0, 10):
            new = headlines.entries[i].title

            # figure out a way to remove once the q gets too big
            if new not in q:
                q.append(new)


def cnbcMain():
    headlines = feedparser.parse(
        "https://www.cnbc.com/id/100003114/device/rss/rss.html")
    global count
    try:
        new = headlines.entries[0].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\cnbcchime.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def cnbcUS():
    headlines = feedparser.parse(
        "https://www.cnbc.com/id/15837362/device/rss/rss.html")
    global count
    try:
        new = headlines.entries[0].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\cnbcchime.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def cnbcEU():
    headlines = feedparser.parse(
        "https://www.cnbc.com/id/19832390/device/rss/rss.html")
    global count
    try:
        new = headlines.entries[0].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\cnbcchime.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def cnbcAS():
    headlines = feedparser.parse(
        "https://www.cnbc.com/id/19794221/device/rss/rss.html")
    global count
    try:
        new = headlines.entries[0].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\cnbcchime.wav', winsound.SND_FILENAME)
    except IndexError:
        pass
