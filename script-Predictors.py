from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Predictors.AbstractPredictor import AbstractPredictor
from Common.Predictors.Tree.DecisionTreePredictor import DecisionTreePredictor
from Common.Predictors.Linear.LinearPredictor import LinearPredictor

yahooStockOption: YahooStockOption = YahooStockOption('AAPL')
print(yahooStockOption.HistoricalData.describe(include='all'))
predictor_list = []
abstractPredictor: AbstractPredictor =\
    LinearPredictor(60, 'Adj Close', yahooStockOption.HistoricalData, yahooStockOption.TimeSpan)
