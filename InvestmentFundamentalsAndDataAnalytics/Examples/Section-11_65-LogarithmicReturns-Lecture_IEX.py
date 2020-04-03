#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[ ]:


PG = wb.DataReader('PG', data_source='iex', start='2015-1-1')


# In[ ]:


PG.head()


# In[ ]:


PG.tail()


# ## Simple Rate of Return

# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$

# In[ ]:


PG['simple_return'] = (PG['close'] / PG['close'].shift(1)) - 1
print (PG['simple_return'])


# In[ ]:


PG['simple_return'].plot(figsize=(8, 5))
plt.show()


# In[ ]:


avg_returns_d = PG['simple_return'].mean()
avg_returns_d


# In[ ]:


avg_returns_a = PG['simple_return'].mean() * 250
avg_returns_a


# In[ ]:


print (str(round(avg_returns_a, 5) * 100) + ' %')


# ## Log Returns

# $$
# ln(\frac{P_t}{P_{t-1}})
# $$

# In[ ]:


PG.head()


# In[ ]:


PG['log_return'] = np.log(PG['close'] / PG['close'].shift(1))
print (PG['log_return'])


# In[ ]:


PG['log_return'].plot(figsize=(8, 5))
plt.show()


# In[ ]:


log_return_d = PG['log_return'].mean()
log_return_d


# In[ ]:


log_return_a = PG['log_return'].mean() * 250
log_return_a


# In[ ]:


print (str(round(log_return_a, 5) * 100) + ' %')

