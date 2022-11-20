"""
conversion of R object to common python type.
Example: R dataframe to pandas dataframe
"""

import numpy as np
import pandas as pd
import rpy2
from rpy2.robjects.pandas2ri import py2rpy, rpy2py
rpy2.robjects.pandas2ri.activate() # necessary for the conversion to happen!

def names(obj):
    return obj.names
####

def get(obj, key):
    """
    Returns attribute of the R object

        Parameters:
                obj (rpy2.robjects): An R object
                key (str): nema of the attribute

        Returns:
                (rpy2.robjects): 'obj' attribute named 'key'
    """
    return obj.rx(key)
####

def to_numpy(obj):
    """
    Returns a numpy array casted from an R object

        Parameters:
                obj (rpy2.robjects): An R object castable into a 2d array

        Returns:
                (numpy.ndarray): array of shape (n1, n2)
    """
    return np.array(obj)[0]
####

def to_dict(obj):
    """
    Returns a dictionary casted from an R object

        Parameters:
                obj (rpy2.robjects): An R object castable into a dictionary

        Returns:
                (dict): python dictionary
    """
    Rdict = {}
    keys = obj.names
    for i in range(len(keys)):
         Rdict[keys[i]] = obj[i]
    return Rdict
####

def to_list(obj):
    """
    Returns a list casted from an R object

        Parameters:
                obj (rpy2.robjects): An R object castable into a list

        Returns:
                (list): python list
    """
    return list(obj)
####

def to_pandas(obj):
    """
    Returns a pandas DataFrame casted from an R object

        Parameters:
                obj (rpy2.robjects): An R object castable into a dataframe

        Returns:
                (pandas.DataFrame): pandas dataframe
    """
    return pd.DataFrame(rpy2py(obj)[0])
####
