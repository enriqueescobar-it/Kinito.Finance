from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.SmaIndicator import SmaIndicator
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
from Common.Plotters.Strategies.SmaStrategyPlotter import SmaStrategyPlotter

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: SmaIndicator = SmaIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockIndicator.PlotData().show()
'''
yahooStockIndicatorPlotter: SmaIndicatorPlotter = SmaIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
yahooStockStrategy: SmaStrategy = SmaStrategy(yahooStockIndicator, yahooStockOption)
yahooStockStrategyPlotter: SmaStrategyPlotter = SmaStrategyPlotter(yahooStockOption, yahooStockStrategy).Plot()
yahooStockStrategyPlotter.show()'''
