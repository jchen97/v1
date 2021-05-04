import csv
import newspaper

good_news = set()
bad_news = set()
stock_offering = set()
mna = set()

def initiate():
    with open('keywords.csv', 'r') as wordfile:
        reader = csv.reader(wordfile)

        for row in reader:
            mna.add(row[0].lower())
            stock_offering.add(row[1].lower())
            good_news.add(row[2].lower())
            bad_news.add(row[3].lower())

        good_news.discard('')
        bad_news.discard('')
        stock_offering.discard('')
        mna.discard('')

    print(good_news)
    print(bad_news)
    print(stock_offering)
    print(mna)

def filterit(headline, ticker):
    return True
