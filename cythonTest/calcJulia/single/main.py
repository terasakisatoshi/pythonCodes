import calc_julia
import numpy as np
from matplotlib import pyplot as plt

jl = calc_julia.calc_julia(1000, (0.322+0.05j))

fig,ax=plt.subplots()
ax.imshow(np.log(jl))
plt.show()
