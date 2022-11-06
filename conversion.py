
import numpy as np
import pandas as pd
import rpy2.robjects as robjects


def to_R(x):
    return robjects.conversion.py2rpy(x)
####

class From_R:
    def __init__(self, obj):
        self.obj = obj 
    ####
    def __getitem__(self, key):
        return self.obj.rx(key)
    ####
    def to_numpy(self, key: str):
        return np.array(self[key])[0]
    ####
    def to_pandas(self, key: str):
        return pd.DataFrame(self.to_numpy(key))
####
