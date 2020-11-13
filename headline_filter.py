import csv
import newspaper

good_news = set()
bad_news = set()
stock_offering = set()


def initiate():
    with open('keywords.csv', 'r') as wordfile:
        reader = csv.reader(wordfile)

        for row in reader:
            stock_offering.add(row[1].lower())
            good_news.add(row[2].lower())
            bad_news.add(row[3].lower())

        good_news.discard('')
        bad_news.discard('')
        stock_offering.discard('')

    print(good_news)
    print(bad_news)
    print(stock_offering)


def filterit(headline, ticker):
    pass
