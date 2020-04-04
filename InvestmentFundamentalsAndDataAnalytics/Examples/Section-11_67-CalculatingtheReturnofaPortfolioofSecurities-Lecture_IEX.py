#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[ ]:
tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='google', start='2002-1-1')['Close']
# In[ ]:
mydata.info()
# In[ ]:
mydata.head()
# In[ ]:
mydata.tail()
# ### Normalization to 100:
# 
# $$
# \frac {P_t}{P_0} * 100
# $$
# In[ ]:
mydata.iloc[0]
# In[ ]:
(mydata / mydata.iloc[0] * 100).plot(figsize = (15, 6));
plt.show()
# In[ ]:
mydata.plot(figsize=(15,6))
plt.show()
# In[ ]:
mydata.loc['2002-01-02']
# In[ ]:
mydata.iloc[0]
# ## Calculating the Return of a Portfolio of Securities
# In[ ]:
returns = (mydata / mydata.shift(1)) - 1
returns.head()
# In[ ]:
weights = np.array([0.25, 0.25, 0.25, 0.25])
# In[ ]:
np.dot(returns, weights)
# ***
# In[ ]:
annual_returns = returns.mean() * 250
annual_returns
# In[ ]:
np.dot(annual_returns, weights)
# In[ ]:
pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + ' %'
print pfolio_1
# ***
# In[ ]:
weights_2 = np.array([0.4, 0.4, 0.15, 0.05])
# In[ ]:
pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + ' %'
print pfolio_1
print pfolio_2
