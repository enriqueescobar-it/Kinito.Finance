from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('ESTC')
print(yahooStockOption.DataFrame.describe(include='all'))

sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)

from pandas import DataFrame
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
#from sklearn.externals import joblib
import joblib
import matplotlib.pyplot as plt
# 20% of data for testing
print(type(yahooStockOption.DataFrame.loc[:, 'Adj Close']))
print(type(yahooStockOption.DataFrame[['Adj Close']]))
print(yahooStockOption.DataFrame[['Adj Close']].head())
df_0: DataFrame = yahooStockOption.DataFrame[['Adj Close']].copy()
forecast_count: int = 30
# dependant variable
df_1 = df_0.copy()
df_1['Prediction'] = df_1[['Adj Close']].shift(-forecast_count)
print(df_1.tail())
# independant variable
## df to numpy array
df_2: DataFrame = df_1.drop(['Prediction'], 1)
print(df_0.head())
print(df_2.head())
#print(df_0 == df_2)
## independent data set X
X = np.array(df_2)
X = X[:-forecast_count]
## dependent data set y
y = np.array(df_1['Prediction'])
y = y[:-forecast_count]
# 80% training 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_forecast = np.array(df_1.drop(['Prediction'], 1))[-forecast_count:]
# LIN
svr_lin: SVR = SVR(kernel='linear', C=1e3)
svr_lin.fit(X_train, y_train)
confidence_lin = svr_lin.score(X_test, y_test)
print('svr_lin', confidence_lin)
prediction_lin = svr_lin.predict(X_forecast)
print(prediction_lin)
# POLY
svr_poly: SVR = SVR(kernel='poly', C=1e3, degree=2)
svr_poly.fit(X_train, y_train)
confidence_poly = svr_poly.score(X_test, y_test)
print('svr_poly', confidence_poly)
prediction_poly = svr_poly.predict(X_forecast)
print(prediction_poly)
# RBF
svr_rbf: SVR = SVR(kernel='rbf', C=1e3, gamma=0.1)#0.85
svr_rbf.fit(X_train, y_train)
confidence_rbf = svr_rbf.score(X_test, y_test)
print('svr_rbf', confidence_rbf)
prediction_rbf = svr_rbf.predict(X_forecast)
print(prediction_rbf)
# LIN REG
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
confidence_lreg = lin_reg.score(X_test, y_test)
print('lin_reg', confidence_lreg)
prediction_lreg = lin_reg.predict(X_forecast)
print(prediction_lreg)
# PLOT
plt.figure(figsize=(8, 6))
plt.scatter(df_0.index, df_0)
plt.plot(df_0.index, lin_reg.predict(X_train), color='green', label='lin_reg')
plt.legend()
plt.show()
exit(1980)
#model = joblib('model.joblib')
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
#joblib.dump(model, 'model.joblib')
#tree.export_graphviz(model, out_file='model.dot', feature_names=[col1, col2], class_names=sorted(y.unique), label='all', rounded=True, filled=True)
predictions = model.predict(X_test)
score: float = accuracy_score(y_test, predictions)
print(score)
