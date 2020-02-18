import feedparser
import formatV1
import winsound
import ticker_finder

urls = {
    "https://www.multichannel.com/.rss/full/": "",
    "https://tools.cdc.gov/api/v2/resources/media/132608.rss": ""
}


def multichannel():
    headlines = feedparser.parse(
        "https://www.multichannel.com/.rss/full/")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["https://www.multichannel.com/.rss/full/"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\pewpew.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def cdc():
    headlines = feedparser.parse(
        "https://tools.cdc.gov/api/v2/resources/media/132608.rss")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["https://tools.cdc.gov/api/v2/resources/media/132608.rss"] = new
            winsound.Beep(2500, 1000)
    except IndexError:
        pass
