

import sys 
sys.path.append('../')

import numpy as np
import pandas as pd
import cf
import conversion
import rpy2.robjects as robjects

jackknife_cov = robjects.r["jackknife_cov"]

print("Reading and processing data")
dt = np.array(
        [
        [1.0, 7.0], 
        [3.0, -1.7], 
        [2.0, 0.5], 
        [6.0, -2.0], 
        [7.0, -0.1]
        ]
    )

print(dt)

r_dt = conversion.to_R(dt)
r_dt2 = jackknife_cov(r_dt)

# To pandas DataFrame
pd_dt = robjects.conversion.rpy2py(r_dt2)
print(pd_dt)
