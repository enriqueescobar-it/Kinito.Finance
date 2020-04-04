#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# In[ ]:
assets = ['PG', '^GSPC']
pf_data = pd.read_csv('D:\Python\Markowitz_Data.csv', index_col = 'Date')
# In[ ]:
pf_data.tail()
# In[ ]:
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
# In[ ]:
log_returns = np.log(pf_data / pf_data.shift(1))
# In[ ]:
log_returns.mean() * 250
# In[ ]:
log_returns.cov() * 250
# In[ ]:
log_returns.corr()
# In[ ]:
num_assets = len(assets)
# In[ ]:
num_assets
# In[ ]:
arr = np.random.random(2)
arr
# In[ ]:
arr[0] + arr[1]
# In[ ]:
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
# In[ ]:
weights[0] + weights[1]
