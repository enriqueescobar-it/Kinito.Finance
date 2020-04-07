from typing import Dict, Any

import Yahoo.YahooTicker as YahooTicker
import requests
from bs4 import BeautifulSoup


class YahooScrapper(object):
    """description of class"""
    Link: str = "https://in.finance.yahoo.com/quote/"
    BalanceSheetUrl: str
    BalanceSheet: Dict[Any, Any]
    CashFlowUrl: str
    CashFlow: Dict[Any, Any]
    FinancialUrl: str
    Financial: Dict[Any, Any]
    KeyStatsUrl: str
    KeyStats: Dict[Any, Any]

    def __init__(self, y_ticker: YahooTicker):
        self.__ticker = y_ticker
        self.__setUrl()
        self.__fetchBalanceSheet()
        self.__fetchCashFlow()
        self.__fetchFinancial()
        self.__fetchKeyStats()

    def __setUrl(self):
        self.BalanceSheetUrl = '{0}{1}/balance-sheet?p={2}'.format(self.Link, self.__ticker.TickerName,
                                                                   self.__ticker.TickerName)
        self.CashFlowUrl = '{0}{1}/financials?p={2}'.format(self.Link, self.__ticker.TickerName,
                                                            self.__ticker.TickerName)
        self.FinancialUrl = '{0}{1}/cash-flow?p={2}'.format(self.Link, self.__ticker.TickerName,
                                                            self.__ticker.TickerName)
        self.KeyStatsUrl = '{0}{1}/key-statistics?p={2}'.format(self.Link, self.__ticker.TickerName,
                                                                self.__ticker.TickerName)

    def __fetchBalanceSheet(self):
        temp_dir = {}
        page_request = requests.get(self.BalanceSheetUrl)
        page_content = page_request.content
        page_soup = BeautifulSoup(page_content, 'html.parser')
        page_tag = "W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)"  # "M(0) Mb(10px) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"
        page_table = page_soup.find_all("div", {"class": page_tag})
        for page_link in page_table:
            rows = page_link.find_all("div", {"class": "rw-expnded"})
            for row in rows:
                temp_dir[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[1]
        self.BalanceSheet = temp_dir

    def __fetchCashFlow(self):
        temp_dir = {}
        page_request = requests.get(self.CashFlowUrl)
        page_content = page_request.content
        page_soup = BeautifulSoup(page_content, 'html.parser')
        page_tag = "smartphone_Px(20px) Mb(30px)"  # "W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)" # M(0) Mb(10px) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"
        page_table = page_soup.find_all("div", {"class": page_tag})
        for page_link in page_table:
            rows = page_link.find_all("div", {"class": "rw-expnded"})
            for row in rows:
                temp_dir[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[1]
        self.CashFlow = temp_dir

    def __fetchFinancial(self):
        temp_dir = {}
        page_request = requests.get(self.CashFlowUrl)
        page_content = page_request.content
        page_soup = BeautifulSoup(page_content, 'html.parser')
        page_tag = "W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)" #  "M(0) Mb(10px) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"
        page_table = page_soup.find_all("div", {"class": page_tag})
        for page_link in page_table:
            rows = page_link.find_all("div", {"class": "rw-expnded"})
            for row in rows:
                temp_dir[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[1]
        self.Financial = temp_dir

    def __fetchKeyStats(self):
        temp_dir = {}
        page_request = requests.get(self.CashFlowUrl)
        page_content = page_request.content
        page_soup = BeautifulSoup(page_content, 'html.parser')
        page_tag = "Pb(30px) Px(20px)"  # "W(100%) Bdcl(c) Mt(10px) "
        page_table = page_soup.find_all("table", {"class": page_tag})
        for page_link in page_table:
            rows = page_link.find_all("tr")
            for row in rows:
                if len(row.get_text(separator='|').split("|")[0:2]) > 0:
                    temp_dir[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[-1]
        self.KeyStats = temp_dir
