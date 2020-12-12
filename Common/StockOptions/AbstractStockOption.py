from abc import *
from typing import List
from pandas import DataFrame
from numpy import ndarray
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.FinVizEngine import FinVizEngine
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper


class AbstractStockOption(ABC):
    IsDaily: bool = False
    IsWeekly: bool = False
    IsMonthly: bool = False
    IsQuarterly: bool = False
    IsAnnually: bool = False
    _source: str = 'yahoo'
    _column: str = 'Adj Close'
    _ticker: str = 'TD'
    _price: float = -1.1
    _high52: float = -1.1
    _low52: float = -1.1
    _range52: List[float]
    _sigma: float = -1.1
    _mu: float = -1.1
    _median: float = -1.1
    _norm_pdf: ndarray
    _data_range: ndarray
    _t_s: TimeSpan = TimeSpan()
    _data: DataFrame
    _historical: DataFrame
    _fin_viz_engine: FinVizEngine
    _y_finance_engine: YahooFinanceEngine
    _yahooSummaryScrapper: YahooSummaryScrapper

    @property
    def Column(self):
        return self._column

    @property
    def Data(self):
        return self._data

    @property
    def DataFrame(self):
        return self._historical

    @property
    def Price(self):
        return self._price

    @property
    def Source(self):
        return self._source

    @property
    def Ticker(self):
        return self._ticker

    @property
    def TimeSpan(self):
        return self._t_s

    @property
    def High52(self):
        return self._high52

    @property
    def Low52(self):
        return self._low52

    @property
    def Range52(self):
        return self._range52

    @property
    def DataRange(self):
        return self._data_range

    @property
    def Mu(self):
        return self._mu

    @property
    def Median(self):
        return self._median

    @property
    def Sigma(self):
        return self._sigma

    @property
    def NormProbDensityFn(self):
        return self._norm_pdf
