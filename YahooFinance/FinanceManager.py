import yfinance as yf
import pandas as pd
from pandas import Series

import DataReaders.YahooTicker as YahooTicker


class FinanceManager(object):
    """description of class"""
    InfoDic: dict
    ActionsDf: pd.DataFrame
    Balance_SheetDf: pd.DataFrame
    Balance_SheetQDf: pd.DataFrame
    BalanceSheetDf: pd.DataFrame
    BalanceSheetQDf: pd.DataFrame
    CalendarDf: pd.DataFrame
    CashFlowDf: pd.DataFrame
    CashFlowQDf: pd.DataFrame
    EarningDf: pd.DataFrame
    EarningQDf: pd.DataFrame
    FinancialDf: pd.DataFrame
    FinancialQDf: pd.DataFrame
    IsIn: str
    OptionTuple: tuple
    RecommendationDf: pd.DataFrame
    SplitSeries: Series
    SustainabilityDf: pd.DataFrame

    def __init__(self, yahoo_ticker: YahooTicker):
        self.__yFinance = yf.Ticker(yahoo_ticker.TickerName)
        self.InfoDic = self.__yFinance.info
        print(self.InfoDic)
        self.ActionsDf = self.__yFinance.actions
        self.Balance_SheetDf = self.__yFinance.balance_sheet
        self.BalanceSheetDf = self.__yFinance.balancesheet
        self.CalendarDf = self.__yFinance.calendar
        self.CashFlowDf = self.__yFinance.cashflow
        self.EarningDf = self.__yFinance.earnings
        self.FinancialDf = self.__yFinance.financials
        self.IsIn = "NA" if self.__yFinance.isin == "-" else self.__yFinance.isin
        self.OptionTuple = self.__yFinance.options
        self.Balance_SheetQDf = self.__yFinance.quarterly_balance_sheet
        self.BalanceSheetQDf = self.__yFinance.quarterly_balancesheet
        self.CashFlowQDf = self.__yFinance.quarterly_cashflow
        self.EarningQDf = self.__yFinance.quarterly_earnings
        self.FinancialQDf = self.__yFinance.quarterly_financials
        self.RecommendationDf = self.__yFinance.recommendations
        self.SplitSeries = self.__yFinance.splits
        self.SustainabilityDf = self.__yFinance.sustainability
