import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

xs = np.arange(-3, 3, 0.1)
y_sin = np.sin(xs)
y_cos = np.cos(xs)

print("type(ax1: {}".format(type(ax1)))

ax1.plot(xs, y_sin)
ax2.plot(xs, y_cos)

ax1.set_ylim(-1.3, 1.3)
ax2.set_ylim(-1.3, 1.3)

ax1.set_title(r"$\sin x")
ax2.set_title(r"$\cos x")

fig.tight_layout()
plt.show()
