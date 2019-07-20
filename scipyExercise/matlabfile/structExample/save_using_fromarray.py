# https://stackoverflow.com/questions/33212855/how-can-i-create-a-matlab-struct-array-from-scipy-io

from numpy.core.records import fromarrays
from scipy.io import loadmat, savemat
import numpy as np
myrec = fromarrays([[1, 10], [2, 20]], names=['field1', 'field2'])
savemat('p.mat', {'myrec': myrec})
mat = loadmat('p.mat', struct_as_record=False, squeeze_me=True)
rec = mat['myrec']
print(rec[0].field1)
print(rec[0].field2)
print(rec[1].field1)
rec[1].field2 = -100
import copy
sample = copy.copy(rec[1])
sample.field2 = -900
rec = np.append(rec, sample)
savemat('pp.mat', {'myrec': rec})
mat = loadmat('pp.mat', struct_as_record=False, squeeze_me=True)
rec = mat['myrec']
print(rec[1].field2)
print(rec[2].field2)
