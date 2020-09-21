from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Predictors.AbstractPredictor import AbstractPredictor
from Common.Predictors.Tree.DecisionTreePredictor import DecisionTreePredictor
from Common.Predictors.Linear.LinearPredictor import LinearPredictor
from Common.Predictors.Svr.LinearSvrPredictor import LinearSvrPredictor
from Common.Predictors.Svr.PolySvrPredictor import PolySvrPredictor
from Common.Predictors.Svr.RbfSvrPredictor import RbfSvrPredictor
from Common.Predictors.Keras.KerasPredictor import KerasPredictor

yahooStockOption: YahooStockOption = YahooStockOption('AAPL')
print(yahooStockOption.HistoricalData.describe(include='all'))
predictor_list = []
#abstractPredictor: AbstractPredictor =\
#    DecisionTreePredictor(60, 'Adj Close', yahooStockOption.HistoricalData, yahooStockOption.TimeSpan)
# from sklearn.cross_validation import train_test_split -> from sklearn.model_selection import train_test_split
# & GridSearchCV

