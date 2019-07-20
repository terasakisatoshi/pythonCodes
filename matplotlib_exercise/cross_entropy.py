# author s.terasaki date 2017/02/11 @ MPS
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
"""
# You can draw graph xkcd-like.
see more delail the following URL
http://www.procrasist.com/entry/python-xkcd
"""
plt.xkcd()

x = np.arange(0, 1, 0.05)
y = np.arange(0, 1, 0.05)
X, Y = np.meshgrid(x, y)

U = np.linspace(0, 1, 100)
V = 1 - U

a, b = 20, 20
W = -a * np.log(U) - b * np.log(V)
Z = -a * np.log(X) - b * np.log(Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color='blue')
ax.plot_wireframe(U, V, W, color="red")
plt.show()
