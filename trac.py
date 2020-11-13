import winsound
import requests
from bs4 import BeautifulSoup

POST_LOGIN_URL = "https://trac.trilliumtrading.com/Login"
REQUEST_URL = "https://trac.trilliumtrading.com/activelytradedstocksreport2.action"

payload = {
    "username": "jchen",
    "password": "babka",
    "#FROM_PAGE#": "#LOGIN#"
}


class Color:
    LTRED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'


tickers = set()


def tracScrape():
    with requests.Session() as session:
        session.post(POST_LOGIN_URL, data=payload)
        r = session.get(REQUEST_URL)

        html = r.text

        soup = BeautifulSoup(html, "html.parser")
        table = soup.find_all('table')[10]

        for row in table.findAll('tr'):
            columns = row.findAll('td')

            count = 0
            for column in columns:
                cell = column.get_text()
                if count == 1:
                    if cell not in tickers:
                        tickers.add(cell)
                        preface = Color.YELLOW + "New TrAC Ticker" + Color.END
                        print("-" * 99)
                        print("\n")
                        print(preface + Color.LTRED + cell + Color.END)

                count = count + 1
