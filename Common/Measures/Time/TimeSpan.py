from datetime import datetime, date
import datetime as dt
from datetime import timedelta
from datetime import *
from dateutil.relativedelta import *
import calendar
import arrow
import moment
import time
from freezegun import freeze_time
from delorean import Delorean


class TimeSpan(object):
    StartDate: datetime
    EndDate: datetime
    StartDateStr: str
    EndDateStr: str
    MonthCount: int

    def __init__(self):
        self.EndDateStr = datetime.today().strftime('%Y-%m-%d')
        self.EndDate = dt.date(*(int(s) for s in self.EndDateStr.split('-')))
        self.StartDate = self.EndDate - timedelta(days=5 * 365.25)
        self.StartDateStr = self.StartDate.strftime('%Y-%m-%d')
        self.MonthCount = (self.EndDate.year - self.StartDate.year) * 12 + (self.EndDate.month - self.StartDate.month)
