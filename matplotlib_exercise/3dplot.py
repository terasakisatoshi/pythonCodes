from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig=plt.figure()
ax1=fig.add_subplot(121,projection='3d')

X=Y=np.arange(-3.3,3.3,0.3)
X,Y=np.meshgrid(X,Y)

Z=np.cos(np.sqrt(X*X+Y*Y))
ax1.plot_surface(X,Y,Z,rstride=1,cstride=1)

ax2=fig.add_subplot(122,projection='3d')
ax2.scatter3D(np.random.rand(100),np.random.rand(100),np.random.rand(100))

plt.show()
