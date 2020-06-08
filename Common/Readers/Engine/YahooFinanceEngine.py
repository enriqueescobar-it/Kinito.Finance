import yfinance as yf
import pandas as pd
from pandas import Series
from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinanceEngine(AbstractEngine):
    """description of class"""
    Url: str
    LogoUrl: str
    Address: str
    City: str
    State: str
    PostalCode: str
    Country: str
    _ticker: str
    InfoDic: dict
    '''ActionsDf: pd.DataFrame
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
    SustainabilityDf: pd.DataFrame'''

    def __init__(self, a_ticker: str = 'CNI'):
        self._ticker = a_ticker
        self.__yFinance = yf.Ticker(a_ticker)
        self.InfoDic = self.__yFinance.info
        print(self.InfoDic)
        self.__setUrl()
        self.__setLogoUrl()
        self.__setAddress()
        self.__setCity()
        self.__setState()
        self.__setPostalCode()
        self.__setCountry()
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

    def __setUrl(self):
        self.Url = self.InfoDic['website']

    def __setLogoUrl(self):
        self.LogoUrl = self.InfoDic['logo_url']

    def __setAddress(self):
        self.Address = self.InfoDic['address1']

    def __setCity(self):
        self.City = self.InfoDic['city']

    def __setPostalCode(self):
        self.PostalCode = self.InfoDic['zip']

    def __setState(self):
        self.State = self.InfoDic['state']

    def __setCountry(self):
        self.Country = self.InfoDic['country']
