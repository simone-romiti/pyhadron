# cf.py
# Definition of cf and cf-derived classes

import numpy as np

from rpy2.robjects.packages import importr
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate() # necessary!

hadron_lib_loc = "/home/simone/Documents/software-stack/install/hadron/master/"
importr("hadron", lib_loc = hadron_lib_loc)

class cf:
    def __new__(self):
        return robjects.r["cf"]()
    ####
####

class cf_meta(cf):
    def __new__(self, cf, nrObs = 1, Time = robjects.r("NULL"), nrStypes = 1, symmetrised = False):
        return robjects.r["cf_meta"](cf, nrObs, Time, nrStypes, symmetrised)
    ####
####

class cf_orig(cf):
    def __new__(self, cf_in = cf(), cf1: np.ndarray = np.ndarray((0,0)), icf1 = None):
        nr,nc = cf1.shape
        M_cf = robjects.r.matrix(cf1, nrow=nr, ncol=nc)
        if(icf1 == None):
            M_icf = robjects.r("NULL")
        else:
            M_icf = robjects.r.matrix(icf1, nrow=nr, ncol=nc)
        ####
        return robjects.r["cf_orig"](cf_in, M_cf, M_icf)
    ####
####



