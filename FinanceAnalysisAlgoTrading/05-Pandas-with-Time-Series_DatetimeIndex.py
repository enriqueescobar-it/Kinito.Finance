#!/usr/bin/env python
# coding: utf-8
# # Introduction to Time Series with Pandas
# A lot of our financial data will have a datatime index, so let's learn how to deal with this sort of data with pandas!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# To illustrate the order of arguments
my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15
# January 2nd, 2017
my_date = datetime(my_year,my_month,my_day)
# Defaults to 0:00
my_date
# January 2nd, 2017 at 13:30:15
my_date_time = datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)
my_date_time
# You can grab any part of the datetime object you want
my_date.day
my_date_time.hour
# ### Pandas with Datetime Index
# You'll usually deal with time series as an index when working with pandas dataframes obtained from some sort of financial API. Fortunately pandas has a lot of functions and methods to work with time series!
# Create an example datetime list/array
first_two = [datetime(2016, 1, 1), datetime(2016, 1, 2)]
first_two
# Converted to an index
dt_ind = pd.DatetimeIndex(first_two)
dt_ind
# Attached to some random data
data = np.random.randn(2,2)
print(data)
cols = ['A','B']
df = pd.DataFrame(data,dt_ind,cols)
df
df.index
# Latest Date Location
df.index.argmax()
# In[35]:
df.index.max()
# Earliest Date Index Location
df.index.argmin()
# In[38]:
df.index.min()
# ## Great, let's move on!
