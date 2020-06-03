import os.path as PanOsPath

class StockFileDataFrame(object):
    
    def __init__(self, csv_file: str) -> str:
        
        if (PanOsPath.exists(csv_file) and PanOsPath.isfile(csv_file)):
            print ("+ File exist: " + csv_file)
            self.file_path = csv_file
        else:
            print ("+ File not exist: " + csv_file)

