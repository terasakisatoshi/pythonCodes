import numpy as np 
import chainer 
from chainer import cuda,Function,gradient_check,Variable,optimizers,serializers,utils
from chainer import Link,Chain,ChainList
import chainer.functions as F
import chainer.links as L 

conv1=F.Convolution2D(1,8,31)

x=Variable(np.array([1]).astype(np.float32))

print(conv1(x))