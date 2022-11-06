## Library usage and structure

(work in progress)

### Short tutorial

Let's consider the following example: the `hadron` function `fun(a1, a2)` takes 2 arguments and returns an object which has an attribute called `M`.
In `python` get `M` as a `numpy.ndarray` as follows:

``` python
import pyhadron # already in sys.path

a1 = pyhadron.wrapper_class_for_a1
a2 = pyhadron.wrapper_class_for_a2

b1 = fun(a1, a2)

b2 = From_R(b1)
b3 = b2.to_numpy("M") # numpy.ndarray
```

Examples scripts are found in the `examples/` directory.

### Detailed explanation

The basis for this library is the `rpy2` python library.

The idea of this library is to have a set of `python` functions homonymus to the ones in the `hadron` library.
The user should be able to call them from python with almost no modifications with respect to `R`. 
When the `R` function takes or returns an `R` class object it works like this:

- The user should  initialize the arguments using either:
  - the conversion functions
  - the class wrappers. 
    These classes are not intended to be used directly in python but as arguments for the `hadron` function wrappers

- The return values are `rpy2` wrappers, which the user can convert to common `python` objects (e.g. pandas DataFrame, numpy array, etc.) using the conversion routines defined in this library. 
