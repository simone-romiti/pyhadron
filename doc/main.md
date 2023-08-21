# How to use the library


## Examples

See the `test` folder for some examples. Here's a simple one:

```
import numpy as np

import pyhadron
hadron = pyhadron.hadron 

from pyhadron.convert import from_R
from pyhadron.convert import from_python

# generating random data
data = np.random.rand(100,3)
print(data)

# running the hadron::uwerr routine
u1_R = hadron.uwerrprimary(data = from_python.to_R(data), pl = True)

# converting the result to useble python data
u1_python = from_R.to_dict(u1_R) # because I know uwerr gives a "list"
print(u1_python.keys())
print(u1_python["Gamma"])

```

