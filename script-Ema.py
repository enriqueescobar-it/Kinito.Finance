from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.EmaIndicator import EmaIndicator
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy

yahooStockOption: YahooStockOption = YahooStockOption('ESTC')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: EmaIndicator = EmaIndicator(yahooStockOption)
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
yahooStockStrategy: EmaStrategy = EmaStrategy(yahooStockIndicator)
#yahooStockStrategy.Plot().show()
yahooStockStrategy.PlotAll().show()
