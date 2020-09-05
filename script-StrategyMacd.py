from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy
from Common.Plotters.Strategies.MacdStrategyPlotter import MacdStrategyPlotter

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: MacdIndicator = MacdIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockIndicator.PlotData().show()
'''
yahooStockIndicatorPlotter: MacdIndicatorPlotter = MacdIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
yahooStockStrategy: MacdStrategy = MacdStrategy(yahooStockIndicator, yahooStockOption)
yahooStockStrategyPlotter: MacdStrategyPlotter = MacdStrategyPlotter(yahooStockOption, yahooStockStrategy).Plot()
yahooStockStrategyPlotter.show()'''
