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
    YearCount: int
    QuarterCount: int
    MonthCount: int
    WeekCount: int
    DayCount: int
    HourCount: int

    def __init__(self):
        self.EndDateStr = datetime.today().strftime('%Y-%m-%d')
        self.EndDate = dt.date(*(int(s) for s in self.EndDateStr.split('-')))
        self.StartDate = self.EndDate - timedelta(days=5 * 365.25)
        # self.StartDate = self.EndDate - relativedelta(years=5)
        self.StartDateStr = self.StartDate.strftime('%Y-%m-%d')
        self.__setYearCount()
        self.__setMonthCount()
        self.__setWeekCount()
        self.__setDayCount()
        self.__setHourCount()

    def __setYearCount(self):
        self.YearCount = relativedelta(self.EndDate, self.StartDate).years
        self.QuarterCount = relativedelta(self.EndDate, self.StartDate).months % 3
        self.__setMonthCount()

    def __setMonthCount(self):
        self.MonthCount = self.YearCount * 12
        self.MonthCount += relativedelta(self.EndDate, self.StartDate).months

    def __setWeekCount(self):
        self.WeekCount = self.YearCount * 52
        self.WeekCount += relativedelta(self.EndDate, self.StartDate).weeks

    def __setDayCount(self):
        self.DayCount = int(round(self.YearCount * 365.25))
        self.DayCount += int(round(relativedelta(self.EndDate, self.StartDate).months * 30.4375))
        self.DayCount += self.EndDate.day

    def __setHourCount(self):
        self.HourCount = relativedelta(self.EndDate, self.StartDate).hours
