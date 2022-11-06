# pyhadron

This repository contains a python wrapper for the `hadron` library (written in the `R` language): https://github.com/HISKP-LQCD/hadron.
See the `doc/` folder for the documentation.

## Installation

### Dependencies

Install the python dependencies:

``` bash
pip install numpy pandas rpy2
```

### Installation

(installation instructions)


## Status of the project


1. (in progress) 
  I've looked at all `class` definitions in `hadron` and created `r2py` wrappers for them.
  I created a set of wrapper classes for the classed defined in the `hadron` library. 
  Implemented so far: `cf`, `cf_meta`, `cf_orig`

2. (to be done)
  Write a script that produces a `.py` file with the homonymous wrappers of the `hadron` functions.