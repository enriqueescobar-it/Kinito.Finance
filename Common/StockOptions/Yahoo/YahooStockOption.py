from Common.StockOptions.AbstractStockOption import AbstractStockOption
from datetime import datetime
import datetime as dt
from datetime import timedelta


class YahooStockOption(AbstractStockOption):
    StartDateStr: str
    EndDateStr: str
    StartDate: datetime
    EndDate: datetime

    def __init__(self):
        self.EndDateStr = datetime.today().strftime('%Y-%m-%d')
        self.EndDate = dt.date(*(int(s) for s in self.EndDateStr .split('-')))
        self.StartDate = self.EndDate - timedelta(days=5*365.25)
        self.StartDateStr = self.StartDate.strftime('%Y-%m-%d')
        self.Source = 'yahoo'
