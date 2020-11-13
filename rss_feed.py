import feedparser
import formatV1
from formatV1 import Color
import winsound
import ticker_finder

urls = {
    "https://www.ftc.gov/feeds/press-release.xml": "",
    "https://nypost.com/feed/": "",
    "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/press-releases/rss.xml": ""
}


def ftcprl():
    headlines = feedparser.parse(
        "https://www.ftc.gov/feeds/press-release.xml")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t")
            urls["https://www.ftc.gov/feeds/press-release.xml"] = new
            winsound.Beep(2020, 1000)
    except IndexError:
        pass


def nypmain():
    headlines = feedparser.parse(
        "https://nypost.com/feed/")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + Color.YELLOW + headlines.entries[0].author + Color.END)
            print("\t" + headlines.entries[0].summary)
            urls["https://nypost.com/feed/"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\blip.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def fdaprl():
    headlines = feedparser.parse(
        "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/press-releases/rss.xml")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/press-releases/rss.xml"] = new
            winsound.Beep(1997, 1000)
    except IndexError:
        pass


# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)
