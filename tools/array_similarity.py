import numpy as np 

def simeq(tar,ref):
    return np.all(tar-ref < 1e-1)

tar=np.array([1,3,5])
ref=np.array([1.0001,3.0001,5.0001])

print(simeq(tar,ref))
