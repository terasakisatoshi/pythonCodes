import numpy as np 

h=1e-4
def numerical_gradient(func,x):
    grad=np.zeros_like(x)
    iterator=np.nditer(x,flags=['multi_index'],op_flags=['readwrite'])
    while not iterator.finished:
        idx=iterator.multi_index
        tmp_val=x[idx]
        x[idx]=float(tmp_val)+h
        fxh1=func(x)
        x[idx]=float(tmp_val)-h
        fxh2=f(x)
        grad[idx]=(fx1-fx2)/(2*h)
        x[idx]=tmp_val
        iterator.iternext()
    return grad


x=np.arange(6).reshape(2,3)
print(x)
iterator=np.nditer(x,flags=['multi_index'])
while not iterator.finished:
    idx=iterator.multi_index
    print(idx,x[idx])
    iterator.iternext()

print(x)