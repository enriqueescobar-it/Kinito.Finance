#from Common.Plotters.TechIndicators.SmaStrategyPlotter import SmaStrategyPlotter
from Common.Plotters.TechIndicators.SmaIndicatorPlotter import SmaIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
from Common.TechIndicators.SmaIndicator import SmaIndicator

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: SmaIndicator = SmaIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
yahooStockIndicatorPlotter: SmaIndicatorPlotter =\
    SmaIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
yahooStockStrategy: SmaStrategy =\
    SmaStrategy(yahooStockIndicator, yahooStockOption)
yahooStockStrategyPlotter =\
    1
