#!/usr/bin/env python
# coding: utf-8
# Time Resampling
# Let's learn how to sample time series data! This will be useful later on in the course!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Grab data
# Faster alternative
# df = pd.read_csv('Data/05-Pandas-with-Time-Series_walmart_stock.csv',index_col='Date')
df = pd.read_csv('Data/05-Pandas-with-Time-Series_walmart_stock.csv')
df.head()
# Create a date index from the date column
df['Date'] = df['Date'].apply(pd.to_datetime)
df.head()
# In[6]:
df.set_index('Date',inplace=True)
df.head()
# ## resample()
# A common operation with time series data is resamplling based on the time series index. Let see how to use the resample() method.
# #### All possible time series offest strings
# Our index
df.index
# You need to call resample with the rule parameter, then you need to call some sort of aggregation function.
# This is because due to resampling, we need some sort of mathematical rule to join the rows by (mean,sum,count,etc...)
# Yearly Means
df.resample(rule='A').mean()
# ### Custom Resampling
# You could technically also create your own custom resampling function:
def first_day(entry):
    """
    Returns the first instance of the period, regardless of samplling rate.
    """
    return entry[0]
# In[25]:
df.resample(rule='A').apply(first_day)
# In[38]:
df['Close'].resample('A').mean().plot(kind='bar')
plt.title('Yearly Mean Close Price for Walmart')
# In[42]:
df['Open'].resample('M').max().plot(kind='bar',figsize=(16,6))
plt.title('Monthly Max Opening Price for Walmart')
# That is it! Up next we'll learn about time shifts!
