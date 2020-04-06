from AssetTypes.BaseAsset import BaseAsset


class GovernmentBond(BaseAsset):

    def __init__(self, a_name: str = 'Asset Name'):
        super().__init__(a_name, 'Government Bond', 'Bond')
