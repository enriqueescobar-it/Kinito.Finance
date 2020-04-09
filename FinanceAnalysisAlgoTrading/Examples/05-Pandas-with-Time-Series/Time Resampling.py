#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# <center>*Copyright Pierian Data 2017*</center>
# <center>*For more information, visit us at www.pieriandata.com*</center>

# # Time Resampling
# 
# Let's learn how to sample time series data! This will be useful later on in the course!

# In[30]:


import numpy as np
import pandas as pd


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[2]:


# Grab data
# Faster alternative
# df = pd.read_csv('time_data/walmart_stock.csv',index_col='Date')
df = pd.read_csv('time_data/walmart_stock.csv')


# In[3]:


df.head()


# Create a date index from the date column

# In[4]:


df['Date'] = df['Date'].apply(pd.to_datetime)


# In[5]:


df.head()


# In[6]:


df.set_index('Date',inplace=True)


# In[8]:


df.head()


# ## resample()
# 
# A common operation with time series data is resamplling based on the time series index. Let see how to use the resample() method.
# 
# #### All possible time series offest strings

# <table border="1" class="docutils">
# <colgroup>
# <col width="13%" />
# <col width="87%" />
# </colgroup>
# <thead valign="bottom">
# <tr class="row-odd"><th class="head">Alias</th>
# <th class="head">Description</th>
# </tr>
# </thead>
# <tbody valign="top">
# <tr class="row-even"><td>B</td>
# <td>business day frequency</td>
# </tr>
# <tr class="row-odd"><td>C</td>
# <td>custom business day frequency (experimental)</td>
# </tr>
# <tr class="row-even"><td>D</td>
# <td>calendar day frequency</td>
# </tr>
# <tr class="row-odd"><td>W</td>
# <td>weekly frequency</td>
# </tr>
# <tr class="row-even"><td>M</td>
# <td>month end frequency</td>
# </tr>
# <tr class="row-odd"><td>SM</td>
# <td>semi-month end frequency (15th and end of month)</td>
# </tr>
# <tr class="row-even"><td>BM</td>
# <td>business month end frequency</td>
# </tr>
# <tr class="row-odd"><td>CBM</td>
# <td>custom business month end frequency</td>
# </tr>
# <tr class="row-even"><td>MS</td>
# <td>month start frequency</td>
# </tr>
# <tr class="row-odd"><td>SMS</td>
# <td>semi-month start frequency (1st and 15th)</td>
# </tr>
# <tr class="row-even"><td>BMS</td>
# <td>business month start frequency</td>
# </tr>
# <tr class="row-odd"><td>CBMS</td>
# <td>custom business month start frequency</td>
# </tr>
# <tr class="row-even"><td>Q</td>
# <td>quarter end frequency</td>
# </tr>
# <tr class="row-odd"><td>BQ</td>
# <td>business quarter endfrequency</td>
# </tr>
# <tr class="row-even"><td>QS</td>
# <td>quarter start frequency</td>
# </tr>
# <tr class="row-odd"><td>BQS</td>
# <td>business quarter start frequency</td>
# </tr>
# <tr class="row-even"><td>A</td>
# <td>year end frequency</td>
# </tr>
# <tr class="row-odd"><td>BA</td>
# <td>business year end frequency</td>
# </tr>
# <tr class="row-even"><td>AS</td>
# <td>year start frequency</td>
# </tr>
# <tr class="row-odd"><td>BAS</td>
# <td>business year start frequency</td>
# </tr>
# <tr class="row-even"><td>BH</td>
# <td>business hour frequency</td>
# </tr>
# <tr class="row-odd"><td>H</td>
# <td>hourly frequency</td>
# </tr>
# <tr class="row-even"><td>T, min</td>
# <td>minutely frequency</td>
# </tr>
# <tr class="row-odd"><td>S</td>
# <td>secondly frequency</td>
# </tr>
# <tr class="row-even"><td>L, ms</td>
# <td>milliseconds</td>
# </tr>
# <tr class="row-odd"><td>U, us</td>
# <td>microseconds</td>
# </tr>
# <tr class="row-even"><td>N</td>
# <td>nanoseconds</td>
# </tr>
# </tbody>
# </table>

# In[14]:


# Our index
df.index


# You need to call resample with the rule parameter, then you need to call some sort of aggregation function. This is because due to resampling, we need some sort of mathematical rule to join the rows by (mean,sum,count,etc...)

# In[17]:


# Yearly Means
df.resample(rule='A').mean()


# ### Custom Resampling
# 
# You could technically also create your own custom resampling function:

# In[23]:


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
