

import sys 
sys.path.append('../')

import numpy as np
import pandas as pd
import cf
from conversion import *
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


r_dt = to_R(dt)
r_dt2 = jackknife_cov(r_dt)

print("----------------------")

# To pandas DataFrame
pd_dt = r_dt2
print(pd_dt)
