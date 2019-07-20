import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
x = np.random.normal(size=100)
sns.set_style('dark')
sns.distplot(x)

plt.show()
