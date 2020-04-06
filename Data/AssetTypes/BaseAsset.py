import pandas as pd
import numpy as np


class BaseAsset(object):
    AssetName: str
    AssetType: str
    ShortType: str

    def __init__(self, a_name: str = 'Asset Name', a_type: str = 'Asset Type', s_type: str = 'Asset'):
        self.AssetName: str = a_name
        self.AssetType: str = a_type
        self.ShortType: str = s_type

    def getSimpleReturn(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        data_frame['SimpleReturn'] = (data_frame['Adj Close'] / data_frame['Adj Close'].shift(1)) - 1
        return data_frame

    def getLogReturn(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        data_frame['log_return'] = np.log(data_frame['Adj Close'] / data_frame['Adj Close'].shift(1))
        return data_frame
