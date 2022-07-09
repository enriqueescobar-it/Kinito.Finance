import argparse


# construct the argument parse and parse the arguments
from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo
from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
args = vars(ap.parse_args())
a_sym: str = args["symbol"]
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol?".format(a_sym))
a_ticker: str = args["symbol"]

ati: AbstractTimeInfo = AbstractTimeInfo()
print(ati.stop_datetime)
atsi: AbstractTimeSpanInfo = AbstractTimeSpanInfo()
print(atsi.stop_datetime)
print(atsi.start_datetime)