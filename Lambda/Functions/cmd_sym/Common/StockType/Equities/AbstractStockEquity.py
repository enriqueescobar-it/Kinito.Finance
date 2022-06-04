from matplotlib import pyplot as plt
import numpy as np
from pandas import DataFrame
import pandas
from prettytable import PrettyTable
from yahooquery import Ticker

from Common.StockType.AbstractStock import AbstractStock
from Common.Readers.Engine.YahooFinStockInfo import YahooFinStockInfo


class AbstractStockEquity(AbstractStock):
    __ticker: str = 'NA'
    __y_query: Ticker
    __yfsi: YahooFinStockInfo
    _name: str = 'NA'
    _has_sectors: bool = False
    _has_holdings: bool = False
    _has_quote_dict: bool = True
    _has_summary_dict: bool = True
    _has_financial_dict: bool = False
    _has_stats_dict: bool = False
    _has_price_dict: bool = True
    _has_net_share_dict: bool = False
    _has_trend_df: bool = False
    _has_company_officers_df: bool = False
    _has_institute_owner_df: bool = False
    _has_insider_holder_df: bool = False
    _has_major_holder_dict: bool = False
    _has_fund_owner_df: bool = False
    _has_fund_bond_dict: bool = False
    _has_fund_category_df: bool = False
    _has_fund_perf_df: bool = False
    _has_fund_bond_rating_df: bool = False
    _has_fund_sector_weight_df: bool = False
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _trend_df: DataFrame = DataFrame()
    _company_officers_df: DataFrame = DataFrame()
    _institute_owner_df: DataFrame = DataFrame()
    _fund_owner_df: DataFrame = DataFrame()
    _fund_category_df: DataFrame = DataFrame()
    _fund_perf_df: DataFrame = DataFrame()
    _fund_bond_rating_df: DataFrame = DataFrame()
    _fund_sector_weight_df: DataFrame = DataFrame()
    _insider_holder_df: DataFrame = DataFrame()
    _major_holder_dict: dict = {}
    _quote_dict: dict = {}
    _summary_dict: dict = {}
    _financial_dict: dict = {}
    _stats_dict: dict = {}
    _price_dict: dict = {}
    _net_share_dict: dict = {}
    _fund_bond_dict: dict = {}
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _cash_part_count: int = -1
    _price_to_book: float = np.nan
    _price_to_cash: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sale: float = np.nan

    def __init__(self, c_name: str, t_name: str, q_type: str):
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Equity'
        self._quote_type = q_type
        #
        self.__y_query = Ticker(t_name)
        self.__yfsi = YahooFinStockInfo(t_name)
        self._setInfo()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Info', 'StockInfo'])
        pt.add_row(['Ticker', self.__ticker])
        pt.add_row(['Type', self.__class])
        pt.add_row(['QuoteType', self._quote_type])
        pt.add_row(['Name', self._name])
        pt.add_row(['StockPercent', self._stock_part_count])
        pt.add_row(['BondPercent', self._bond_part_count])
        pt.add_row(['CashPercent', self._cash_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        pt.add_row(['HasSectors', self._has_sectors])
        pt.add_row(['HasHoldings', self._has_holdings])
        pt.add_row(["HasQuoteDict", self._has_quote_dict])
        pt.add_row(["HasSummaryDict", self._has_summary_dict])
        pt.add_row(['HasFinancialDict', self._has_financial_dict])
        pt.add_row(['HasStatsDict', self._has_stats_dict])
        pt.add_row(["HasPriceDict", self._has_price_dict])
        pt.add_row(["HasNetShareDict", self._has_net_share_dict])
        pt.add_row(["HasTrendDf", self._has_trend_df])
        pt.add_row(["HasCompanyOfficersDf", self._has_company_officers_df])
        pt.add_row(["HasInstituteOwnerDf", self._has_institute_owner_df])
        pt.add_row(["HasInsiderHolderDf", self._has_insider_holder_df])
        pt.add_row(["HasMajorHolderDict", self._has_major_holder_dict])
        pt.add_row(["HasFundOwnerDf", self._has_fund_owner_df])
        pt.add_row(["HasFundBondDict", self._has_fund_bond_dict])
        pt.add_row(["HasFundCategoryDf", self._has_fund_category_df])
        pt.add_row(["HasFundPerformanceDf", self._has_fund_perf_df])
        pt.add_row(["HasFundRatingDf", self._has_fund_bond_rating_df])
        pt.add_row(["HasFundSectorWeightDf", self._has_fund_sector_weight_df])
        s = pt.__str__()
        if self._has_sectors:
            s += "\n\nSECTOR DATAFRAME\n" + self._sector_df.to_string(index=True)
        if self._has_holdings:
            s += "\n\nHOLDING DATAFRAME\n" + self._holding_df.to_string(index=True)
        if self._has_quote_dict:
            s += "\n\nQUOTE DICTIONARY\n" + str(self._quote_dict)
        if self._has_summary_dict:
            s += "\n\nSUMMARY DICTIONARY\n" + str(self._summary_dict)
        if self._has_financial_dict:
            s += "\n\nFINANCIAL DICTIONARY\n" + str(self._financial_dict)
        if self._has_stats_dict:
            s += "\n\nSTATS DICTIONARY\n" + str(self._stats_dict)
        if self._has_price_dict:
            s += "\n\nPRICE DICTIONARY\n" + str(self._price_dict)
        if self._has_net_share_dict:
            s += "\n\nNET SHARE DICTIONARY\n" + str(self._net_share_dict)
        if self._has_trend_df:
            s += "\n\nRECOMMENDED TREND DF\n" + self._trend_df.to_string(index=True)
        if self._has_company_officers_df:
            s += "\n\nCOMPANY OFFICERS DF\n" + self._company_officers_df.to_string(index=True)
        if self._has_institute_owner_df:
            s += "\n\nINSTITUTION OWNER DF\n" + self._institute_owner_df.to_string(index=False)
        if self._has_insider_holder_df:
            s += "\n\nINSIDER HOLDER DF\n" + self._insider_holder_df.to_string(index=False)
        if self._has_major_holder_dict:
            s += "\n\nMAJOR HOLDER DICTIONARY\n" + str(self._major_holder_dict)
        if self._has_fund_owner_df:
            s += "\n\nFUND OWNER DF\n" + self._fund_owner_df.to_string(index=True)
        if self._has_fund_bond_dict:
            s += "\n\nFUND BOND DICTIONARY\n" + str(self._fund_bond_dict)
        if self._has_fund_category_df:
            s += "\n\nFUND CATEGORY DF\n" + self._fund_category_df.to_string(index=True)
        if self._has_fund_perf_df:
            s += "\n\nFUND PERFORMANCE DF\n" + self._fund_perf_df.to_string(index=True)
        if self._has_fund_bond_rating_df:
            s += "\n\nFUND BOND RATING DF\n" + self._fund_bond_rating_df.to_string(index=True)
        if self._has_fund_sector_weight_df:
            s += "\n\nFUND SECTOR WEIGHT DF\n" + self._fund_sector_weight_df.to_string(index=True)
        return s

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "Info": "StockInfo",
            "ticker": self.__ticker,
            "type": self.__class,
            "quote_type": self._quote_type,
            "name": self._name,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "cash_percent": self._cash_part_count,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash,
            "has_sectors": self._has_sectors,
            "has_holdings": self._has_holdings,
            "has_quote_dict": self._has_quote_dict,
            "has_summary_dict": self._has_summary_dict,
            "has_financial_dict": self._has_financial_dict,
            "has_stats_dict": self._has_stats_dict,
            "has_price_dict": self._has_price_dict,
            "has_net_share_dict": self._has_net_share_dict,
            "has_trend_df": self._has_trend_df,
            "has_company_officers_df": self._has_company_officers_df,
            "has_institute_owner_df": self._has_institute_owner_df,
            "has_insider_holder_df": self._has_insider_holder_df,
            "has_major_holder_dict": self._has_major_holder_dict,
            "has_fund_owner_df": self._has_fund_owner_df,
            "has_fund_bond_dict": self._has_fund_bond_dict,
            "has_fund_category_df": self._has_fund_category_df,
            "has_fund_perf_df": self._has_fund_perf_df,
            "has_fund_bond_rating_df": self._has_fund_bond_rating_df,
            "has_fund_sector_weight_df": self._has_fund_sector_weight_df
        }.items()

    def _setInfo(self):
        self.__setSectorDf()
        self.__setHoldingDf()
        self._stock_part_count = 0
        self._bond_part_count = 0
        self._stock_part_count, self._bond_part_count, self._cash_part_count = self.__setAllocation()
        self.__setInfo()
        self.__setPerformance()
        self._quote_dict = self._get_sub_dict(self.__y_query.quote_type, self.__ticker)
        self._summary_dict = self._get_sub_dict(self.__y_query.summary_detail, self.__ticker)
        self._has_financial_dict, self._financial_dict = self._get_dict_valid(self.__y_query.financial_data, 'financialData')
        self._financial_dict = self._get_sub_dict(self._financial_dict, self.__ticker)
        self._has_stats_dict, self._stats_dict = self._get_dict_valid(self.__y_query.key_stats, 'defaultKeyStatistics')
        self._stats_dict = self._get_sub_dict(self._stats_dict, self.__ticker)
        self._price_dict = self._get_sub_dict(self.__y_query.price, self.__ticker)
        self._has_net_share_dict, self._net_share_dict = self._get_dict_valid(self.__y_query.share_purchase_activity, 'netSharePurchaseActivity')
        self._net_share_dict = self._get_sub_dict(self.__y_query.share_purchase_activity, self.__ticker)
        self._has_trend_df, self._trend_df = self._get_df_valid(self.__y_query.recommendation_trend, 'recommendationTrend')
        self._has_company_officers_df, self._company_officers_df = self._get_df_valid(self.__y_query.company_officers, 'assetProfile')
        self._has_institute_owner_df, self._institute_owner_df = self._get_df_valid(self.__y_query.institution_ownership, 'institutionOwnership')
        self._has_insider_holder_df, self._insider_holder_df = self._get_df_valid(self.__y_query.insider_holders, 'insiderHolders')
        self._has_major_holder_dict, self._major_holder_dict = self._get_dict_valid(self.__y_query.major_holders, 'majorHoldersBreakdown')
        self._major_holder_dict = self._get_sub_dict(self._major_holder_dict, self.__ticker)
        self._has_fund_owner_df, self._fund_owner_df = self._get_df_valid(self.__y_query.fund_ownership, 'fundOwnership')
        self._has_fund_bond_dict, self._fund_bond_dict = self._get_dict_valid(self.__y_query.fund_bond_holdings, 'topHoldings')
        self._fund_bond_dict = self._get_sub_dict(self._fund_bond_dict, self.__ticker)
        self._has_fund_category_df, self._fund_category_df = self._get_df_valid(self.__y_query.fund_category_holdings, 'topHoldings')
        self._has_fund_perf_df, self._fund_perf_df = self._get_df_valid(self.__y_query.fund_performance, 'fundPerformance')
        self._has_fund_bond_rating_df, self._fund_bond_rating_df = self._get_df_valid(self.__y_query.fund_bond_ratings, 'topHoldings')
        self._has_fund_sector_weight_df, self._fund_sector_weight_df = self._get_df_valid(self.__y_query.fund_sector_weightings, 'topHoldings')
        print(type(self.__y_query.insider_transactions))
        print('[', self.__y_query.insider_transactions, ']insiderTransactions')
        #print('[', self.__y_query.earnings_trend, ']earningsTrend')
        #print('[', self.__y_query.earning_history, ']earningsHistory')
        #print('[', self.__y_query.sec_filings, ']secFilings')
        #print('[', self.__y_query.balance_sheet(frequency='a'), ']B_DF unavailable')
        #print('[', self.__y_query.income_statement(frequency='a'), ']I_DF unavailable')
        #print('[', self.__y_query.cash_flow(frequency='a'), ']C_DF unavailable')
        #exit(-1)
        self.__plotSectorDf()#.show()

    def __setSectorDf(self):
        is_df: bool = isinstance(self.__y_query.fund_sector_weightings, pandas.DataFrame)

        if is_df:
            self._sector_df = self.__y_query.fund_sector_weightings.reset_index()
            self._sector_df.columns = ['Sector', 'Percent']
            self._has_sectors = True
        else:
            s: str = (list(self.__y_query.fund_sector_weightings.values())[0]).split(' found ')[0]
            self._sector_df['Sector'] = s
            self._sector_df['Percent'] = 1.0
            self._sector_df.loc[0] = [s, 1.0]

    def __plotSectorDf(self) -> plt:
        if (self._sector_df['Percent'] != self._sector_df['Percent'][0]).all():
            self._sector_df.plot.pie(x='Sector', y='Percent', labels=self._sector_df['Sector'], subplots=True,
                                    autopct="%.1f%%", figsize=(10, 10), fontsize=9, legend=True,
                                    title='Sector Distribution ' + self.__ticker + ' ' + self.__class)
            return plt

    def __setHoldingDf(self):
        is_df: bool = isinstance(self.__y_query.fund_top_holdings, pandas.DataFrame)

        if is_df:
            self._holding_df = self.__y_query.fund_top_holdings
            self._holding_df.set_index('symbol', inplace=True)
            self._holding_df.reset_index(inplace=True)
            self._has_holdings = True
        else:
            s: str = (list(self.__y_query.fund_sector_weightings.values())[0]).split(' found ')[0]
            self._holding_df['symbol'] = s
            self._holding_df['holdingName'] = 'a name'
            self._holding_df['holdingPercent'] = 1.0
            self._holding_df.loc[0] = [self.__ticker, s, 1.0]

    def __setAllocation(self):
        is_df: bool = isinstance(self.__y_query.fund_top_holdings, pandas.DataFrame)
        df: DataFrame = DataFrame()
        stock_int: int = 0
        bond_int: int = 0
        cash_int: int = 0
        other_int: int = 0
        pref_int: int = 0
        conv_int: int = 0

        if is_df:
            df = self.__y_query.fund_category_holdings.set_index('maxAge')
            df.reset_index(inplace=True)
            if 'stockPosition' in df.columns:
                stock_int = round(df['stockPosition'][0] * 100)
            if 'bondPosition' in df.columns:
                bond_int = round(df['bondPosition'][0] * 100)
            if 'cashPosition' in df.columns:
                cash_int = round(df['cashPosition'][0] * 100)
            if 'otherPosition' in df.columns:
                other_int = round(df['otherPosition'][0] * 100)
            if 'preferredPosition' in df.columns:
                pref_int = round(df['preferredPosition'][0] * 100)
            if 'convertiblePosition' in df.columns:
                conv_int = round(df['convertiblePosition'][0] * 100)
        else:
            df['maxAge'] = 1.0
            df['cashPosition'] = np.nan
            df['stockPosition'] = np.nan
            df['bondPosition'] = np.nan
            df['otherPosition'] = np.nan
            df['preferredPosition'] = np.nan
            df['convertiblePosition'] = np.nan
            df.loc[0] = [1.0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
            df = df.set_index('maxAge')
            df.reset_index(inplace=True)
            stock_int = round(np.nan_to_num(df['stockPosition'][0]) * 100)
            bond_int = round(np.nan_to_num(df['bondPosition'][0]) * 100)
            cash_int = round(np.nan_to_num(df['cashPosition'][0]) * 100)
        return stock_int, bond_int, cash_int

    def __setInfo(self):
        self._price_to_book = self.__yfsi.PriceToBook
        self._price_to_earn = self.__yfsi.PriceToEarnings
        self._price_to_sale = self.__yfsi.PriceToSales
        '''
        "maxAge": 1,
        "priceHint": 2,
        "enterpriseValue": 1672450801664,
        "forwardPE": 25.70207,
        "profitMargins": 0.21350001,
        "floatShares": 4329740605,
        "sharesOutstanding": 4334329856,
        "sharesShort": 35234606,
        "sharesShortPriorMonth": 34828293,
        "sharesShortPreviousMonthDate": "2020-06-15 00:00:00",
        "dateShortInterest": "2020-07-15 00:00:00",
        "sharesPercentSharesOut": 0.0081,
        "heldPercentInsiders": 0.00066,
        "heldPercentInstitutions": 0.62115,
        "shortRatio": 0.96,
        "shortPercentOfFloat": 0.0081,
        "beta": 1.182072,
        "category": null,
        "bookValue": 18.137,
        "priceToBook": 21.214094,
        "fundFamily": null,
        "legalType": null,
        "lastFiscalYearEnd": "2019-09-28 00:00:00",
        "nextFiscalYearEnd": "2021-09-28 00:00:00",
        "mostRecentQuarter": "2020-03-28 00:00:00",
        "earningsQuarterlyGrowth": -0.027,
        "netIncomeToCommon": 57215000576,
        "trailingEps": 12.728,
        "forwardEps": 14.97,
        "pegRatio": 2.78,
        "lastSplitFactor": "7:1",
        "lastSplitDate": "2014-06-09 00:00:00",
        "enterpriseToRevenue": 6.241,
        "enterpriseToEbitda": 21.634,
        "52WeekChange": 0.8239218,
        "SandP52WeekChange": 0.103224516
        '''

    def __setPerformance(self):
        is_null: bool = len(self.__y_query.fund_performance.get(self.__ticker)) >= 50

        if is_null:
            print("+", self.__class__.__name__, ':', self.__ticker + ' size', len(self.__y_query.fund_performance.get(self.__ticker)))
        else:
            for key in self.__y_query.fund_performance.get(self.__ticker):
                print("+", self.__class__.__name__, ':', key)

    @property
    def Name(self):
        return self._name

    @property
    def HoldingDataFrame(self):
        return self._holding_df

    @property
    def SectorDataFrame(self):
        return self._sector_df

    @property
    def StockPartCount(self):
        return self._stock_part_count

    @property
    def BondPartCount(self):
        return self._bond_part_count

    @property
    def CashPartCount(self):
        return self._cash_part_count

    @property
    def PriceToEarnings(self):
        return self._price_to_earn

    @property
    def PriceToSales(self):
        return self._price_to_sale

    @property
    def PriceToBook(self):
        return self._price_to_book

    @property
    def PriceToCashflow(self):
        return self._price_to_cash

    @property
    def HasSectors(self):
        return self._has_sectors

    @property
    def HasHoldings(self):
        return self._has_holdings
