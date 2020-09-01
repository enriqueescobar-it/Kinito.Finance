from Common.Predictors.AbstractPredictor import AbstractPredictor
from sklearn.tree import DecisionTreeRegressor


class DecisionTreePredictor(AbstractPredictor):
    __model: DecisionTreeRegressor

    def __init__(self, span: int = 60):
        self.__model = DecisionTreeRegressor()
        self.__span = span
        self.__name = 'DecisionTree'
        self.__column = 'Prediction' + self.__name + str(span)
