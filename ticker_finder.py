import csv
from formatV1 import Color

# ticker:name string
company_ticker = {}
# ticker:corresponding sound string
tickers_sound = {}
# ticker:tuple of relevant words


relevant_words = {}
# ^^^ need to implement this


def initiate():
    global company_ticker

    with open('finviz1.csv', 'r') as stockfile:
        reader = csv.reader(stockfile)
        for row in reader:
            ticker = ((4 - len(row[0])) * " ") + row[0]
            company_name = cleanup(" " + row[1])

            pair = {ticker: company_name}
            company_ticker.update(pair)

    while "" in company_ticker:
        del company_ticker[""]

    print(company_ticker)


# cleans up string for company names
def cleanup(name):
    name = name.replace(" L.P.", "")
    name = name.replace(" Co.", "")
    name = name.replace(" Ltd", "")
    name = name.replace(" plc", "")
    name = name.replace(" Plc", "")
    name = name.replace(" PLC", "")
    name = name.replace(" LLC", "")
    name = name.replace(" ETF", "")
    name = name.replace(" Technologies", "")

    name = name.replace(" Incorporated", "")
    name = name.replace(" International Corporation", "")
    name = name.replace(" Corporation", "")

    name = name.replace(" Holding Corp.", "")
    name = name.replace(" Holdings", "")
    name = name.replace(" Holding", "")

    name = name.replace(" Public Joint Stock Company", "")
    name = name.replace(" Public Limited Company", "")
    name = name.replace(" Limited Company", "")
    name = name.replace(" Company", "")
    name = name.replace(" Limited", "")
    name = name.replace(",", "")
    name = name.replace(".", "")
    name = name.replace(" Inc", "")
    name = name.replace("The ", "")
    return name


def find_ticker(headline):
    for key, value in company_ticker.items():
        # print(key, value)
        if value in (" " + headline):
            return key
    return "----"
