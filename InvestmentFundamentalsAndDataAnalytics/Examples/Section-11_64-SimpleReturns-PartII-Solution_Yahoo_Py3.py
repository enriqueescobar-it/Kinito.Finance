#!/usr/bin/env python
# coding: utf-8
# ## Simple Returns - Part II
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$
# In[ ]:
import numpy as np
from pandas_datareader import data as wb
MSFT = wb.DataReader('MSFT', data_source='yahoo', start='2000-1-1')
MSFT['simple_return'] = (MSFT['Adj Close'] / MSFT['Adj Close'].shift(1)) - 1
print (MSFT['simple_return'])
# Plot the simple returns on a graph.
# In[ ]:
import matplotlib.pyplot as plt
# In[ ]:
MSFT['simple_return'].plot(figsize=(8, 5))
plt.show()
# Calculate the average daily return.
# In[ ]:
avg_returns_d = MSFT['simple_return'].mean()
avg_returns_d
# Estimate the average annual return.
# In[ ]:
avg_returns_a = MSFT['simple_return'].mean() * 250
avg_returns_a
# Print the percentage version of the result as a float with 2 digits after the decimal point.
# In[ ]:
print (str(round(avg_returns_a, 4) * 100) + ' %')
