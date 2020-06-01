from Common.WebScrappers.AbstractWebScrapper import AbstractWebScrapper
from yarl import URL


class YahooScrapper(AbstractWebScrapper):
    """description of class"""
    Link: str = "https://finance.yahoo.com/quote/"
    Url: URL

    def __init__(self, a_ticker: str):
        self.__ticker: str = a_ticker
        self.__setLink()

    def __setLink(self):
        self.Link = '{0}{1}'.format(self.Link, self.__ticker)
        self.__setUrl()

    def __setUrl(self):
        self.Url = URL(self.Link)

    def ParseBody(self):
        pass
