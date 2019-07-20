"""
Reference:
http://pythonscience.blogspot.com/2014/02/ctypesarray.html
"""
import numpy as np

lib = np.ctypeslib.load_library('libarr.so', '.')
ndtype = np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS')
lib.add_one.argtypes = [ndtype, np.ctypeslib.ct.c_int]
lib.add_one.restype=None

arr = np.arange(10).astype(np.float64)
print("arr=", arr)
ret = lib.add_one(arr, 10)
print("arr=", arr)