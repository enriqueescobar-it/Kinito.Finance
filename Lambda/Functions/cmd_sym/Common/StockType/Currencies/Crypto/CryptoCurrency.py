from yahooquery import Ticker

#
from Common.Readers.Engine.YahooFinEngine import YahooFinEngine
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency


#

class CryptoCurrency(AbstractCurrency):
    #__ticker: str = 'NA'
    #_y_query: Ticker
    #

    def __init__(self, c_name: str, t_name: str, q_type: str):
        super().__init__(c_name.replace(' ', '').replace('-', ''), q_type)
        #
        self._ticker = t_name
        self._class_type = 'CryptoCurrency'
        self._info_type = self._class_type + 'Info'
        #self.__quote_type = q_type
        #
        self._y_query = Ticker(t_name)
        self._y_fin_engine = YahooFinEngine(t_name)
        #
        self._set_info()

    def __str__(self) -> str:
        return super(CryptoCurrency, self).__str__()
