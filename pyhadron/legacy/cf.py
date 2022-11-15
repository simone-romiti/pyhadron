# cf.py
# Definition of cf and cf-derived classes

import numpy as np

import Rhadron as hadron

import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate() # necessary!

class cf:
    def __new__(self):
        return hadron.cf()
    ####
####

class cf_meta(cf):
    def __new__(self, _cf = cf(), nrObs = 1, Time = robjects.r("NULL"), nrStypes = 1, symmetrised = False):
        return robjects.r["cf_meta"](_cf, nrObs, Time, nrStypes, symmetrised)
    ####
####

class cf_boot(cf):
    def __new__(self, _cf, boot_R, boot_l, seed, sim, endcorr, cf_tsboot, icf_tsboot = robjects.r("NULL"), resampling_method = 'bootstrap'):
        return robjects.r["cf_boot"](_cf, boot_R, boot_l, seed, sim, endcorr, cf_tsboot, icf_tsboot, resampling_method)
####

class cf_orig(cf):
    def __new__(self, cf_in = cf(), _cf: np.ndarray = np.ndarray((0,0)), i_cf = None):
        nr,nc = _cf.shape
        M_cf = robjects.r.matrix(_cf, nrow=nr, ncol=nc)
        if(i_cf == None):
            M_icf = robjects.r("NULL")
        else:
            M_icf = robjects.r.matrix(i_cf, nrow=nr, ncol=nc)
        ####
        return robjects.r["cf_orig"](cf_in, M_cf, M_icf)
    ####
####

class cf_principal_correlator(cf):
    def __new__(self, _cf, id, gevp_reference_time):
        return robjects.r["cf_principal_correlator"](_cf, id, gevp_reference_time)
####

class cf_shifted(cf):
    def __new__(self, _cf, deltat, forwardshift):
        return robjects.r["cf_shifted"](_cf, deltat, forwardshift)
####

class cf_smeared(cf):
    def __new__(self, _cf, scf, iscf = robjects.r("NULL"), nrSamples=0, obs=None):
        return robjects.r["cf_smeared"](_cf, scf, iscf , nrSamples, obs)
####


class cf_subtracted(cf):
    def __new__(self, _cf, subtracted_values, subtracted_ii):
        return robjects.r["cf_subtracted"](_cf, subtracted_values, subtracted_ii)
####

class cf_weighted(cf):
    def __new__(self, _cf, weight_factor, weight_cosh):
        return robjects.r["cf_weighted"](_cf, weight_factor, weight_cosh)
####
