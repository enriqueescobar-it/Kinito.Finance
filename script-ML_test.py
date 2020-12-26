from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('AAPL')
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

##splitting dataset into train and test split
training_size = int(len(df_array) * 0.80)
testing_size = len(df_array) - training_size
training_df_array = df_array[0:training_size, :]
testing_df_array = df_array[training_size:len(df_array), :1]
print(len(training_df_array))
print(training_size)
print(len(testing_df_array))
print(testing_size)


# convert an array of values into a data set matrix
def create_data_set(data_set: np.array, time_step_count: int = 1) -> ndarray:
    dataX = []
    dataY = []
    for i in range(len(data_set) - time_step_count - 1):
        a = data_set[i:(i + time_step_count), 0]  ###i=0, 0,1,2,3-----99   100
        dataX.append(a)
        dataY.append(data_set[i + time_step_count, 0])
    return np.array(dataX), np.array(dataY)


# reshape into X=t,t+1,t+2,t+3 and Y=t+4
time_step = 100
x_training_df_array, y_training_df_array = create_data_set(training_df_array, time_step)
x_testing_df_array, y_testing_df_array = create_data_set(testing_df_array, time_step)
print('x_training_df_array', x_training_df_array.shape)
print('y_training_df_array', y_training_df_array.shape)
print('y_training_df_array', y_training_df_array.size)
print('x_testing_df_array', x_testing_df_array.shape)
print('y_testing_df_array', y_testing_df_array.shape)
print('y_testing_df_array', y_testing_df_array.size)

# reshape input to be [samples, time steps, features] which is required for LSTM
x_training_df_array = x_training_df_array.reshape(x_training_df_array.shape[0], x_training_df_array.shape[1], 1)
x_testing_df_array = x_testing_df_array.reshape(x_testing_df_array.shape[0], x_testing_df_array.shape[1], 1)
### Create the Stacked LSTM model
import tensorflow as tf
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
model.fit(x_training_df_array, y_training_df_array, validation_data=(x_testing_df_array, y_testing_df_array), epochs=100, batch_size=64, verbose=1)
print(tf.__version__)
### Lets Do the prediction and check performance metrics
training_predict_array: ndarray = model.predict(x_training_df_array)
testing_predict_array: ndarray = model.predict(x_testing_df_array)
##Transformback to original form
training_predict_array = minMaxScaler.inverse_transform(training_predict_array)
testing_predict_array = minMaxScaler.inverse_transform(testing_predict_array)
### Calculate RMSE performance metrics
import math
#import matplotlib as plt
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error

print(math.sqrt(mean_squared_error(y_training_df_array, training_predict_array)))

### Test Data RMSE
math.sqrt(mean_squared_error(y_testing_df_array, testing_predict_array))
### Plotting
# shift train predictions for plotting
look_back = 100
trainPredictPlot: ndarray = np.empty_like(df_array)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(training_predict_array) + look_back, :] = training_predict_array
# shift test predictions for plotting
testPredictPlot: ndarray = np.empty_like(df_array)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(training_predict_array) + (look_back * 2) + 1:len(df_array) - 1, :] = testing_predict_array
print(trainPredictPlot.shape)
# plot baseline and predictions
df_array_plot = minMaxScaler.inverse_transform(df_array)
plt.plot(df_array_plot)
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()
print('EQUAL', training_size == len(x_training_df_array))
print('EQUAL', len(training_predict_array) == len(x_training_df_array))
print('EQUAL', testing_size == len(x_testing_df_array))
print('EQUAL', len(testing_predict_array) == len(x_testing_df_array))
print(len(testing_predict_array))
print(len(x_testing_df_array))
print(len(testing_df_array))
print(testing_size)
x_input = testing_df_array[341:].reshape(1, -1)
temp_input = list(x_input)
temp_input = temp_input[0].tolist()
# demonstrate prediction for next 10 days
lst_output = []
n_steps: int = 100
i: int = 0
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

plt.plot(day_new, minMaxScaler.inverse_transform(df_array[1158:]))
plt.plot(day_pred, minMaxScaler.inverse_transform(lst_output))
df3 = df_array.tolist()
df3.extend(lst_output)
plt.plot(df3[1200:])
df3 = minMaxScaler.inverse_transform(df3).tolist()
plt.plot(df3)
