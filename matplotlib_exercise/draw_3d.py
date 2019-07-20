from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 1)
y = np.arange(-10, 10, 1)
X, Y = np.meshgrid(x, y)

a,b,c=20,4,20
A=np.array([[a,b],[b,c]])
print(np.linalg.det(A))
Z = a*X**2+2*b*X*Y+c*Y**2

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z) #<---ここでplot

plt.show()