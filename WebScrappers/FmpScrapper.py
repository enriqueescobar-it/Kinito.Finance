from typing import Dict, Any

import DataReaders.YahooTicker as YahooTicker
import requests


class FmpScrapper(object):
    """description of class"""
    Link: str = "https://financialmodelingprep.com/api/v3"
    BalanceSheetUrl: str
    BalanceSheet: dict
    CashFlowUrl: str
    CashFlow: Dict[Any, Any]
    FinancialUrl: str
    Financial: Dict[Any, Any]
    KeyStatsUrl: str
    KeyStats: Dict[Any, Any]
    IncomeUrl: str
    Income: Dict[Any, Any]

    def __init__(self, y_ticker: YahooTicker):
        self.__ticker = y_ticker
        self.__setUrl()
        self.__fetchBalanceSheet()
        self.__fetchCashFlow()
        self.__fetchFinancial()
        self.__fetchKeyStats()
        self.__fetchIncome()

    def __setUrl(self):
        self.BalanceSheetUrl = '{0}/financials/balance-sheet-statement/{1}'.format(self.Link, self.__ticker.TickerName)
        self.CashFlowUrl = '{0}/financials/cash-flow-statement/{1}'.format(self.Link, self.__ticker.TickerName)
        self.FinancialUrl = '{0}/enterprise-value/{1}'.format(self.Link, self.__ticker.TickerName)
        self.KeyStatsUrl = '{0}/company-key-metrics/{1}'.format(self.Link, self.__ticker.TickerName)
        self.IncomeUrl = '{0}/financials/income-statement/{1}'.format(self.Link, self.__ticker.TickerName)

    def __fetchBalanceSheet(self):
        page_request = requests.get(self.BalanceSheetUrl)
        fin_dir = page_request.json()
        self.BalanceSheet = {key: value for key, value in fin_dir["financials"][0].items()}

    def __fetchCashFlow(self):
        temp_dir: Dict[Any, Any] = {}
        temp_key: str = "financials"
        page_request = requests.get(self.CashFlowUrl)
        fin_dir = page_request.json()
        for key, value in fin_dir[temp_key][0].items():
            if key not in temp_dir.keys():
                temp_dir[key] = value
        self.CashFlow = temp_dir

    def __fetchFinancial(self):
        temp_dir: Dict[Any, Any] = {}
        temp_key: str = "enterpriseValues"
        page_request = requests.get(self.FinancialUrl)
        fin_dir = page_request.json()
        for key, value in fin_dir[temp_key][0].items():
            if key not in temp_dir.keys():
                temp_dir[key] = value
        self.Financial = temp_dir

    def __fetchKeyStats(self):
        temp_dir: Dict[Any, Any] = {}
        temp_key: str = "metrics"
        page_request = requests.get(self.KeyStatsUrl)
        fin_dir = page_request.json()
        for key, value in fin_dir[temp_key][0].items():
            if key not in temp_dir.keys():
                temp_dir[key] = value
        self.KeyStats = temp_dir

    def __fetchIncome(self):
        temp_dir: Dict[Any, Any] = {}
        temp_key: str = "financials"
        page_request = requests.get(self.IncomeUrl)
        fin_dir = page_request.json()
        for key, value in fin_dir[temp_key][0].items():
            if key not in temp_dir.keys():
                temp_dir[key] = value
        self.Income = temp_dir
