import numpy as np
from matplotlib import pyplot as plt

f = lambda x, y: x**2 + 2 * x * y + 3
df_dx = lambda x, y: 2 * x + 2 * y
df_dy = lambda x, y: 2 * x

interval = 0.25
xs = np.arange(-2, 2 + interval, interval)
ys = np.arange(-2, 2 + interval, interval)

XX, YY = np.meshgrid(xs, ys)
zs = f(XX, YY)
zs_dx = df_dx(XX, YY)
zs_dy = df_dy(XX, YY)

fig, (ax1, ax2) = plt.subplots(1, 2)
cs = ax1.contour(XX, YY, zs, 10, colors='black')
ax1.clabel(cs, fmt='%2.0f', fontsize=8)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_aspect("equal")

ax2.quiver(XX, YY, zs_dx, zs_dy)
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax2.set_aspect("equal")

plt.tight_layout()
plt.show()
