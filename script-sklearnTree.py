from tensorflow.python.keras import Sequential
from pandas_datareader import data
import pandas as pd
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
stock = 'TSLA'
yahooStockOption: YahooStockOption = YahooStockOption(stock)
total_size: int = len(yahooStockOption.DataFrame)
train_size: int = round(0.85 * total_size)
test_size: int = round(0.1 * total_size)
print(yahooStockOption.DataFrame.describe(include='all'))
print(total_size)
print(train_size)
print(test_size)
sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

scaler = MinMaxScaler(feature_range=(0, 1))
prediction_days: int = 60
future_days: int = 1
scaled_data: np.ndarray = scaler.fit_transform(yahooStockOption.DataFrame['Adj Close'].values.reshape(-1, 1))
x_train_list: list = []
y_train_list: list = []
print(type(x_train_list))
for x in range(prediction_days, total_size):
    x_train_list.append(scaled_data[x - prediction_days: x, 0])
    y_train_list.append(scaled_data[x, 0])
x_train, y_train = np.array(x_train_list), np.array(y_train_list)
print(type(x_train))
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
print(type(x_train))

model: Sequential = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=future_days))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=25, batch_size=32)
# data unknown to model
test_start = dt.datetime(2021, 1, 1)
test_end = dt.datetime.now()
test_data = data.DataReader(stock, 'yahoo', test_start, test_end)
actual_prices = test_data['Adj Close'].values
total_dataset = pd.concat((yahooStockOption.DataFrame['Adj Close'], test_data['Adj Close']), axis=0)
model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days : ].values
model_inputs = model_inputs.reshape(-1, 1)
model_inputs = scaler.transform(model_inputs)
# predict
x_test = []
for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x - prediction_days : x, 0])
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
predicted_prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)
# plot
plt.plot(actual_prices, color='blue', label='act_p')
plt.plot(predicted_prices, color='green', label='pred_p')
plt.title(stock + '_Share Price')
plt.xlabel('Time')
plt.ylabel(stock + '_label')
plt.legend()
plt.show()
# predict a day ahead
real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model_inputs+1), 0]]
real_data = np.array(real_data)
real_data = np.reshape(real_data, (real_data[0], real_data[1], 1))
prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)
print('prediction', prediction)
exit(1492)
#
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
# from sklearn.externals import joblib
import joblib

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
# print(df_0 == df_2)
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
svr_rbf: SVR = SVR(kernel='rbf', C=1e3, gamma=0.1)  # 0.85
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
'''
# PLOT
plt.figure(figsize=(8, 6))
plt.scatter(df_0.index, df_0)
plt.plot(df_0.index, lin_reg.predict(X_train), color='green', label='lin_reg')
plt.legend()
plt.show()
#model = joblib('model.joblib')
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
#joblib.dump(model, 'model.joblib')
#tree.export_graphviz(model, out_file='model.dot', feature_names=[col1, col2], class_names=sorted(y.unique), label='all', rounded=True, filled=True)
predictions = model.predict(X_test)
score: float = accuracy_score(y_test, predictions)
print(score)
'''
