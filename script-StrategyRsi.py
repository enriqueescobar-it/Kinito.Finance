#from Common.Plotters.Strategies.RsiStrategyPlotter import RsiStrategyPlotter
from Common.Plotters.TechIndicators.RsiIndicatorPlotter import RsiIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
#from Common.Strategies.TechIndicators.RsiStrategy import RsiStrategy
from Common.TechIndicators.RsiIndicator import RsiIndicator

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: RsiIndicator = RsiIndicator(yahooStockOption)
print(yahooStockIndicator._label)
yahooStockIndicatorPlotter: RsiIndicatorPlotter = RsiIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
#yahooStockStrategy: RsiStrategy = RsiStrategy(yahooStockIndicator, yahooStockOption)
#yahooStockStrategyPlotter: RsiStrategyPlotter = RsiStrategyPlotter(yahooStockOption, yahooStockStrategy).Plot()
#yahooStockStrategyPlotter.show()
