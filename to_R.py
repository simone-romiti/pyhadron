import rpy2.robjects as robjects

def to_R(x):
    return robjects.conversion.py2rpy(x)
####
