from datetime import datetime


class Color:
    PURPLE = '\033[95m'
    LTCYAN = '\033[96m'
    LTBLUE = '\033[94m'
    LTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LTRED = '\033[91m'
    BLACK = '\033[30m'
    BLUE = '\033[34m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def rss_printout(headlines, ticker, num):
    dateTimeObj = datetime.now()
    timeObj = dateTimeObj.time()

    # find keywords
    # keyword_search.filter(headlines)
    # should return

    print(Color.BLACK + "-" * 99 + Color.END)
    print("\n")
    print(headlines.entries[num].published + "//   " + Color.UNDERLINE + headlines.feed.title + Color.END
          + "....." + headlines.entries[num].link)
    print("\n")
    print(
        timeObj.strftime("%H:%M:%S")
        + "....." + Color.LTBLUE + ticker + Color.END
        + "....." + Color.YELLOW + headlines.entries[num].title + Color.END
    )
    print("\n")


def website_printout(headline, ticker, url):
    dateTimeObj = datetime.now()
    timeObj = dateTimeObj.time()

    print(Color.BLACK + "-" * 99 + Color.END)
    print("\n")
    print("xxx, xx xxx 2020 xx:xx:xx GMT" + "//   " + Color.UNDERLINE + headline + Color.END
          + "....." + url)
    print("\n")
    print(
        timeObj.strftime("%H:%M:%S")
        + "....." + Color.LTBLUE + ticker + Color.END
        + "....." + Color.YELLOW + headline + Color.END
    )
    print("\n")
    pass
