# Importing all the R 

import rpy2.robjects as robjects
L_func = robjects.r["lsf.str"]("package:hadron") # list of hadron functions
