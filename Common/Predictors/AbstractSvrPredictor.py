from Common.Predictors.AbstractPredictor import AbstractPredictor, abstractmethod


class AbstractSvrPredictor(AbstractPredictor):

    @abstractmethod
    def _setData(self):
        pass

    @abstractmethod
    def _setForecast(self):
        pass

    @abstractmethod
    def _setIndependent(self):
        pass

    @abstractmethod
    def _setDependent(self):
        pass
