# Creating a cf_orig from a matrix

import numpy as np
import sys 
sys.path.append('../')

import Rhadron
import convert.from_R as from_R
# import convert.from_python as from_python

print("Creating cf_orig object from matrix")
newcf = Rhadron.cf()
newcf_meta = Rhadron.cf_meta(newcf)

M = np.zeros((10, 4))
M[5,3] = 77 
newcf_orig = Rhadron.cf_orig(newcf_meta, M)

print("Converting cf attribute to numpy array")

Rcf = from_R.get(newcf_orig, "cf")
print(Rcf)

M1 = from_R.to_numpy(Rcf)
print(M1)

print("Converting cf attribute to pandas dataframe")
M2 = from_R.to_pandas(Rcf)
print(M2)



