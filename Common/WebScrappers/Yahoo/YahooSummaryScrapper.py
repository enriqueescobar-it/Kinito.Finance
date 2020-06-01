from Common.WebScrappers.Yahoo.YahooScrapper import YahooScrapper
import bs4
import requests


class YahooSummaryScrapper(YahooScrapper):
    Beta: str
    EPS: str
    EarningsDate: str
    MarketCap: str
    PEratio: str
    __htmlBody: bs4.ResultSet
    __request: str
    __htmlParser: bs4.BeautifulSoup

    def __init__(self, a_ticker: str):
        super().__init__(a_ticker)
        self.__setRequest()
        self.__setHtmlParser()
        self.__setHtmlBody()

    def __setRequest(self):
        self.__request = requests.get(self.Link).text

    def __setHtmlParser(self):
        self.__htmlParser = bs4.BeautifulSoup(self.__request, 'html.parser')

    def __setHtmlBody(self):
        self.__htmlBody = self.__htmlParser.find_all("tbody")

    def ParseBody(self):
        l = {}
        u = list()
        try:
            table1 = self.__htmlBody[0].find_all("tr")
        except:
            table1 = None
        try:
            table2 = self.__htmlBody[1].find_all("tr")
        except:
            table2 = None
        for i in range(0, len(table1)):
            try:
                table1_td = table1[i].find_all("td")
            except:
                table1_td = None
            l[table1_td[0].text] = table1_td[1].text
            u.append(l)
            l = {}
        for i in range(0, len(table2)):
            try:
                table2_td = table2[i].find_all("td")
            except:
                table2_td = None
            l[table2_td[0].text] = table2_td[1].text
            u.append(l)
            l = {}
        self.MarketCap = str(u[:][8]['Market Cap'])
        self.Beta = str(u[:][9]['Beta (5Y Monthly)'])
        self.PEratio = str(u[:][10]['PE Ratio (TTM)'])
        self.EPS = str(u[:][11]['EPS (TTM)'])
        self.EarningsDate = str(u[:][12]['Earnings Date'])
