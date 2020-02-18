import feedparser
import formatV1
from formatV1 import Color
import winsound
import ticker_finder

urls = {
    "https://www.cnet.com/rss/news/": "",
    "https://www.statnews.com/category/adams-take/feed/": "",
    "http://rss.cnn.com/rss/cnn_health.rss": "",
    "https://developer.uspto.gov/ptab-feed/notifications.rss": ""
}


def cnetNews():
    headlines = feedparser.parse(
        "https://www.cnet.com/rss/news/")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["https://www.cnet.com/rss/news/"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\pewpew.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def feuerstein():
    headlines = feedparser.parse(
        "https://www.statnews.com/category/adams-take/feed/")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["https://www.statnews.com/category/adams-take/feed/"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\chewy_roar.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def cnnhealth():
    headlines = feedparser.parse(
        "http://rss.cnn.com/rss/cnn_health.rss")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["http://rss.cnn.com/rss/cnn_health.rss"] = new
            winsound.Beep(2020, 1000)
    except IndexError:
        pass


def ptab():
    headlines = feedparser.parse(
        "https://developer.uspto.gov/ptab-feed/notifications.rss")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(headlines.entries[0].author)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + Color.YELLOW + headlines.entries[0].author + Color.END)
            print("\t" + headlines.entries[0].summary)
            urls["https://developer.uspto.gov/ptab-feed/notifications.rss"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\Twitter.wav', winsound.SND_FILENAME)
    except IndexError:
        pass
