from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('TD')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockOptionPlotter: HistoricalPlotter = HistoricalPlotter(yahooStockOption.HistoricalData, yahooStockOption.Source, yahooStockOption.Ticker, yahooStockOption.TimeSpan).Plot()
yahooStockOptionPlotter.show()
