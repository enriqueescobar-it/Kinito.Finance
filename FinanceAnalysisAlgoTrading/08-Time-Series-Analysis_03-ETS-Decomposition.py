#!/usr/bin/env python
# coding: utf-8
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# <center>*Copyright Pierian Data 2017*</center>
# <center>*For more information, visit us at www.pieriandata.com*</center>
# In[45]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
# In[39]:
airline = pd.read_csv('airline_passengers.csv',index_col="Month")
# In[40]:
airline.head()
# In[41]:
airline.plot()
# ## ETS
# 
# We can use an additive model when it seems that the trend is more linear and the seasonality and trend components seem to be constant over time (e.g. every year we add 10,000 passengers). A multiplicative model is more appropriate when we are increasing (or decreasing) at a non-linear rate (e.g. each year we double the amount of passengers).
# 
# Based off this chart, it looks like the trend in these earlier days is slightly increasing at a higher rate than just linear (although it is a  bit hard to tell from this one plot).
# In[51]:
# Get data in correct format
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)
# In[52]:
airline.head()
# In[58]:
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')
result.plot()
# In[59]:
# You may accidentally see two of the same plots here, not to worry,
# just a small bug with statsmodels function.
