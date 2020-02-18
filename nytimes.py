import feedparser
import formatV1
import winsound
import ticker_finder

articles = {}
count = 0


def nytus():
    global count
    headlines = feedparser.parse(
        "https://rss.nytimes.com/services/xml/rss/nyt/US.xml")
    try:
        new = headlines.entries[5].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 5)
            print("\t" + headlines.entries[5].summary)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\blaster-firing.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def nyttech():
    global count
    headlines = feedparser.parse(
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml")
    try:
        new = headlines.entries[4].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 4)
            print("\t" + headlines.entries[4].summary)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\blaster-firing.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def nytbus():
    global count
    headlines = feedparser.parse(
        "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml")
    try:
        new = headlines.entries[9].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 9)
            print("\t" + headlines.entries[9].summary)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\blaster-firing.wav', winsound.SND_FILENAME)
    except IndexError:
        pass