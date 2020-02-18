import feedparser
import formatV1
import winsound
import ticker_finder

articles = {}
count = 0


def verge():
    headlines = feedparser.parse(
        "https://www.theverge.com/rss/index.xml")
    try:
        global count
        new = headlines.entries[0].title
        if new not in articles.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            articles[count] = new
            count += 1
            print(count)
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\pewpew.wav', winsound.SND_FILENAME)
    except IndexError:
        pass
