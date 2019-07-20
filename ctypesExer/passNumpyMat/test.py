import numpy as np
from numpy.ctypeslib import ndpointer

lib = np.ctypeslib.load_library("libhandletensor.so", ".")
tensor_type = ndpointer(dtype=np.float32, shape=(
    3 * 4 * 5,), flags="C_CONTIGUOUS")
restype = ndpointer(dtype=np.float32, shape=(6 * 4 * 5,), flags="C_CONTIGUOUS")

lib.handle_tensor.argtypes = [tensor_type, restype]
lib.handle_tensor.restype = None

tensor = np.arange(3 * 4 * 5).astype(np.float32)
tensor = tensor.reshape(3, 4, 5)
print(tensor[1])
res = np.zeros(2 * 3 * 4 * 5).astype(np.float32)

lib.handle_tensor(tensor.ravel(), res)
print(res[1])
