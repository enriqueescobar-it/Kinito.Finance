from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex


class SnPTSXCompositeIndex(AbstractStockMarketIndex):

    def __init__(self):
        self.__ticker = '^GSPTSE'
