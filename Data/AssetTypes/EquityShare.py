from Data.AssetTypes.BaseAsset import BaseAsset


class EquityShare(BaseAsset):

    def __init__(self, a_name: str = 'Asset Name'):
        super().__init__(a_name, 'Equity Share', 'Stock')
