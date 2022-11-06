import numpy as np
import pandas as pd
import rpy2
from rpy2.robjects.pandas2ri import py2rpy, rpy2py
rpy2.robjects.pandas2ri.activate()

def get(obj, key):
    return obj.rx(key)
####

def to_numpy(obj):
    return np.array(obj)[0]
####

def to_dict(obj):
    return dict(obj.obj)
####

def to_list(obj):
    return list(obj.obj)
####

def to_pandas(obj):
    return pd.DataFrame(rpy2py(obj)[0])
####
