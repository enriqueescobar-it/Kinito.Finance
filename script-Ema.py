from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.EmaIndicator import EmaIndicator
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy

yahooStockOption: YahooStockOption = YahooStockOption('ESTC')
print(yahooStockOption.DataFrame.describe(include='all'))
yahooStockIndicator: EmaIndicator = EmaIndicator(yahooStockOption)
print('Column=', yahooStockIndicator.Column)
print('Data=', yahooStockIndicator.GetData().columns)
print('FigSize=', yahooStockIndicator.FigSizeTuple)
print('FigStyle=', yahooStockIndicator.FigStyle)
print('Label=', yahooStockIndicator.Label)
print('LabelX=', yahooStockIndicator.LabelX)
print('LabelXangle=', yahooStockIndicator.LabelXangle)
print('LabelY=', yahooStockIndicator.LabelY)
print('LabelMain=', yahooStockIndicator.LabelMain)
print('LegendPlace=', yahooStockIndicator.LegendPlace)
print('LowHigh=', yahooStockIndicator.LowMedHighTuple)
print('Name=', yahooStockIndicator.Name)
print('Source=', yahooStockIndicator.Source)
yahooStockIndicator.PlotData().show()
yahooStockStrategy: EmaStrategy = EmaStrategy(yahooStockIndicator)
yahooStockStrategy.Plot().show()
yahooStockStrategy.PlotAll().show()
