import numpy as np
from scipy import linalg as sla
a=np.array([[16,-1,1,2],
            [2,12,1,-1],
            [1,3,-24,2],
            [4,-2,1,20]],dtype='f')
#initial value s.t. np.linang.norm(x) is 1
x=np.array([0.5,0.5,0.5,0.5]).T

epsilon=0.0001
maxiteration=1000

for iteration in range(maxiteration):
    x_new =a@x
    eigen=x_new.dot(x)
    if(np.linalg.norm(x_new-eigen*x)<epsilon):
        break
    #normalize
    x_new/=np.linalg.norm(x_new)
    #update x
    x=x_new
else:
    print("fail to calc eigen value")
    exit(1)

print("num of iteration is %d"%iteration)
print("one of the eigen value of matrix a is %f"%eigen)
print("its eigen vector is \n{}".format(x))
print("compare SciPy result...")
print(sla.eig(a))

