import csv

tickers = []
company_names = []


with open('finviz1.csv', 'r') as stockfile:
    reader = csv.reader(stockfile)
    for row in reader:
        if " ETF" not in row[2]:
            tickers.append(row[1])
            company_names.append
# write entire thing to file

with open('justin.csv', 'w') as newfile:
    writer = csv.writer(newfile)
    for row in writer:
        print("r")