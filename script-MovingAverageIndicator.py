'''
from Common.Plotters.TechIndicators.RsiPlotter import RsiPlotter
'''
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MovingAverageIndicator import MovingAverageIndicator

yahooStockOption: YahooStockOption = YahooStockOption('TD')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator = MovingAverageIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
