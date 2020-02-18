import csv

good_news = []
bad_news = []
stock_offering = []


def initiate():
    with open('keywords.csv', 'r') as wordfile:
        reader = csv.reader(wordfile)

        for row in reader:
            stock_offering.append(row[1].lower())
            good_news.append(row[2].lower())
            bad_news.append(row[3].lower())


def filterit(headline, ticker):
    pass


initiate()
