# Creating a cf_orig from a matrix

import numpy as np
import sys 
sys.path.append('../')

import cf
from conversion import *

print("Creating cf_orig object from matrix")
newcf = cf.cf()
newcf_meta = cf.cf_meta(newcf)

M = np.zeros((10, 4))
M[5,3] = 77 
newcf_orig = cf.cf_orig(newcf_meta, M)

print("Converting cf attribute to numpy array")

Rcf = from_R.get(newcf_orig, "cf")
print(Rcf)

M1 = from_R.to_numpy(Rcf)
print(M1)

print("Converting cf attribute to pandas dataframe")
M2 = from_R.to_pandas(Rcf)
print(M2)



