#!/usr/bin/env python
# coding: utf-8
## Monte Carlo - Black-Scholes-Merton
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Download the data for Microsoft (‘MSFT’) from Yahoo Finance for the period ‘2000-1-1’ until today.
# Download the data for Microsoft (‘MSFT’) from IEX for the period ‘2015-1-1’ until today.
# We have written a few lines of code that will import the documents you need and define the functions estimating d1, d2, and the Black-Scholes-Merton formula. 
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
# $$
# d_1 = \frac{\ln(\frac{S}{K}) + (r + \frac{stdev^2}{2})t}{s \cdot \sqrt{t}}
# $$
# $$
# d_2 = d_1 - s \cdot \sqrt{t} = \frac{\ln(\frac{S}{K}) + (r - \frac{stdev^2}{2})t}{s \cdot \sqrt{t}}
# $$
data = pd.read_csv('Section-17_MSFT_2000.csv', index_col = 'Date')
# In[2]:
def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
 
def d2(S0, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
def BSM(S, K, r, stdev, T):
        return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))
# Store the annual standard deviation of the log returns in a variable, called “stdev”.
# In[3]:
log_returns = np.log(1 + data.pct_change())
log_returns.tail()
# In[5]:
stdev = log_returns.std() * 250 ** 0.5
stdev
# Set the risk free rate, r, equal to 2.5% (0.025); the strike price, K, equal to 110.0; and the time horizon, T, equal to 1, respectively.
r = 0.025
K = 110.0
T = 1
# Create a variable S equal to the last adjusted closing price of Microsoft. Use the “iloc” method.
# In[7]:
S = data.iloc[-1]
S
# Call the d1 and d2 functions with the relevant arguments to obtain their values.
d1(S, K, r, stdev, T)
d2(S, K, r, stdev, T)
# Use the BSM function to estimate the price of a call option, given you know the values of S, K, r, stdev, and T.
BSM(S, K, r, stdev, T)
