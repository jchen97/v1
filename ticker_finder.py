import csv
from formatV1 import Color

# ticker:name string
company_ticker = {}
# ticker:corresponding sound string
tickers_sound = {}
# ticker:tuple of relevant words


relevant_words = {}
# ^^^ need to implement this
tup1 = ()


def initiate():
    global company_ticker

    with open('finviz.csv', 'r') as stockfile:
        reader = csv.reader(stockfile)
        for row in reader:
            ticker = ((4 - len(row[1])) * " ") + row[1]
            company_name = cleanup(" " + row[2].lower())

            pair = {ticker: company_name}
            company_ticker.update(pair)

    while "" in company_ticker:
        del company_ticker[""]

    print(company_ticker)


# cleans up string for company names
def cleanup(name):
    name = name.replace(" l.p.", "")
    name = name.replace(" co.", "")
    name = name.replace(" ltd", "")
    name = name.replace(" plc", "")
    name = name.replace(" llc", "")
    name = name.replace(" etf", "")
    name = name.replace(" technologies", "")

    name = name.replace(" incorporated", "")
    name = name.replace(" international corporation", "")
    name = name.replace(" corporation", "")

    name = name.replace(" holding corp.", "")
    name = name.replace(" holdings", "")
    name = name.replace(" holding", "")

    name = name.replace(" public joint stock company", "")
    name = name.replace(" public limited company", "")
    name = name.replace(" limited company", "")
    name = name.replace(" company", "")
    name = name.replace(" limited", "")
    name = name.replace(",", "")
    name = name.replace(".", "")
    name = name.replace(" inc", "")
    name = name.replace("the ", "")
    return name


def find_ticker(headline):
    for key, value in company_ticker.items():
        # print(key, value)
        if value in (" " + headline.lower()):
            return key
    return "----"
