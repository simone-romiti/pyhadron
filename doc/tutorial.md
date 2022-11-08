# Library usage and structure

## Short tutorial

Example: the `hadron` function `fun(a1)` returns an object with an attribute called `M`, and `M` is castable into an `numpy.ndarray` of shape `(n1, n2)`.
In `python` get `M` as follows:

``` python
# pyhadron should be already in sys.path
import pyhadron.Rhadron as Rhadron
from pyhadron.convert import from_R from_python

# a0 defined somewhere above
a1 = from_python.to_R(a0)
Robj1 = fun(a1)
b1 = from_R.to_numpy(from_R.get(obj, "M")) # numpy.ndarray
```

Examples scripts are found in the `examples/` directory.

## Detailed explanation

The basis for this library is the `rpy2` python library.

The idea of this library is to have a set of `python` functions homonymus to the ones in the `hadron` library.
The user should be able to call them from python with almost no modifications with respect to `R`. 
When the `R` function takes or returns an `R` class object it works like this:

- The user should  initialize the arguments using either:
  - the conversion functions

- The return values are `rpy2` wrappers, which the user can convert to common `python` objects (e.g. pandas DataFrame, numpy array, etc.) using the conversion routines defined in this library.

In short, this library is intended to offload to `R` the computation of only `hadron` functions. All the rest (plots, data initialization, etc.) can be done with python.