"""
pyhadron

A python wrapper for the `R` library `hadron`.
"""

__package__ = "pyhadron"
__version__ = "0.1.0"
__author__ = 'Simone Romiti'
__credits__ = 'C. Urbach et. al. : https://github.com/HISKP-LQCD/hadron'


import yaml
import os
import glob
import rpy2
from rpy2.robjects.packages import importr

## basic configuration
base = importr('base') # R base package

## disabling r warnings
## this is the default. The user can re-enble them with R_warnings.enable()
rpy2.rinterface_lib.callbacks.logger.setLevel(50)  # 50 suppresses all warnings
 

## default plotting
grDevices = importr("grDevices") # enables R plots generation
grDevices.pdf("Rplots.pdf") # R default

## wrapping hadron

import pkg_resources
distribution = pkg_resources.get_distribution(__package__)
yaml_file_path = os.path.abspath(os.path.expanduser(distribution.location+"/"+__package__+"/info.yaml"))

with open(yaml_file_path, "r") as yaml_file:
    nd = yaml.safe_load(yaml_file)
####

# path to the installation directory
HADRON_LOC = os.path.abspath(os.path.expanduser(nd["hadron_inst_dir"]))

# path to the hadron documentation
HADRON_DOC = glob.glob(os.path.join(HADRON_LOC, "hadron_*.pdf"))

hadron = importr('hadron', lib_loc = HADRON_LOC) # hadron package

