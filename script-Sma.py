from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.SmaIndicator import SmaIndicator
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
# MWK YCBD GRWG FSZ AMZN CGO RCI PPL SJR.B AQN CP CNI TD KL WCN BPY OTEX
# BCE ZWB CM KEY VNR ENB TFII LMT WMT RY BRKB GNW IT KO QQQ VZ NKE
#ETFs# BRTXQ FZILX FSRNX VTSAX
# TFII LSPD T FTS RY
# ACES AMT AMZN AQN ARKF ARKK BCE BPY BRK-B BRKB BRTXQ CCA CGO CM CNI COST CP ENB FIE FSRNX FSZ FTS FZILX FZROX
# GNW GRWG HQU HZU IT JNUG KEY KL KO LMT LSPD MA MWK NKE NPI OTEX PPL QQC-f QQQ RCI RCI.B RY SHOP SJR.B SOXL
# T TD TEC.TO TFII VDC VFV VGT VNR VPU VTSAX VYM VZ WCN WELL WMT XEI XIT YCBD ZQQ ZWB
yahooStockOption: YahooStockOption = YahooStockOption('OTEX')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: SmaIndicator = SmaIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockStrategy: SmaStrategy = SmaStrategy(yahooStockIndicator)
yahooStockStrategy.Plot().show()
