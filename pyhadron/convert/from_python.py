import rpy2.robjects as robjects

def to_R(x):
    """
    Returns rpy2 object generated from 'x'

        Parameters:
                x : A python object castable into an rpy2.robjects

        Returns:
                (rpy2.robjects): rpy2 equivalent of 'x'
    """
    return robjects.conversion.py2rpy(x)
####

def to_R_list(attrs):
    """
    Returns rpy2 object ListVector

        Parameters:
                d : A python dictionary for the R list attributes 

        Returns:
                (rpy2.robjects.ListVector): R list with attributes specified by d
    """
    return robjects.ListVector(attrs)
####