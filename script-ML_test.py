from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('ESTC')
print(yahooStockOption.DataFrame.describe(include='all'))

sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)

yahooStockOptionPlotter: HistoricalPlotter = HistoricalPlotter(yahooStockOption, vixIndex, sAnP500)

from pandas import Series

df_serie: Series = yahooStockOption.DataFrame.reset_index()[yahooStockOption.Column]
print(type(df_serie))
### LSTM are sensitive to the scale of the data. so we apply MinMax scaler
import numpy as np
from numpy import ndarray
from sklearn.preprocessing import MinMaxScaler

minMaxScaler = MinMaxScaler(feature_range=(0, 1))
df_array: ndarray = minMaxScaler.fit_transform(np.array(df_serie).reshape(-1, 1))
print(type(df_array))
exit(111)
##splitting dataset into train and test split
training_size = int(len(df_array) * 0.80)
testing_size = len(df_array) - training_size
train_data = df_array[0:training_size, :]
test_data = df_array[training_size:len(df_array), :1]
print(train_data)
import numpy


# convert an array of values into a dataset matrix
def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - time_step - 1):
        a = dataset[i:(i + time_step), 0]  ###i=0, 0,1,2,3-----99   100
        dataX.append(a)
        dataY.append(dataset[i + time_step, 0])
    return numpy.array(dataX), numpy.array(dataY)


# reshape into X=t,t+1,t+2,t+3 and Y=t+4
time_step = 100
X_train, y_train = create_dataset(train_data, time_step)
X_test, ytest = create_dataset(test_data, time_step)
print('X_train', X_train.shape)
print('y_train', y_train.shape)
print('y_train', y_train.size)
print('X_test', X_test.shape)
print('ytest', ytest.shape)

# reshape input to be [samples, time steps, features] which is required for LSTM
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
### Create the Stacked LSTM model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(100, 1)))
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()
model.summary()
model.fit(X_train, y_train, validation_data=(X_test, ytest), epochs=100, batch_size=64, verbose=1)
import tensorflow as tf

print(tf.__version__)
### Lets Do the prediction and check performance metrics
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)
##Transformback to original form
train_predict = minMaxScaler.inverse_transform(train_predict)
test_predict = minMaxScaler.inverse_transform(test_predict)

### Calculate RMSE performance metrics
import math
import matplotlib as plt
from sklearn.metrics import mean_squared_error

math.sqrt(mean_squared_error(y_train, train_predict))

### Test Data RMSE
math.sqrt(mean_squared_error(ytest, test_predict))
### Plotting
# shift train predictions for plotting
look_back = 100
trainPredictPlot = numpy.empty_like(df_array)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict) + look_back, :] = train_predict
# shift test predictions for plotting
testPredictPlot = numpy.empty_like(df_array)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(train_predict) + (look_back * 2) + 1:len(df_array) - 1, :] = test_predict
# plot baseline and predictions
# plt.plot(minMaxScaler.inverse_transform(df1))
#plt.plot(trainPredictPlot)
#plt.plot(testPredictPlot)
plt.show()
print(len(test_data))
x_input = test_data[341:].reshape(1, -1)
temp_input = list(x_input)
temp_input = temp_input[0].tolist()
# demonstrate prediction for next 10 days
from numpy import array

lst_output = []
n_steps = 100
i = 0
while i < 30:
    if len(temp_input) > 100:
        # print(temp_input)
        x_input = np.array(temp_input[1:])
        print("{} day input {}".format(i, x_input))
        x_input = x_input.reshape(1, -1)
        x_input = x_input.reshape((1, n_steps, 1))
        # print(x_input)
        yhat = model.predict(x_input, verbose=0)
        print("{} day output {}".format(i, yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input = temp_input[1:]
        # print(temp_input)
        lst_output.extend(yhat.tolist())
        i = i + 1
    else:
        x_input = x_input.reshape((1, n_steps, 1))
        yhat = model.predict(x_input, verbose=0)
        print(yhat[0])
        temp_input.extend(yhat[0].tolist())
        print(len(temp_input))
        lst_output.extend(yhat.tolist())
        i = i + 1
print(lst_output)
day_new = np.arange(1, 101)
day_pred = np.arange(101, 131)
import matplotlib.pyplot as plt

plt.plot(day_new, minMaxScaler.inverse_transform(df_array[1158:]))
plt.plot(day_pred, minMaxScaler.inverse_transform(lst_output))
df3 = df_array.tolist()
df3.extend(lst_output)
plt.plot(df3[1200:])
df3 = minMaxScaler.inverse_transform(df3).tolist()
plt.plot(df3)
