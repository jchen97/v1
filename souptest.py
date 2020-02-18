import requests
from bs4 import BeautifulSoup

#page = requests.get("https://www.businesswire.com/portal/site/home/news/")
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify)
#print(soup.find_all('a')[3].get_text())

def cnbcbus():
    page = requests.get("https://www.cnbc.com/business/")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(list(soup.children))
    xml = list(soup.children)[0]
    print(soup.find('title'))


def motleyFool():
    page = requests.get("https://www.fool.com/premium/stock-advisor/coverage/")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    #print(list(soup.children))
    #print([type(item) for item in list(soup.children)])
    xml = list(soup.children)[2]
    #print([type(item) for item in list(xml.children)])
    body = list(xml.children)[1]
    #print([type(item) for item in list(body.children)])
    headline = list(body.children)[33]
    #print([type(item) for item in list(headline.children)])
    #print(headline.get_text())
    title = list(headline.children)[1]
    #print(title.get_text())


cnbcbus()
