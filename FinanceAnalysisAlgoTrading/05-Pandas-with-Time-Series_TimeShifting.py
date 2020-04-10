#!/usr/bin/env python
# coding: utf-8
# # Time Shifting
# Sometimes you may need to shift all your data up or down along the time series index,
# in fact, a lot of pandas built-in methods do this under the hood.
# This isn't something we won't do often in the course, but its definitely good to know about this anyways!
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Data/05-Pandas-with-Time-Series_walmart_stock.csv',index_col='Date')
df.index = pd.to_datetime(df.index)
df.tail()
# ## .shift() forward
df.shift(1).head()
# You will lose that last piece of data that no longer has an index!
df.shift(1).tail()
# ## shift() backwards
df.shift(-1).head()
df.shift(-1).tail()
# ## Shifting based off Time String Code 
# ### Using tshift()
# Shift everything forward one month
df.tshift(periods=1,freq='M').head()
# That is it for now!
