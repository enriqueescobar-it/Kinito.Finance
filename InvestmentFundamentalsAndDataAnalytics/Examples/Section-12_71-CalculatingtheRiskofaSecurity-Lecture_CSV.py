#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[ ]:
sec_data = pd.read_csv('D:/Python/PG_BEI.DE_2007_2017.csv', index_col='Date')
# In[ ]:
sec_data.tail()
# In[ ]:
sec_returns = np.log(sec_data / sec_data.shift(1))
# In[ ]:
sec_returns
# ## PG
# In[ ]:
sec_returns['PG'].mean()
# In[ ]:
sec_returns['PG'].mean() * 250
# In[ ]:
sec_returns['PG'].std()
# In[ ]:
sec_returns['PG'].std() * 250 ** 0.5
# ## Beiersdorf
# In[ ]:
sec_returns['BEI.DE'].mean()
# In[ ]:
sec_returns['BEI.DE'].mean() * 250
# In[ ]:
sec_returns['BEI.DE'].std()
# In[ ]:
sec_returns['BEI.DE'].std() * 250 ** 0.5
# Final Results:
# In[ ]:
print sec_returns['PG'].mean() * 250
print sec_returns['BEI.DE'].mean() * 250
# In[ ]:
sec_returns['PG', 'BEI.DE'].mean() * 250
# In[ ]:
sec_returns[['PG', 'BEI.DE']].mean() * 250
# In[ ]:
sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5
