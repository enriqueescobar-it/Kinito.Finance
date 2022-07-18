import argparse
from datetime import datetime

import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_nyse

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo
from Common.InfoType.Times.DateTimeInfo import DateTimeInfo
from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo
from Common.InfoType.Times.Spans.QuarterSpanInfo import QuarterSpanInfo
from Common.InfoType.Times.Spans.TimeSpanInfo import TimeSpanInfo
from Common.InfoType.Times.Spans.YearSpanInfo import YearSpanInfo

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
args = vars(ap.parse_args())
a_sym: str = args["symbol"]
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol?".format(a_sym))
a_ticker: str = args["symbol"]

dti: DateTimeInfo = DateTimeInfo()
print(dti.to_json())
print(dti)

ati: AbstractTimeInfo = AbstractTimeInfo()
print(ati.to_json())
print(ati)

atsi: AbstractTimeSpanInfo = AbstractTimeSpanInfo(datetime.now())
print(atsi.to_json())
print(atsi)

qsi: QuarterSpanInfo = QuarterSpanInfo(datetime.now())
print(qsi.to_json())
print(qsi)

ysi: YearSpanInfo = YearSpanInfo(datetime.now())
print(ysi.to_json())
print(ysi)

tsi: TimeSpanInfo = TimeSpanInfo(datetime.now())
print(tsi.to_json())
print(tsi)
print(mcal.get_calendar_names())
nyse: exchange_calendar_nyse.NYSEExchangeCalendar = mcal.get_calendar('NYSE')
print(type(nyse), type(nyse.tz), nyse.tz.zone)
