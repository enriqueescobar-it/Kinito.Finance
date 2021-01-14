#!/usr/bin/env python
# coding: utf-8
# # Visualizing Time Series Data
# Let's go through a few key points of creatng nice time visualizations!
import pandas as pd
import matplotlib.pyplot as plt

# get_ipython().run_line_magic('matplotlib', 'inline')
# Optional for interactive
# %matplotlib notebook (watch video for full details)
mcdon = pd.read_csv('Data/04-Visualization-Matplotlib-Pandas_mcdonalds.csv', index_col='Date', parse_dates=True)
mcdon.head()
mcdon.plot()
mcdon['Adj. Close'].plot()
mcdon['Adj. Volume'].plot()
mcdon['Adj. Close'].plot(figsize=(12, 8))
plt.ylabel('Close Price')
plt.xlabel('Overwrite Date Index')
plt.title('Mcdonalds')
mcdon['Adj. Close'].plot(figsize=(12, 8), title='Pandas Title')
# # Plot Formatting
# ## X Limits
mcdon['Adj. Close'].plot(xlim=['2007-01-01', '2009-01-01'])
mcdon['Adj. Close'].plot(xlim=['2007-01-01', '2009-01-01'], ylim=[0, 50])
# ## Color and Style
mcdon['Adj. Close'].plot(xlim=['2007-01-01', '2007-05-01'], ylim=[0, 40], ls='--', c='r')
# ## X Ticks
# This is where you will need the power of matplotlib to do heavy lifting if you want some serious customization!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

# In[14]:
mcdon['Adj. Close'].plot(xlim=['2007-01-01', '2007-05-01'], ylim=[0, 40])
idx = mcdon.loc['2007-01-01':'2007-05-01'].index
idx
stock = mcdon.loc['2007-01-01':'2007-05-01']['Adj. Close']
stock
#  ## Basic matplotlib plot
fig, ax = plt.subplots()
ax.plot_date(idx, stock, '-')
plt.tight_layout()
# ## Fix the overlap!
fig, ax = plt.subplots()
ax.plot_date(idx, stock, '-')
fig.autofmt_xdate()  # Auto fixes the overlap!
plt.tight_layout()
plt.show()
# ## Customize grid
fig, ax = plt.subplots()
ax.plot_date(idx, stock, '-')
ax.yaxis.grid(True)
ax.xaxis.grid(True)
fig.autofmt_xdate()  # Auto fixes the overlap!
plt.tight_layout()
# ## Format dates on Major Axis
# In[21]:
fig, ax = plt.subplots()
ax.plot_date(idx, stock, '-')
# Grids
ax.yaxis.grid(True)
ax.xaxis.grid(True)
# Major Axis
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b\n%Y'))
fig.autofmt_xdate()  # Auto fixes the overlap!
plt.tight_layout()
plt.show()
# In[22]:
fig, ax = plt.subplots()
ax.plot_date(idx, stock, '-')
# Grids
ax.yaxis.grid(True)
ax.xaxis.grid(True)
# Major Axis
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('\n\n\n\n%Y--%B'))
fig.autofmt_xdate()  # Auto fixes the overlap!
plt.tight_layout()
plt.show()
# ## Minor Axis
# In[23]:
fig, ax = plt.subplots()
ax.plot_date(idx, stock, '-')
# Major Axis
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('\n\n%Y--%B'))
# Minor Axis
ax.xaxis.set_minor_locator(dates.WeekdayLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
# Grids
ax.yaxis.grid(True)
ax.xaxis.grid(True)
fig.autofmt_xdate()  # Auto fixes the overlap!
plt.tight_layout()
plt.show()
# In[33]:
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot_date(idx, stock, '-')
# Major Axis
ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=1))
ax.xaxis.set_major_formatter(dates.DateFormatter('%B-%d-%a'))
# Grids
ax.yaxis.grid(True)
ax.xaxis.grid(True)
fig.autofmt_xdate()  # Auto fixes the overlap!
plt.tight_layout()
plt.show()
# ## Great job!
