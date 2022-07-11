import argparse

from datetime import datetime
# construct the argument parse and parse the arguments

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo
from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo
from Common.InfoType.Times.Spans.QuarterSpanInfo import QuarterSpanInfo
from Common.InfoType.Times.Spans.YearSpanInfo import YearSpanInfo

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
args = vars(ap.parse_args())
a_sym: str = args["symbol"]
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol?".format(a_sym))
a_ticker: str = args["symbol"]

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

