import numpy as np

for p in [100, 1000, 10000, 100000]:
    uniform = np.random.random(p)
    xs = uniform ** (1 / 7)
    mu = np.mean(xs)
    print(mu)  # this should converge to 7/8 = 0.875
