from ctypes import cdll, c_double
import sys
print(sys.version)

lib = cdll.LoadLibrary("libadd.so")
lib.add.argtypes = [c_double, c_double]
lib.add.restype = c_double
ret = c_double(lib.add(c_double(3), c_double(4)))
print(ret)
