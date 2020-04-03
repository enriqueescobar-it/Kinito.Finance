#!/usr/bin/env python
# coding: utf-8

# In all our analyses, we used estimations for either simple or logarithmic rates of return. <br/>
# The formula for simple returns is
# 
# $$
# \frac{P_t - P_{t-1}}{P_{t-1}}
# ,$$
# 
# while the formula for log returns is
# 
# $$
# ln( \frac{P_t}{P_{t-1}} )
# .$$
# 
# <br/>
# If our dataset is simply called "data", in Python, we could write the first formula as  <br/ >
# 
# *(data / data.shift(1)) - 1,*
# 
# and the second one as
# 
# *np.log(data / data.shift(1)).*
# 
# <br/>
# Instead of coding it this way, some professionals prefer using **Pandas.DataFrame.pct_change()** method, as it computes simple returns directly. We will briefly introduce it to you in this notebook document.

# First, let's import NumPy, Pandas, and pandas_datareader.

# In[1]:


import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  


# We will calculate returns of the Procter and Gamble stock, based on adjusted closing price data since the 1st of January 2007.

# In[2]:


ticker = 'PG' 
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']


# So far, we estimated simple returns in the following way.

# In[3]:


s_rets_1 = (data / data.shift(1)) - 1
s_rets_1.head()


# Observe the .pct_change() method can obtain an identical result.

# In[4]:


s_rets_2 = data.pct_change()
s_rets_2.head()


# Now, if you multiply the obtained values by 100, you will see the percentage change:

# In[5]:


s_rets_2.head() * 100


# This means the close price on 2007-01-04 was 0.76% lower than the price on 2007-01-03, the price on 2007-01-05 was 0.85% lower than the price on 2007-01-04, and so on.

# A few arguments can be used in the percentage change method. The most important one is 'period' as it specifies the difference between prices in the nominator. By default, it equals one, and that's why we obtained the same result for s_rets_1 and s_rets_2. Let's assume we would like to calculate simple returns with the following formula: 
# 
# $$
# \frac{P_t - P_{t-2}}{P_{t-2}}
# ,$$

# Then, we should specify 'periods = 2' in parentheses: 

# In[6]:


s_rets_3 = data.pct_change(periods=2)
s_rets_3.head()


# You can see there was no value obtained not only for the first, but also for the second observation. If we use the "old" formula, and not this method, *shift(2)* would lead us to the same output:

# In[7]:


s_rets_4 = (data / data.shift(2)) - 1
s_rets_4.head()


# Great! <br/>
# 
# Now, let's consider logarithmic returns. To this moment, we applied the following formula:

# In[8]:


log_rets_1 = np.log(data / data.shift(1))
log_rets_1.tail()


# You can calculate the same formula for log returns with the help of the .pct_change() method. Just be careful with the way you apply the formula! Mathematically, it will look like this:
# 
# $$
# ln(\frac{P_t}{P_{t-1}} ) = ln( \frac{P_t - P_{t-1}}{P_{t-1}} + \frac{P_{t-1}}{P_{t-1}}) = ln(\ simple.returns + 1)
# .$$

# In[9]:


log_rets_2 = np.log(data.pct_change() + 1)
log_rets_2.tail()


# ***

# The .pct_change() method is very popular. Whether you include it in your code or you go the other way around and type the formulas as we did in our analyses, you should obtain the correct value for the returns you need.
