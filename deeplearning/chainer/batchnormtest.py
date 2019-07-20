import chainer.links as L
import chainer.functions as F

bn = L.BatchNormalization(3)
print(bn.avg_mean)
print(bn.avg_var)
print(bn.beta.data)
print(bn.gamma.data)
