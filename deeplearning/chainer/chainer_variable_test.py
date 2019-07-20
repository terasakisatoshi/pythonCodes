import numpy as np 
import chainer 
from chainer import cuda,Function,gradient_check,report,training,utils,Variable
from chainer import datasets,iterators,optimizers,serializers 
from chainer import Link,Chain,ChainList 
from chainer import functions as F 
from chainer import links as L 
from chainer.training import extensions 

def VariableTest1():
    x=np.array([5],dtype=np.float32)
    x=Variable(x)
    y=x**2-2*x+1
    print(y,y.data)
    y.backward()
    print(x.grad)
    z=2*x
    y=x**2-z+1
    y.backward()
    print("x.grad",x.grad)
    print("z.grad",z.grad)
    """
    preserve gradient information of intermediate variable
    """
    y.backward(retain_grad=True)
    print("z.grad",z.grad)

def VariableTest2():
    x=Variable(np.array([[1,2,3],[4,5,6]],dtype=np.float32))
    y=x**2-2*x+1
    """
    Note that if we want to start backward computation from a variable holding a multi-element array,
    we must set the initial error manually.
    This is done simply by setting the grad attribute of the output variable
    i.e. y.gras=np.ones
    """
    y.grad=np.ones((2,3),dtype=np.float32)
    y.backward()
    print(x.grad)

def LinkTest1():
    f=L.Linear(3,2)
    f.W.data=np.array([[1,2,3],[4,5,6]],dtype=np.float32)
    f.b.data=np.array([1,2],dtype=np.float32)
    x=Variable(np.array([[1,2,3],[4,5,6]],dtype=np.float32))
    print(f.W.data,f.b.data,f.W.data.shape)
    y=f(x)
    print(y.data)
    """
    A=1,2,3   
      4 5 6
    B=1,4
      2,3
      3,6
    matrix product AB=14  ,32
                      32 ,77
    """
    #lets backward
    f.cleargrads()
    y.grad=np.ones((2,2),dtype=np.float32)
    y.backward()
    print(f.W.grad)
    print(f.b.grad)
def main():
    LinkTest1()
if __name__ == '__main__':
    main()
