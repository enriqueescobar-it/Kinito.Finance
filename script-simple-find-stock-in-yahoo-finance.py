#!/usr/bin/python3
import datetime as dateTime
import matplotlib.pyplot as matPyPlot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as dataReader

style.use('ggplot')

start = dateTime.datetime(2019, 1, 1)
stop_ = dateTime.datetime.now()
# try to update your "pandas_datereader" and then use "stooq" or "iex" instead of "morningstar":
df = dataReader.DataReader("TSLA", 'stooq', start, stop_)
print(df.head())
exit(11)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())


