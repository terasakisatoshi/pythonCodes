
import math

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis, norm, uniform, kurtosistest


num_samples = 100000

# rvs (Random variates)
n = norm.rvs(loc=0.0, scale=1.0, size=num_samples)
print("for normal distribution N(0, 1),")
print("skew= ", round(skew(n), 4))
print("kurtosis= ", round(kurtosis(n), 4))

triangle = np.array([math.sqrt(u * 16 / num_samples)
                     for u in range(num_samples)])

v = n + triangle * 3.0
print("for incremental shape,")
print("skew= ", round(skew(v), 4))
print("kurtosis= ", round(kurtosis(v), 4))

plt.hist(v, bins=50, normed=True)
plt.show()
