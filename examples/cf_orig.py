# Creating a cf_orig from a matrix

import numpy as np
import sys 
sys.path.append('../')

import cf
import conversion

print("Creating cf_orig object from matrix")
newcf = cf.cf()
newcf_meta = cf.cf_meta(newcf)

M = np.zeros((10, 4))
M[5,3] = 77 
newcf_orig = cf.cf_orig(newcf_meta, M)

print("Converting cf attribute to numpy array")
myRcf = conversion.From_R(newcf_orig)
print(myRcf["cf"])

M1 = myRcf.to_numpy("cf")
print(M1)

print("Converting cf attribute to pandas dataframe")
M2 = myRcf.to_pandas("cf")
print(M2)



