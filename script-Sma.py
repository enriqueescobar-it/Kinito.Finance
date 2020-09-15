from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.SmaIndicator import SmaIndicator
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
# MWK YCBD GRWG FSZ AMZN CGO RCI PPL SJR.B AQN CP CNI TD KL WCN BPY OTEX
# BCE ZWB CM KEY VNR ENB TFII LMT WMT RY BRKB GNW IT
#ETFs# BRTXQ FZILX FSRNX VTSAX
# TFII LSPD T FTS RY
yahooStockOption: YahooStockOption = YahooStockOption('OTEX')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: SmaIndicator = SmaIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockStrategy: SmaStrategy = SmaStrategy(yahooStockIndicator)
yahooStockStrategy.Plot().show()
