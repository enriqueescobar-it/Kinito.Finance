from typing import Optional

from pandas import DataFrame
from yahoo_fin.stock_info import *

from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinEngine(AbstractEngine):
    AnalyseEarningsEstimateDf: pd.DataFrame
    AnalyseRevenueEstimateDf: pd.DataFrame
    AnalyseEarningsHistoryDf: pd.DataFrame
    AnalyseEPSRevisionsDf: pd.DataFrame
    AnalyseGrowthEstimateDf: pd.DataFrame
    __analysisDictionary: dict
    CashFlowDf: Optional[DataFrame]
    BalanceSheetDf: Optional[DataFrame]
    IncomeStatementDf: Optional[DataFrame]
    __ticker: str

    def __init__(self, a_ticker: str = 'CNI'):
        self.__ticker = a_ticker
        self.GetAnalysis()
        self.GetBalanceSheet()
        self.GetCashFlow()
        self.GetIncomeStatement()

    def GetAnalysis(self):
        self.__analysisDictionary = get_analysts_info(self.__ticker)
        self.AnalyseEarningsEstimateDf = self.__analysisDictionary['Earnings Estimate']
        self.AnalyseRevenueEstimateDf = self.__analysisDictionary['Revenue Estimate']
        self.AnalyseEarningsHistoryDf = self.__analysisDictionary['Earnings History']
        self.AnalyseEPSRevisionsDf = self.__analysisDictionary['EPS Revisions']
        self.AnalyseGrowthEstimateDf = self.__analysisDictionary['Growth Estimates']

    def GetBalanceSheet(self):
        self.BalanceSheetDf = get_balance_sheet(self.__ticker)

    def GetCashFlow(self):
        self.CashFlowDf = get_cash_flow(self.__ticker)

    def GetIncomeStatement(self):
        self.IncomeStatementDf = get_income_statement(self.__ticker)
        print('val: ', get_stats_valuation(self.__ticker))
        print('stat: ', get_stats(self.__ticker))
