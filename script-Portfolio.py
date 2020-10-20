import seaborn as sns
import matplotlib.pyplot as plt
from math import ceil
import numpy as np
from Common.Comparators.Portfolio.PortfolioComparator import PortfolioComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
#from typing import List
yahooTickers: list = ['CNI', 'CP', 'TD', 'OTEX', 'AQN']
    #['T', 'IBM', 'ABBV', 'GM', 'IRM', 'MPW', 'AGNC', 'PSEC', 'MAIN']
    #['VGT', 'VPU', 'VDC', 'VYM'], 'F', 'VYMI'
    #['CNI', 'CP', 'TD', 'OTEX', 'AQN', 'WCN']
yahooStocks: list = list()
for yahooTicker in yahooTickers:
    yahooStocks.append(YahooStockOption(yahooTicker))
    print(yahooTicker)

yahooPc: PortfolioComparator = PortfolioComparator(yahooStocks)
yahooPc.PlotBasics().show()
yahooPc.PlotAllSimple().show()
yahooPc.PlotAllHeatmaps().show()
exit(333)
# Explo Data Analysis
# on returns sns.pairplot(returns w/o NaN => returns[1:])
# return[col].min() -> value .argmin() -> index == .idxmin()
# return.std() higher riskier
# returns.ix[str_date_min:str_date_max].std()
# sns.distplot(returns.ix[str_date_min:str_date_max][StockName], color='g', bins=50)
# sns.heatmap on corr
# sns.clustermap on corr
# df.iplot(kind='candle')
# df[colname].ix[deltatime].ta_plot(study='sma',periods[12,21,55]) 'boll' => sma14, lower14, upper14
# EVal Perfo CALSSIFICATION ERROR METRICS
# ...
# Eval Perfo REGRESSION ERROR METRICS
# Mean Absolute Error MAE
# Mean Squared Error MSE
# Root Mean Squared Error RMSE
sns.pairplot(yahooPc.Data)
plt.show()
print('data', yahooPc.Data.shape)
len80: int = ceil(round(len(yahooPc.Data) * 0.8, 0))
print(len80)
X = yahooPc.Data.iloc[:, 0][0:len80]
y = yahooPc.Data.iloc[:, 0][len80:]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
#test model if residuals are normal
sns.distplot(y_test-predictions)
from sklearn import metrics
MAE = metrics.mean_absolute_error(y_test, predictions)
MSE = metrics.mean_squared_error(y_test, predictions)
RMSE = np.sqrt(metrics.mean_squared_error(y_test, predictions))
