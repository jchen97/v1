import feedparser
import formatV1
from formatV1 import Color
import winsound
import ticker_finder
import headline_filter

urls = {
    "https://www.ftc.gov/feeds/press-release.xml": "",
    "https://nypost.com/feed/": "",
    "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/press-releases/rss.xml": "",
    "https://www.zer0es.tv/category/big-announcements/feed/": "",
    "https://insideevs.com/rss/news/all/": "",
    "https://techcrunch.com/feed/": ""
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
            if headline_filter.filterit(new, ticker):
                formatV1.rss_printout(headlines, ticker, 0)
                print("\t" + Color.YELLOW + headlines.entries[0].author + Color.END)
                print("\t" + headlines.entries[0].summary)
                urls["https://nypost.com/feed/"] = new
                # winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\blip.wav', winsound.SND_FILENAME)
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


def zerotv():
    headlines = feedparser.parse(
        "https://www.zer0es.tv/category/big-announcements/feed/")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["https://www.zer0es.tv/category/big-announcements/feed/"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\gun_44mag_11.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def insideev():
    headlines = feedparser.parse(
        "https://insideevs.com/rss/news/all/")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            formatV1.rss_printout(headlines, ticker, 0)
            print("\t" + headlines.entries[0].summary)
            urls["https://insideevs.com/rss/news/all/"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\electricshock.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


def techcrunch():
    headlines = feedparser.parse(
        "https://techcrunch.com/feed/")
    try:
        new = headlines.entries[0].title
        if new not in urls.values():

            ticker = ticker_finder.find_ticker(new)

            formatV1.rss_printout(headlines, ticker, 0)

            urls["https://techcrunch.com/feed/"] = new
            winsound.PlaySound(r'C:\Users\Trader\Documents\WavSounds\electricshock.wav', winsound.SND_FILENAME)
    except IndexError:
        pass


# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)
