import numpy as np
from scipy.io import loadmat, savemat, whosmat

vect = np.arange(10)
print(vect.shape)
savemat('np_vector.mat', {'vect': vect})
mat = loadmat('np_vector.mat')
print(whosmat('np_vector.mat'))
print(mat['vect'].shape)
