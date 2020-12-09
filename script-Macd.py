from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy

yahooStockOption: YahooStockOption = YahooStockOption('ESTC')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: MacdIndicator = MacdIndicator(yahooStockOption)
print('Column=', yahooStockIndicator.Column)
print('Data=', yahooStockIndicator.DataFrame.columns)
print('FigStyle=', yahooStockIndicator.FigStyle)
print('Label=', yahooStockIndicator.Label)
print('LabelX=', yahooStockIndicator.LabelX)
print('LabelXangle=', yahooStockIndicator.LabelXangle)
print('LabelY=', yahooStockIndicator.LabelY)
print('LabelMain=', yahooStockIndicator.LabelMain)
print('LegendPlace=', yahooStockIndicator.LegendPlace)
print('Name=', yahooStockIndicator.Name)
print('Source=', yahooStockIndicator.Source)
yahooStockStrategy: MacdStrategy = MacdStrategy(yahooStockIndicator)
#yahooStockStrategy.Plot().show()
yahooStockStrategy.PlotAll().show()
