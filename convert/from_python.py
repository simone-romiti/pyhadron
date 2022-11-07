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
