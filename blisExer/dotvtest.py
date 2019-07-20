"""
git clone https://github.com/explosion/cython-blis.git
cd cython-blis
pip intall .
Note that do not use `pip install blis` because blis.py is not defined
"""
import array
import time

import numpy as np
from blis.py import dotv

v1 = np.array([1, 2, 3]).astype(np.float32)
v2 = np.array([4, 5, 6]).astype(np.float32)
v1 = array.array('f', [1, 2, 3])
v2 = array.array('f', [4, 5, 6])
print(dotv(v1, v2))
print(np.dot(v1, v2))

start = time.time()
for i in range(1000000):
    dotv(v1, v2)
print(time.time() - start)

start = time.time()
for i in range(1000000):
    np.dot(v1, v2)
print(time.time() - start)
