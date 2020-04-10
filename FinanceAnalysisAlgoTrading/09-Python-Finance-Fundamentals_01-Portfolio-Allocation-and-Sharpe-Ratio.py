#!/usr/bin/env python
# coding: utf-8
# # Sharpe Ratio and Portfolio Values
import pandas as pd
import quandl
import matplotlib.pyplot as plt
import numpy as np
# ## Create a Portfolio
# In[3]:
start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01')
# Grabbing a bunch of tech stocks for our portfolio
aapl = quandl.get('WIKI/AAPL.11',start_date=start,end_date=end)
cisco = quandl.get('WIKI/CSCO.11',start_date=start,end_date=end)
ibm = quandl.get('WIKI/IBM.11',start_date=start,end_date=end)
amzn = quandl.get('WIKI/AMZN.11',start_date=start,end_date=end)
# Alternative
# aapl = pd.read_csv('AAPL_CLOSE',index_col='Date',parse_dates=True)
# cisco = pd.read_csv('CISCO_CLOSE',index_col='Date',parse_dates=True)
# ibm = pd.read_csv('IBM_CLOSE',index_col='Date',parse_dates=True)
# amzn = pd.read_csv('AMZN_CLOSE',index_col='Date',parse_dates=True)
aapl.to_csv('09-Python-Finance-Fundamentals_01-AAPL_CLOSE.csv')
cisco.to_csv('09-Python-Finance-Fundamentals_01-CISCO_CLOSE.csv')
ibm.to_csv('09-Python-Finance-Fundamentals_01-IBM_CLOSE.csv')
amzn.to_csv('09-Python-Finance-Fundamentals_01-AMZN_CLOSE.csv')
# ## Normalize Prices
# This is the same as cumulative daily returns
aapl.iloc[0]['Adj. Close']
# In[8]:
for stock_df in (aapl,cisco,ibm,amzn):
    stock_df['Normed Return'] = stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']
aapl.head()
# In[10]:
aapl.tail()
# ## Allocations
# Let's pretend we had the following allocations for our total portfolio:
# * 30% in Apple
# * 20% in Google/Alphabet
# * 40% in Amazon
# * 10% in IBM
# Let's have these values be reflected by multiplying our Norme Return by out Allocations
for stock_df,allo in zip([aapl,cisco,ibm,amzn],[.3,.2,.4,.1]):
    stock_df['Allocation'] = stock_df['Normed Return']*allo
aapl.head()
# ## Investment
# Let's pretend we invested a million dollars in this portfolio
for stock_df in [aapl,cisco,ibm,amzn]:
    stock_df['Position Values'] = stock_df['Allocation']*1000000
# ## Total Portfolio Value
portfolio_val = pd.concat([aapl['Position Values'],cisco['Position Values'],ibm['Position Values'],amzn['Position Values']],axis=1)
portfolio_val.head()
# In[16]:
portfolio_val.columns = ['AAPL Pos','CISCO Pos','IBM Pos','AMZN Pos']
portfolio_val.head()
# In[18]:
portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)
portfolio_val.head()
# In[20]:
portfolio_val['Total Pos'].plot(figsize=(10,8))
plt.title('Total Portfolio Value')
# In[22]:
portfolio_val.drop('Total Pos',axis=1).plot(kind='line')
portfolio_val.tail()
# # Portfolio Statistics
# ### Daily Returns
portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)
# ### Cumulative Return
cum_ret = 100 * (portfolio_val['Total Pos'][-1]/portfolio_val['Total Pos'][0] -1 )
print('Our return {} was percent!'.format(cum_ret))
# ### Avg Daily Return
portfolio_val['Daily Return'].mean()
# ### Std Daily Return
portfolio_val['Daily Return'].std()
portfolio_val['Daily Return'].plot(kind='kde')
# # Sharpe Ratio
# The Sharpe Ratio is a measure for calculating risk-adjusted return, and this ratio has become the industry standard for such calculations.
# Sharpe ratio = (Mean portfolio return − Risk-free rate)/Standard deviation of portfolio return
# The original Sharpe Ratio
# Annualized Sharpe Ratio = K-value * SR
# K-values for various sampling rates:
# * Daily = sqrt(252)
# * Weekly = sqrt(52)
# * Monthly = sqrt(12)
# Since I'm based in the USA, I will use a very low risk-free rate (the rate you would get if you just put your money in a bank, its currently very low in the USA,
# let's just say its ~0% return). If you are in a different country with higher rates for your trading currency, you can use this trick to convert a yearly rate with a daily rate:
# daily_rate = ((1.0 + yearly_rate)**(1/252))-1
# Other values people use are things like the 3-month treasury bill or [LIBOR](http://www.investopedia.com/terms/l/libor.asp).
# Read more: Sharpe Ratio http://www.investopedia.com/terms/s/sharperatio
SR = portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std()
SR
# In[31]:
ASR = (252**0.5)*SR
ASR
# In[33]:
portfolio_val['Daily Return'].std()
portfolio_val['Daily Return'].mean()
portfolio_val['Daily Return'].plot('kde')
# In[36]:
aapl['Adj. Close'].pct_change(1).plot('kde')
ibm['Adj. Close'].pct_change(1).plot('kde')
amzn['Adj. Close'].pct_change(1).plot('kde')
cisco['Adj. Close'].pct_change(1).plot('kde')
np.sqrt(252)* (np.mean(.001-0.0002)/.001)
# # Great Job!
