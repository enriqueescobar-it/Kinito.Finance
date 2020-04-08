#!/usr/bin/env python
# coding: utf-8
# ## Calculating the Return of Indices
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Consider three famous American market indices – Dow Jones, S&P 500, and the Nasdaq for the period of 1st of January 2000 until today.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
tickers = ['^DJI', '^GSPC', '^IXIC', '^GDAXI']
ind_data = pd.DataFrame()
for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Adj Close']
ind_data.head()
ind_data.tail()
# Normalize the data to 100 and plot the results on a graph. 
(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()
# How would you explain the common and the different parts of the behavior of the three indices?
# Obtain the simple returns of the indices.
ind_returns = (ind_data / ind_data.shift(1)) - 1
ind_returns.tail()
# Estimate the average annual return of each index.
annual_ind_returns = ind_returns.mean() * 250
annual_ind_returns
