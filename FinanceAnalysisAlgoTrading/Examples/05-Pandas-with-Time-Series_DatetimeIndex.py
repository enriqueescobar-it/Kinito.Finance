#!/usr/bin/env python
# coding: utf-8
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# <center>*Copyright Pierian Data 2017*</center>
# <center>*For more information, visit us at www.pieriandata.com*</center>
# # Introduction to Time Series with Pandas
# 
# A lot of our financial data will have a datatime index, so let's learn how to deal with this sort of data with pandas!
# In[15]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# In[2]:
from datetime import datetime
# In[3]:
# To illustrate the order of arguments
my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15
# In[4]:
# January 2nd, 2017
my_date = datetime(my_year,my_month,my_day)
# In[5]:
# Defaults to 0:00
my_date 
# In[6]:
# January 2nd, 2017 at 13:30:15
my_date_time = datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)
# In[7]:
my_date_time
# You can grab any part of the datetime object you want
# In[8]:
my_date.day
# In[9]:
my_date_time.hour
# ### Pandas with Datetime Index
# 
# You'll usually deal with time series as an index when working with pandas dataframes obtained from some sort of financial API. Fortunately pandas has a lot of functions and methods to work with time series!
# In[13]:
# Create an example datetime list/array
first_two = [datetime(2016, 1, 1), datetime(2016, 1, 2)]
first_two
# In[14]:
# Converted to an index
dt_ind = pd.DatetimeIndex(first_two)
dt_ind
# In[29]:
# Attached to some random data
data = np.random.randn(2,2)
print(data)
cols = ['A','B']
# In[28]:
df = pd.DataFrame(data,dt_ind,cols)
# In[30]:
df
# In[31]:
df.index
# In[34]:
# Latest Date Location
df.index.argmax()
# In[35]:
df.index.max()
# In[37]:
# Earliest Date Index Location
df.index.argmin()
# In[38]:
df.index.min()
# ## Great, let's move on!
