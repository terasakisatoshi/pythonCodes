import numpy as np
from scipy.io import loadmat, savemat, whosmat

obj_arr = np.zeros((2,), dtype=np.object)
obj_arr[0] = 1
obj_arr[1] = 'a string'

savemat('np_cells.mat', {'obj_arr': obj_arr})
mat = loadmat('np_cells.mat', squeeze_me=True)
obj = mat['obj_arr']
print(obj)
print(obj[0])
print(obj[1])
