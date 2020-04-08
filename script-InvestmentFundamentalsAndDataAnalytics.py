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
