import numpy as np
from matplotlib import pyplot as plt

# solve ODE y^{(maxdeg)}=F(x,y',\dots,y^{(maxdeg-1)})
maxdeg = 2

x_init = 0.0
# y(0)=0,y'(0)=-1.0
y0_init, y1_init = 0.0, -1.0
# F=-y
F = lambda x, y: -y[0]
# set initial value
x = x_init
y = np.array([y0_init, y1_init])
# create tmp array to define fv
fs = [lambda x, y: y[k+1] for k in range(maxdeg-1)]
fs.append(lambda x, y: F(x, y))

fv = lambda x, y: np.array([fs[k](x, y) for k in range(len(fs))])
# apply Heun method
phi = lambda x, y: (fv(x, y) + fv(x+h, y+h*fv(x, y)))/2.0

maxiterator = 1000
h = 0.1
xplt, ys = [], []
for i in range(maxiterator):
    xplt.append(x)
    ys.append(y.copy())
    x += h
    y += h*phi(x, y)


yplt = np.array(ys).transpose()[0]
plt.plot(xplt, yplt)
plt.show()
