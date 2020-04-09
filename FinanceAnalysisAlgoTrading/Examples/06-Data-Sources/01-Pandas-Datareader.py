#!/usr/bin/env python
# coding: utf-8

# # Pandas Datareader
# 
# ** NOTE: Not every geographical location works well with pandas datareader, your firewall may also block it!**
# 
# Functions from pandas_datareader.data and pandas_datareader.wb extract data from various Internet sources into a pandas DataFrame. Currently the following sources are supported:
# 
# * Yahoo! Finance
# * Google Finance
# * Enigma
# * St.Louis FED (FRED)
# * Kenneth French’s data library
# * World Bank
# * OECD
# * Eurostat
# * Thrift Savings Plan
# * Oanda currency historical rate
# * Nasdaq Trader symbol definitions (remote_data.nasdaq_symbols)
# 
# It should be noted, that various sources support different kinds of data, so not all sources implement the same methods and the data elements returned might also differ.

# In[3]:


import pandas_datareader.data as web

import datetime

start = datetime.datetime(2015, 1, 1)

end = datetime.datetime(2017, 1, 1)

facebook = web.DataReader("FB", 'google', start, end)


# In[4]:


facebook.head()


# ### Experimental Options
# 
# The Options class allows the download of options data from Google Finance.
# 
# The get_options_data method downloads options data for specified expiry date and provides a formatted DataFrame with a hierarchical index, so its easy to get to the specific option you want.
# 
# Available expiry dates can be accessed from the expiry_dates property.

# In[5]:


from pandas_datareader.data import Options

fb_options = Options('FB', 'google')


# In[8]:


data = fb_options.get_options_data(expiry=fb_options.expiry_dates[0])


# In[10]:


data.head()


# # FRED

# In[11]:


import pandas_datareader.data as web

import datetime

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2017, 1, 1)

gdp = web.DataReader("GDP", "fred", start, end)


# In[12]:


gdp.head()


# In[ ]:




