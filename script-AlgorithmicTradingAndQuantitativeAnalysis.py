from datetime import date
from pprint import pprint
from typing import List, Any, Union
import pandas as pd
from pandas import DataFrame
import Common.Measures.TradingDateTimes.PyDateTimes as PyDays
import Common.Readers.TickerNameList as PyTickers
import Common.Readers.YahooTicker as PyTicker
from Common.TimeSeries import AlphaVantageManager
from Common.WebScrappers import YahooScrapper, FmpScrapper, StockRowScrapper
from Common.Readers.YahooTicker import YahooTicker
from Common.Readers.Engine import YahooFinancialEngine
from Common.Readers.Engine.YahooFinanceEngine import FinanceManager
from Common.Readers.Engine.FinVizEngine import FinVizManager
from Common.Readers import YahooPdrManager
from Common.TechnicalIndicators.MovingAverageConvergenceDivergenceManager import MovingAverageConvergenceDivergenceManager
from Common.TechnicalIndicators.AverageTrueRangeManager import AverageTrueRangeManager
from Common.TechnicalIndicators import BollingerBandsManager
from Common.TechnicalIndicators.RelativeStrengthIndexManager import RelativeStrengthIndexManager
from Common.TechnicalIndicators.OnBalanceVolumeManager import OnBalanceVolumeManager
from Common.TechnicalIndicators import SlopesManager
from Common.TechnicalIndicators.RenkoManager import RenkoManager
from Common.TechnicalIndicators.AverageDirectionalIndexManager import AverageDirectionalIndexManager
from Common.PerformanceIndicators import SortinoRatioManager
from Common.PerformanceIndicators.SharpeRatioManager import SharpeRatioManager
from Common.PerformanceIndicators import MaximumDrawDownManager
from Common.PerformanceIndicators.CumulativeAnnualGrowthRateManager import CumulativeAnnualGrowthRateManager
from Common.PerformanceIndicators.CalmarRatioManager import CalmarRatioManager

to_day: date = PyDays.DateTimeNow()
to_day_s: str = to_day.strftime('%Y-%m-%d')
ya_day: date = PyDays.DateTime52WeekAgo()
ya_day_s: str = ya_day.strftime('%Y-%m-%d')
alpha_key = "Data/alphavantage-key.txt"
# extracting stock data (historical close price) for the stocks identified
ticker_list = PyTickers.PortfolioDjiStocks()
# ticker_list = PyTickers.NameList50()
counter: int = 0
pdr_adjclose_df: DataFrame = pd.DataFrame()
financial_df: DataFrame = pd.DataFrame()
alpha_close_df: DataFrame = pd.DataFrame()
drop_list: List[Union[str, Any]] = []
py_tickers: List[YahooTicker] = []
new_tickers = ticker_list
yTicker = PyTicker.YahooTicker('NYSE', ticker_list[1], 26, 0)
financeManager: FinanceManager = FinanceManager(yTicker)
finVizManager: FinVizManager = FinVizManager(yTicker)
financialManager: YahooFinancialEngine = YahooFinancialEngine(yTicker)
yahooPdrManager: YahooPdrManager = YahooPdrManager(yTicker, ya_day, to_day)
print('MACD')
macdManager: MovingAverageConvergenceDivergenceManager = MovingAverageConvergenceDivergenceManager(yahooPdrManager.YahooData, ya_day, to_day)
pprint(macdManager.IndicatorDf.tail().iloc[:, -5:])
print('ATR')
atrManager: AverageTrueRangeManager = AverageTrueRangeManager(yahooPdrManager.YahooData, 20)
pprint(atrManager.IndicatorDf.tail().iloc[:, -5:])
print('BollingerBands')
babeManager: BollingerBandsManager = BollingerBandsManager(yahooPdrManager.YahooData)
pprint(babeManager.IndicatorDf.tail().iloc[:, -5:])
print('RSI')
rsiManager: RelativeStrengthIndexManager = RelativeStrengthIndexManager(yahooPdrManager.YahooData)
pprint(rsiManager.IndicatorDf.tail().iloc[:, -5:])
print('OBV')
obvManager: OnBalanceVolumeManager = OnBalanceVolumeManager(yahooPdrManager.YahooData)
pprint(obvManager.IndicatorDf.head().iloc[:, -5:])
print('Slopes')
slopesManager: SlopesManager = SlopesManager(yahooPdrManager.YahooData)
pprint(slopesManager.IndicatorDf.head().iloc[:, -5:])
print('Renko')
renkoManager: RenkoManager = RenkoManager(yahooPdrManager.YahooData)
pprint(renkoManager.IndicatorDf.head().iloc[:, -5:])
print('ADX')
adxManager: AverageDirectionalIndexManager = AverageDirectionalIndexManager(yahooPdrManager.YahooData)
pprint(adxManager.IndicatorDf.tail().iloc[:, -5:])
print('SortinoRatio')
sortinoRatioManage: SortinoRatioManager = SortinoRatioManager(yahooPdrManager.YahooData)
print(sortinoRatioManage.KPIdf)
print('SharpeRatio')
sharpeRatioManager: SharpeRatioManager = SharpeRatioManager(yahooPdrManager.YahooData)
print(sharpeRatioManager.KPIdf)
print('MaximumDrawDown')
mddManager: MaximumDrawDownManager = MaximumDrawDownManager(yahooPdrManager.YahooData)
print(mddManager.KPIdf)
print('CumulativeAnnualGrowthRate')
cagrManager: CumulativeAnnualGrowthRateManager = CumulativeAnnualGrowthRateManager(yahooPdrManager.YahooData)
print(cagrManager.KPIdf)
print('CalmarRatio')
crManager: CalmarRatioManager = CalmarRatioManager(yahooPdrManager.YahooData)
print(crManager.KPIdf)
avManager: AlphaVantageManager = AlphaVantageManager(alpha_key, yTicker)
yahooScrapper: YahooScrapper = YahooScrapper(yTicker)
pprint(yahooScrapper.BalanceSheetUrl)
pprint(yahooScrapper.CashFlowUrl)
pprint(yahooScrapper.FinancialUrl)
pprint(yahooScrapper.KeyStatsUrl)
fmpScrapper: FmpScrapper = FmpScrapper(yTicker)
pprint(fmpScrapper.BalanceSheetUrl)
pprint(fmpScrapper.CashFlowUrl)
pprint(fmpScrapper.FinancialUrl)
pprint(fmpScrapper.KeyStatsUrl)
pprint(fmpScrapper.IncomeUrl)
stockRowScrapper: StockRowScrapper = StockRowScrapper(yTicker)
pprint(stockRowScrapper.BalanceSheetUrl)
pprint(stockRowScrapper.BalanceSheetCsv)
# removing stocks whose data has been extracted from the ticker list
while len(new_tickers) != 0 and counter <= 5:
    new_tickers = [j for j in new_tickers if
                   j not in drop_list]
    for new_ticker in new_tickers:
        try:
            y_ticker = PyTicker.YahooTicker('NYSE', new_ticker, 52, 0)
            # pdr
            # pdr_df = get_data_yahoo(new_ticker, ya_day, to_day)
            # pdr_df.dropna(inplace=True)
            # pdr_df = getPdrDataFrame(new_ticker, ya_day, to_day)
            # pdr_df = y_ticker.PdrDf
            # pdr_adjclose_df[new_ticker] = pdr_df["Adj Close"]
            pdr_adjclose_df[new_ticker] = y_ticker.PdrDf["Adj Close"]
            # yahoo financial
            # new_financial: YahooFinancials = YahooFinancials(new_ticker)
            # new_financial: YahooFinancials = getYfDic(new_ticker)
            # new_financial: YahooFinancials = y_ticker.FinancialDf
            # new_dic = new_financial.get_historical_price_data(ya_day_s, to_day_s, "daily")[new_ticker]
            # new_dic = y_ticker.FinancialDf.get_historical_price_data(ya_day_s, to_day_s, "daily")[new_ticker]
            fm = YahooFinancialEngine(y_ticker)
            new_dic_field = fm.GetDailyHistoricalDataPrices(ya_day, to_day)
            new_data_frame = pd.DataFrame(new_dic_field)[["formatted_date", "adjclose"]]
            new_data_frame = new_data_frame.set_index("formatted_date", inplace=True)
            # first_data_frame = new_data_frame[~new_data_frame.index.duplicated(keep='first')]
            # financial_df[new_ticker] = first_data_frame["adjclose"]'''
            # alpha vantage
            # alpha_ts = TimeSeries(key=open(alpha_key, 'r').read(), output_format='pandas')
            # alpha_ts = getAvDay1MinPdrDataFrame(alpha_key, new_ticker)
            # alpha_df = alpha_ts.get_intraday(symbol=new_ticker, interval='1min', outputsize='full')[0]
            # alpha_df.columns = ["open", "high", "low", "close", "volume"]
            # alpha_df = getAvDay1MinPdrDataFrame(alpha_key, new_ticker)
            avm: AlphaVantageManager = AlphaVantageManager(alpha_key, y_ticker)
            alpha_close_df[new_ticker] = avm.GetIntraDayMinuteSparse(1)["close"]
            #
            drop_list.append(new_ticker)
            py_tickers.append(y_ticker)
            # i_sleep = (counter*random.random())/(2*counter)
            # time.sleep(i_sleep)
            pprint(str(counter) + " " + new_ticker + " " + str(len(drop_list)))  # + ":" + str(i_sleep))
        except:
            print(new_ticker, "_".ljust(20) + "failed to fetch data...retrying -> " + str(counter))
            continue
    counter += 1

pprint(py_tickers[0].TickerName)
pprint(str(py_tickers[0].PdrDf.shape))
exit(999)
# Replaces NaN values with the next valid value along the column
yPdr = YahooPdrManager(py_tickers[0], py_tickers[0].DateTimeFrom, py_tickers[0].DateTimeTo)
yPdr.FillNaWithNextValue()
py_tickers[0].PdrDf.fillna(method='bfill', axis=0, inplace=True)
# Deletes any row where NaN value exists
yPdr.DropRowsWithNan()
py_tickers[0].PdrDf.dropna(how='any', axis=0, inplace=True)
# Mean, Median, Standard Deviation, daily return
# prints mean stock price for each stock
print("mean")
pprint(py_tickers[0].PdrDf.mean())
# prints median stock price for each stock
print("median")
pprint(py_tickers[0].PdrDf.median())
# prints standard deviation of stock price for each stock
print("std")
# Creates dataframe with daily return for each stock
daily_return = py_tickers[0].PdrDf.pct_change()
pprint(py_tickers[0].PdrDf.std())
# prints mean daily return for each stock
print("mean daily")
pprint(daily_return.mean().tail())
# prints standard deviation of daily returns for each stock
print("std daily")
pprint(daily_return.std().tail())
# Rolling mean and standard deviation
# simple moving average
print("mean daily simple moving average")
pprint(daily_return.rolling(window=20).mean().tail())
print("std daily simple moving average")
pprint(daily_return.rolling(window=20).std().tail())
# exponential moving average
print("mean daily exponential moving average")
pprint(daily_return.ewm(span=20, min_periods=20).mean().tail())
print("std daily exponential moving average")
pprint(daily_return.ewm(span=20, min_periods=20).std().tail())
exit(7)
# Handling NaN Values
# Replaces NaN values with the next valid value along the column
pdr_adjclose_df.fillna(method='bfill', axis=0, inplace=True)
# Creates dataframe with daily return for each stock
daily_return = pdr_adjclose_df.pct_change()
# Data vizualization
# Plot of all the stocks superimposed on the same chart
pdr_adjclose_df.plot()
