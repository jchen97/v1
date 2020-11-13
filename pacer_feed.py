import feedparser
import formatV1
from formatV1 import Color
import winsound
import ticker_finder

urls = {
    "https://ecf.ded.uscourts.gov/cgi-bin/rss_outside.pl": "Biogen",
    "": ""
}

# open slot


def courtA():
    link = ""
    target = ""
    headlines = feedparser.parse(link)
    try:
        new = headlines.entries[0].title
        if new not in urls.values():
            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls[link] = new

            if target in new:
                print("\t" + "!!!" + Color.LTRED + ("<BIOGEN>" * 10) + Color.END + "!!!")
                winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\boxing_bell_multiple.wav', winsound.SND_FILENAME)
            else:
                winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\bloop_x.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def courtB():
    link = "https://ecf.ded.uscourts.gov/cgi-bin/rss_outside.pl"
    target = "Biogen"
    headlines = feedparser.parse(link)
    try:
        new = headlines.entries[0].title
        if new not in urls.values():
            ticker = ticker_finder.find_ticker(new)

            # Detects relevant keywords. Returns a string that may or may not be modified>
            # new = keyword_search.detect(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls[link] = new

            if target in new:
                print("\t" + "!!!" + Color.LTRED + ("<BIOGEN>" * 10) + Color.END + "!!!")
                winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\boxing_bell_multiple.wav', winsound.SND_FILENAME)
            else:
                winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\bloop_x.wav', winsound.SND_FILENAME)
    except IndexError:
        pass
