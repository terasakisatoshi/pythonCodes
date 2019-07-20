import numpy as np
from copy import copy
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

# np.sum(a,axis=0)
def sum_axis0(a):
    s = None
    for i in range(a.shape[0]):
        b=copy(a[i])
        print('b=', b)
        if s is None:
            s = b
        else:
            s += b
    return s

print(sum_axis0(a))

a=a.transpose((1,0))