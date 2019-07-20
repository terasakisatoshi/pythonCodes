from single import julia_single
from parallel import julia_parallel
import time

resolution = 50000
c = (0.322+0.05j)
# single
start = time.time()
#jl_single = julia_single.calc_julia(resolution, c)
end = time.time()
single_time=end-start
print("single elapsed =", single_time)
# parallel
start = time.time()
jl_parallel = julia_parallel.calc_julia(resolution, c)
end = time.time()
parallel_time=end-start
print("parallel elapsed =", parallel_time)

print("single/parallel =",single_time/parallel_time)

assert (jl_single == jl_parallel).all()

from matplotlib import pyplot as plt 
import numpy as np
plt.imshow(np.log(jl_single))
plt.show()