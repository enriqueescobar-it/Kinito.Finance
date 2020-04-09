# one stock -> simple return is common but not for many
# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
'''from AssetTypes.BaseAsset import BaseAsset
from AssetTypes.EquityShare import EquityShare
from AssetTypes.GovernmentBond import GovernmentBond'''
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
# with iex key`
# PG = wb.DataReader('PG', data_source='iex', start='2015-1-1')
# csv
# PG = pd.read_csv('Section-11_PG_1995-03_23_2017.csv')
# PG = PG.set_index('Date')
# calculate simple return
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])
# plot simple return
PG['simple_return'].plot(figsize=(8, 5))
# plt.show()
# Calculate the simple average daily return.
avg_returns_d = PG['simple_return'].mean()
# Estimate the simple average annual return.
avg_returns_a = PG['simple_return'].mean() * 250
# Print the simple percentage version of the result as a float with 2 digits after the decimal point.
print (str(round(avg_returns_a, 5) * 100) + ' %')
# calculate log return
PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print (PG['log_return'])
# plot log return
PG['log_return'].plot(figsize=(8, 5))
# plt.show()
# Calculate the log average daily return.
avg_returns_d = PG['log_return'].mean()
# Estimate the log average annual return.
avg_returns_a = PG['log_return'].mean() * 250
# Print the log percentage version of the result as a float with 2 digits after the decimal point.
print (str(round(avg_returns_a, 5) * 100) + ' %')
#
import quandl
#
mydata_01 = quandl.get("FRED/GDP")
mydata_01.tail()
mydata_01.head()
mydata_01.to_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_01.csv')
mydata_01 = pd.read_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_01.csv', index_col='Date')
mydata_01.tail()
mydata_01 = pd.read_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_01.csv')
mydata_01.tail()
mydata_01.set_index('Date')
mydata_01.tail()
mydata_02 = pd.read_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_02.csv', index_col='Date')
mydata_02.head()
mydata_02.tail()
mydata_02.to_excel('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_02.xlsx')
mydata_02.info()
mydata_03 = pd.read_excel('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_03.xlsx')
mydata_03.info()
mydata_03.set_index('Year')
mydata_03.info()
########## Return of Indices
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
tickers = ['^DJI', '^GSPC', '^IXIC', '^GDAXI']
ind_data = pd.DataFrame()
for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Adj Close']
ind_data.head()
ind_data.tail()
# Normalize the data to 100 and plot the results on a graph. 
(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()
# How would you explain the common and the different parts of the behavior of the three indices?
# Obtain the simple returns of the indices.
ind_returns = (ind_data / ind_data.shift(1)) - 1
ind_returns.tail()
# Estimate the average annual return of each index.
annual_ind_returns = ind_returns.mean() * 250
annual_ind_returns
##########
'''baseAsset: BaseAsset = EquityShare('PG')
print(baseAsset.ShortType)
print(baseAsset.AssetType)
print(baseAsset.AssetName)
print(baseAsset.getSimpleReturn(PG))'''
tickers = ['PG', 'MSFT', 'F', 'GE']
yahoo_df = pd.DataFrame()
iex_df = pd.DataFrame()
for t in tickers:
    yahoo_df[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']
    # iex_df[t] = wb.DataReader(t, data_source='iex', start='2002-1-1')['Close']
yahoo_df = pd.read_csv('Section-12_PG_BEI.DE_2007_2017.csv', index_col='Date')
yahoo_df.tail()
yahoo_df.head()
# newDataFrame.to_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-example_01.csv')
# newDataFrame.to_excel('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-example_01.xlsx')'''
yahoo_df.iloc[0]
(yahoo_df / yahoo_df.iloc[0] * 100).plot(figsize = (15, 6));
yahoo_df.plot(figsize=(15,6))
yahoo_df.loc['2007-01-03']
yahoo_df.iloc[0]
## Calculating the Return of a Portfolio of Securities
simple_returns = (yahoo_df / yahoo_df.shift(1)) - 1
simple_returns.head()
weights = np.array([0.5, 0.5])
np.dot(simple_returns, weights)
simple_returns_anual = simple_returns.mean() * 250
simple_returns_anual
np.dot(simple_returns_anual, weights)
pfolio_1 = str(round(np.dot(simple_returns_anual, weights), 5) * 100) + ' %'
print (pfolio_1)
weights_2 = np.array([0.75, 0.25])
pfolio_2 = str(round(np.dot(simple_returns_anual, weights_2), 5) * 100) + ' %'
print (pfolio_2)
## Calculating the Risk of a Portfolio of Securities Section-11_MSFT_2000_2017.csv
log_returns = np.log(yahoo_df / yahoo_df.shift(1))
log_returns.head()
# MSFT
log_returns['PG'].mean()
# Annual risk: covariance
log_returns['PG'].mean()*250
# Daily risk:
log_returns['PG'].std()
# Annual risk: covariance
log_returns['PG'].std() * 250 ** 0.5
# PG
log_returns['BEI.DE'].mean()
# Annual risk: covariance
log_returns['BEI.DE'].mean()*250
# Daily risk:
log_returns['BEI.DE'].std()
# Annual risk: covariance
log_returns['BEI.DE'].std() * 250 ** 0.5
# Repeat the process we went through in the lecture for these two stocks. How would you explain the difference between their means and their standard deviations?
log_returns[['PG', 'BEI.DE']].mean() * 250
# Store the volatilities of the two stocks in an array called "vols".
volatilities = log_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5
volatilities
# ## Covariance and Correlation on returns
# \begin{eqnarray*}
# Covariance Matrix: \  \   
# \Sigma = \begin{bmatrix}
#         \sigma_{1}^2 \ \sigma_{12} \ \dots \ \sigma_{1I} \\
#         \sigma_{21} \ \sigma_{2}^2 \ \dots \ \sigma_{2I} \\
#         \vdots \ \vdots \ \ddots \ \vdots \\
#         \sigma_{I1} \ \sigma_{I2} \ \dots \ \sigma_{I}^2
#     \end{bmatrix}
# \end{eqnarray*}
# variance on returns
ms_var = log_returns['PG'].var() 
ms_var
ms_var_anual = log_returns['PG'].var() * 250
ms_var_anual
pg_var = log_returns['BEI.DE'].var() 
pg_var
pg_var_anual = log_returns['BEI.DE'].var() * 250
pg_var_anual
# covariance on returns
cov_matrix = log_returns.cov()
cov_matrix
cov_matrix_anual = log_returns.cov() * 250
cov_matrix_anual
# correlation on returns no need x 252
corr_matrix = log_returns.corr()
corr_matrix
# ## Calculating Portfolio Risk
# Weigthing scheme:
weights = np.array([0.25, 0.75])
# Portfolio Variance:
pfolio_var = np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
pfolio_var
# Portfolio Volatility:
pfolio_vol = (np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))) ** 0.5
pfolio_vol
print (str(round(pfolio_vol, 5) * 100) + ' %')
# systematic = un diversifiable risk
# unsystematic = diversifiable risk = idiosyncratic -> diversification
## Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio
# Diversifiable Risk:
ms_var_anual = log_returns['PG'].var() * 250
ms_var_anual
pg_var_anual = log_returns['BEI.DE'].var() * 250
pg_var_anual
diversifable_risk = pfolio_var - (weights[0] ** 2 * ms_var_anual) - (weights[1] ** 2 * pg_var_anual)
diversifable_risk
print (str(round(diversifable_risk*100, 3)) + ' %')
# Non-Diversifiable Risk:
n_dr_1 = pfolio_var - diversifable_risk
n_dr_1
n_dr_2 = (weights[0] ** 2 * ms_var_anual) + (weights[1] ** 2 * pg_var_anual)
n_dr_2
n_dr_1 == n_dr_2
# regresssions
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm 
import matplotlib.pyplot as plt
data = pd.read_excel('Section-13_Housing.xlsx')
data[['House Price', 'House Size (sq.ft.)']]
# univarate regression
X = data['House Size (sq.ft.)']
Y = data['House Price']
plt.scatter(X,Y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft)')
# regression linear OLS
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
### Alpha, Beta, R^2:
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
line = intercept + slope * X
plt.plot(X,line)
print(slope)
print(intercept)
print(r_value)
print(r_value**2)
print(p_value)
print(std_err)
data = pd.read_excel('Section-13_IQ_data.xlsx')
data[['IQ', 'Test 1']]
X = data['Test 1']
Y = data['IQ']
plt.scatter(X,Y)
plt.axis([0, 120, 0, 150])
plt.ylabel('IQ')
plt.xlabel('Test 1')
# regression linear OLS
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
### Alpha, Beta, R^2:
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
line = intercept + slope * X
plt.plot(X,line)
print(slope)
print(intercept)
print(r_value)
print(r_value**2)
print(p_value)
print(std_err)
####################
# ## Obtaining the Efficient Frontier - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# We are in the middle of a set of 3 Python lectures that will help you reproduce the Markowitz Efficient Frontier. Let’s split this exercise into 3 parts and cover the first part here. 
# Begin by loading data for Walmart and Facebook from the 1st of January 2014 until today.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
assets = ['PG', '^GSPC']
# assets = ['WMT', 'FB']
pf_data = pd.DataFrame()
# for a in assets:
#     pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2010-1-1')['Adj Close']
pf_data = pd.read_csv('Section-14_Markowitz_Data.csv', index_col = 'Date')
# pf_data = pd.read_csv('Section-12_Walmart_FB_2014_2017.csv', index_col='Date')
pf_data.tail()
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
log_returns = np.log(pf_data / pf_data.shift(1))
log_returns.mean() * 250
log_returns.cov() * 250
log_returns.corr()
# In[10]:
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
weights[0] + weights[1]
# Now, estimate the expected Portfolio Return, Variance, and Volatility.
# Expected Portfolio Return:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# Expected Portfolio Volatility:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# ***
# The rest of this exercise will be a reproduction of what we did in the previous video.
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.
pfolio_returns = []
pfolio_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns, pfolio_volatilities
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once you have done that, the two objects will be NumPy arrays. 
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
pfolio_returns, pfolio_volatilities
# In[21]:
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
portfolios.head()
portfolios.tail()
# In[24]:
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
######### Section-14_87-ObtainingtheEfficientFrontier-PartIII-Solution_CSV
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
assets = ['WMT', 'FB']
pf_data = pd.read_csv('Section-14_Walmart_FB_2014_2017.csv', index_col='Date')
# pf_data = pd.DataFrame()
# for a in assets:
#     pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']
pf_data.tail()
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
log_returns = np.log(pf_data / pf_data.shift(1))
log_returns.mean() * 250
log_returns.cov() * 250
log_returns.corr()
# In[10]:
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
weights[0] + weights[1]
# Now, estimate the expected Portfolio Return, Variance, and Volatility.
# Expected Portfolio Return:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# Expected Portfolio Volatility:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# The rest of this exercise will be a reproduction of what we did in the previous video.
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.
pf_returns = []
pf_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pf_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pf_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pf_returns, pf_volatilities
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once you have done that, the two objects will be NumPy arrays. 
# In[8]:
pf_returns = np.array(pf_returns)
pf_volatilities = np.array(pf_volatilities)
pf_returns, pf_volatilities
# Now, create a dictionary, called portfolios, whose keys are the strings “Return” and “Volatility” and whose values are the NumPy arrays pf_returns and pf_volatilities. 
# In[9]:
portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_volatilities})
# In[10]:
portfolios.head()
portfolios.tail()
# Finally, plot the data from the portfolios dictionary on a graph. Let the x-axis represent the volatility data from the portfolios dictionary and the y-axis – the data about rates of return. <br />
# Organize your chart well and make sure you have labeled both the x- and the y- axes.
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
# What do you think would happen if you re-created the Markowitz Efficient Frontier for 3 stocks? The code you have created is supposed to accommodate easily the addition of a third stock, say British Petroleum (‘BP’). Insert it in your data and re-run the code (you can expand the “Cell” list from the Jupyter menu and click on “Run All” to execute all the cells at once!). <br />
# How would you interpret the obtained graph? 
assets = ['WMT', 'FB', 'BP']
pf_data = pd.DataFrame()
for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']
pf_data.head()
# In[14]:
log_returns = np.log(pf_data / pf_data.shift(1))
# In[15]:
num_assets = len(assets)
num_assets
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
weights[0] + weights[1] + weights[2]
# Expected Portfolio Return:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# Expected Portfolio Volatility:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# *****
pfolio_returns = []
pfolio_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns, pfolio_volatilities
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once you have done that, the two objects will be NumPy arrays. 
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
pfolio_returns, pfolio_volatilities
# In[21]:
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
portfolios.head()
portfolios.tail()
# In[24]:
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
########## Section-14_87-ObtainingtheEfficientFrontier-PartIII-Solution-3companies_CSV
#!/usr/bin/env python
# coding: utf-8
# ## Obtaining the Efficient Frontier - Part III
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# We are in the middle of a set of 3 Python lectures that will help you reproduce the Markowitz Efficient Frontier. Lets split this exercise into 3 parts and cover the first part here. 
# Begin by loading data for Walmart and Facebook from the 1st of January 2014 until today.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# In[2]:
assets = ['WMT', 'FB', 'BP']
# pf_data = pd.DataFrame()
# for a in assets:
#     pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']
pf_data = pd.read_csv('Section-14_87-WMT_FB_BP_2014_2017.csv', index_col='Date')
# In[3]:
pf_data.head()
# In[4]:
pf_data.tail()
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
log_returns = np.log(pf_data / pf_data.shift(1))
log_returns.mean() * 250
log_returns.cov() * 250
log_returns.corr()
# In[10]:
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
# In[15]:
weights[0] + weights[1] + weights[2]
# Expected Portfolio Return:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# Expected Portfolio Volatility:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# The rest of this exercise will be a reproduction of what we did in the previous video.
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.
pfolio_returns = []
pfolio_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
pfolio_returns, pfolio_volatilities
# In[20]:
pfolio_returns = []
pfolio_volatilities = []
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
pfolio_returns, pfolio_volatilities
# In[21]:
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
portfolios.head()
portfolios.tail()
# In[24]:
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
## Calculating the Beta of a Stock
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Load the data for Microsoft and S&P 500 for the period 1st of January 2012 – 31st of December 2016. 
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# tickers = ['PG', '^GSPC']
# tickers = ['MSFT', '^GSPC']
# data = pd.DataFrame()
# for t in tickers:
#     data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']
#     data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']
data = pd.read_csv('Section-15_CAPM_Data.csv', index_col = 'Date')
data = pd.read_csv('Section-15_CAPM_Exercise_Data.csv', index_col = 'Date')
data.head()
# Let S&P 500 act as the market. 
# *****
# Calculate the beta of Microsoft.
sec_returns = np.log( data / data.shift(1) )
# In[3]:
cov = sec_returns.cov() * 250
cov
# In[4]:
cov_with_market = cov.iloc[0,1]
cov_with_market
# In[5]:
market_var = sec_returns['^GSPC'].var() * 250
market_var
# ** Beta**
# $$ 
# \beta_{stock} = \frac{\sigma_{stock,market}}{\sigma_{market}^2}
# $$
stock_beta = cov_with_market / market_var
stock_beta
## Calculating the Expected Return of a Stock (CAPM)
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Obtain data for Microsoft and S&P 500 for the period 1st of January 2012  31st of December 2016 from Yahoo Finance. 
# Let S&P 500 act as the market. 
# Calculate the beta of Microsoft.
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# tickers = ['PG', '^GSPC']
# tickers = ['MSFT', '^GSPC']
# data = pd.DataFrame()
# for t in tickers:
#     data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']
data = pd.read_csv('Section-15_CAPM_Data.csv', index_col = 'Date')
# data = pd.read_csv('Section-15_CAPM_Exercise_Data.csv', index_col = 'Date')
data.head()
sec_returns = np.log( data / data.shift(1) )
# In[3]:
cov = sec_returns.cov() * 250
cov
# In[4]:
cov_with_market = cov.iloc[0,1]
cov_with_market
# In[5]:
market_var = sec_returns['^GSPC'].var() * 250
market_var
# **Beta:**
### $$
# \beta_{pg} = \frac{\sigma_{pg,m}}{\sigma_{m}^2}
# $$
stock_beta = cov_with_market / market_var
stock_beta
# Assume a risk-free rate of 2.5% and a risk premium of 5%. <br />
# Estimate the expected return of Microsoft.
# **Calculate the expected return of P&G (CAPM):**
# ### $$
# \overline{r_{pg}} = r_f + \beta_{pg}(\overline{r_{m}} - r_f) 
# $$
stock_expectedReturn = 0.025 + stock_beta * 0.05
stock_expectedReturn
## Estimating the Sharpe Ratio in Python
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Obtain data for Microsoft and S&P 500 for the period 1st of January 2012 – 31st of December 2016 from Yahoo Finance. 
# Let S&P 500 act as the market. 
# Calculate the beta of Microsoft.
# Assume a risk-free rate of 2.5% and a risk premium of 5%.<br />
# Estimate the expected return of Microsoft.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# tickers = ['PG', '^GSPC']
# tickers = ['MSFT', '^GSPC']
# data = pd.DataFrame()
# for t in tickers:
#     data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']
# data = pd.read_csv('Section-15_CAPM_Exercise_Data.csv', index_col = 'Date')
data = pd.read_csv('Section-15_CAPM_Data.csv', index_col = 'Date')  
data.head()
sec_returns = np.log( data / data.shift(1) )
# In[3]:
cov = sec_returns.cov() * 250
cov
# In[4]:
cov_with_market = cov.iloc[0,1]
cov_with_market
# In[5]:
market_var = sec_returns['^GSPC'].var() * 250
market_var
# ** Beta: **
# $$ 
# \beta_{pg} = \frac{\sigma_{pg,m}}{\sigma_{m}^2}
# $$
stock_beta = cov_with_market / market_var
stock_beta
# **Calculate the expected return of P&G (CAPM):**
# $$
# \overline{r_{pg}} = r_f + \beta_{pg}(\overline{r_{m}} - r_f) 
# $$
stock_er = 0.025 + stock_beta * 0.05
stock_er
# Calculate the Sharpe ratio in Python.
# **Sharpe ratio:**
# $$
# Sharpe = \frac{\overline{r_{pg}} - r_f}{\sigma_{pg}}
# $$
SharpeRatio = (stock_er - 0.025) / (sec_returns['PG'].std() * 250 ** 0.5)
#SharpeRatio = (stock_er - 0.025) / (sec_returns['MSFT'].std() * 250 ** 0.5)
SharpeRatio
## Monte Carlo - Predicting Gross Profit - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Imagine you are an experienced manager and you have forecasted revenues of \$200mln, with an expected deviation of $10mln. You are convinced Cogs will be near 40% of the revenues, and their expected deviation is 20% of its own value. 
# Use NumPys random.random function to simulate the potential revenue stream for 250 iterations (which is the number of trading days in a year) and then the predicted Cogs value. 
import numpy as np
import matplotlib.pyplot as plt
# In[2]:
rev_m = 170 # 200
rev_stdev = 20 # 10
iterations = 1000 # 250
# In[3]:
rev = np.random.normal(rev_m, rev_stdev, iterations)
rev
# Plot the obtained data for revenues and Cogs on a graph and observe the behavior of the obtained values.
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()
# In[5]:
COGS = - (rev * np.random.normal(0.6,0.1)) # (0.4,0.2))
plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()
# Cogs mean:
COGS.mean()
# Cogs std:
COGS.std()
# ****
# Based on the predicted revenue and Cogs values, estimate the expected Gross Profit of your company. 
# *Reminder: Be careful about estimating the gross profit. If you have stored the Cogs value as a negative number, the gross profit will equal revenues plus Cogs. If you have created Cogs as a positive value, then gross profit would be equal to revenues minus Cogs. Either way, you will obtain the same result for gross profit.* 
Gross_Profit = rev + COGS
Gross_Profit
plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()
# What is the maximum and what is the minimum gross profit value you obtained?
max(Gross_Profit)
# In[10]:
min(Gross_Profit)
# What is its mean and standard deviation?
Gross_Profit.mean()
# In[12]:
Gross_Profit.std()
# Do you remember what a histogram is? Plot the gross profit data on a histogram. Use 20 bins directly to check the distribution of the data.
plt.figure(figsize=(10, 6));
plt.hist(Gross_Profit, bins = [40, 50, 60, 70, 80, 90, 100, 110, 120]);
plt.show()
# In[14]:
plt.figure(figsize=(10, 6));
plt.hist(Gross_Profit, bins = 20);
plt.show()
# ************
# In all our analyses, we used estimations for either simple or logarithmic rates of return. <br/>
# The formula for simple returns is
# $$
# \frac{P_t - P_{t-1}}{P_{t-1}}
# $$
# while the formula for log returns is
# $$
# ln( \frac{P_t}{P_{t-1}} )
# $$
# If our dataset is simply called "data", in Python, we could write the first formula as
# *(data / data.shift(1)) - 1,*
# and the second one as
# *np.log(data / data.shift(1)).*
# Instead of coding it this way, some professionals prefer using **Pandas.DataFrame.pct_change()** method, as it computes simple returns directly. We will briefly introduce it to you in this notebook document.
# First, let's import NumPy, Pandas, and pandas_datareader.
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
# We will calculate returns of the Procter and Gamble stock, based on adjusted closing price data since the
# 1st of January 2007.
# 1st of January 2015.
data = pd.read_csv('Section-17_PG_2007_2017.csv', index_col = 'Date')
# ticker = 'PG' 
# data = pd.DataFrame()
# data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']
# data[ticker] = wb.DataReader(ticker, data_source='iex', start='2015-1-1')['close']
# So far, we estimated simple returns in the following way.
s_rets_1 = (data / data.shift(1)) - 1
s_rets_1.head()
# Observe the .pct_change() method can obtain an identical result.
s_rets_2 = data.pct_change()
s_rets_2.head()
# Now, if you multiply the obtained values by 100, you will see the percentage change:
s_rets_2.head() * 100
# This means the close price on 2007-01-04 was 0.76% lower than the price on 2007-01-03, the price on 2007-01-05 was 0.85% lower than the price on 2007-01-04, and so on.
# A few arguments can be used in the percentage change method. The most important one is 'period' as it specifies the difference between prices in the nominator. By default, it equals one, and that's why we obtained the same result for s_rets_1 and s_rets_2. Let's assume we would like to calculate simple returns with the following formula: 
# $$
# \frac{P_t - P_{t-2}}{P_{t-2}}
# $$
# Then, we should specify 'periods = 2' in parentheses:
s_rets_3 = data.pct_change(periods=2)
s_rets_3.head()
# You can see there was no value obtained not only for the first, but also for the second observation. If we use the "old" formula, and not this method, *shift(2)* would lead us to the same output:
s_rets_4 = (data / data.shift(2)) - 1
s_rets_4.head()
# Now, let's consider logarithmic returns. To this moment, we applied the following formula:
log_rets_1 = np.log(data / data.shift(1))
log_rets_1.tail()
# You can calculate the same formula for log returns with the help of the .pct_change() method. Just be careful with the way you apply the formula! Mathematically, it will look like this:
# $$
# ln(\frac{P_t}{P_{t-1}} ) = ln( \frac{P_t - P_{t-1}}{P_{t-1}} + \frac{P_{t-1}}{P_{t-1}}) = ln(\ simple.returns + 1)
# $$
# In[9]:
log_rets_2 = np.log(data.pct_change() + 1)
log_rets_2.tail()
# ***
# The .pct_change() method is very popular. Whether you include it in your code or you go the other way around and type the formulas as we did in our analyses, you should obtain the correct value for the returns you need.
########## 103
## Monte Carlo - Forecasting Stock Prices - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Download the data for Microsoft (MSFT) from Yahoo Finance for the period 2000-1-1 until today.
# Download the data for Microsoft (MSFT) from IEX for the period 2015-1-1 until today.
# Forecasting Future Stock Prices  continued:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
# In[2]:
# ticker = 'PG'
# ticker = 'MSFT'
# data = pd.DataFrame()
# data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']
# data[ticker] = wb.DataReader(ticker, data_source='iex', start='2015-1-1')['close']
data = pd.read_csv('Section-17_PG_2007_2017.csv', index_col = 'Date')
data = pd.read_csv('Section-17_MSFT_2000.csv', index_col = 'Date')
data.plot(figsize=(10, 6));
# Use the .pct_change() method to obtain the log returns of Microsoft for the designated period.
log_returns = np.log(1 + data.pct_change())
log_returns.tail()
log_returns.plot(figsize = (10, 6))
# Assign the mean value of the log returns to a variable, called U, and their variance to a variable, called var. 
u = log_returns.mean()
u
# In[7]:
var = log_returns.var()
var
# Calculate the drift, using the following formula: 
# $$
# drift = u - \frac{1}{2} \cdot var
# $$
drift = u - (0.5 * var)
drift
# Store the standard deviation of the log returns in a variable, called stdev.
stdev = log_returns.std()
stdev
# ******
# Use .values to transform the *drift* and the *stdev* objects into arrays. 
type(drift)
drift.values
# In[4]:
type(stdev)
# In[12]:
np.array(drift)
drift.values
# In[14]:
stdev.values
# Forecast future stock prices for every trading day a year ahead. So, assign 250 to t_intervals.
# Lets examine 10 possible outcomes. Bind iterations to the value of 10.
t_intervals = 250
t_intervals = 1000
iterations = 10
# Use the formula we have provided and calculate daily returns.
# $$
# r = drift + stdev \cdot z
# $$
# $$
# daily\_returns = exp({drift} + {stdev} * z), 
# $$
# $$
# where\  z = norm.ppf(np.random.rand(t\_intervals, iterations)
# $$
# $$
# daily\_returns = e^{r}
# $$
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
daily_returns
# $$
# S_t = S_0 \mathbin{\cdot} daily\_return_t
# $$
# $$
# S_{t+1} = S_t \mathbin{\cdot} daily\_return_{t+1}
# $$
# $$...$$
# $$
# S_{t+999} = S_{t+998} \mathbin{\cdot} daily\_return_{t+999}
# $$
# ***
# Create a variable S0 equal to the last adjusted closing price of Microsoft. Use the iloc method.
S0 = data.iloc[-1]
S0
# Create a variable price_list with the same dimension as the daily_returns matrix. 
price_list = np.zeros_like(daily_returns)
price_list
price_list[0]
# Set the values on the first row of the price_list array equal to S0.
price_list[0] = S0
price_list
# Create a loop in the range (1, t_intervals) that reassigns to the price in time t the product of the price in day (t-1) with the value of the daily returns in t.
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]
price_list
# Finally, plot the obtained price list data.
plt.figure(figsize=(10,6))
plt.plot(price_list);

